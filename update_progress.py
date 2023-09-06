from collections import Counter
import shutil
import os
from typing import TextIO


progress_template_path = "progresstemplate.md"
PROGRESS_BAR_LENGTH = 25

SKELETON_PATH = "README.md"
PROGRESS_PATH = "progress_summary.md"
TMP_PATH = ".tmp.md"


def count_progress_file(lines: TextIO) -> Counter:
    lines_trimmed = [line.strip() for line in lines]
    counter = Counter()

    for line in lines_trimmed:
        prefix = line[:5]
        counter[prefix] += 1

    # print(counter)
    filtered_counter = {x: count
                        for x, count in counter.items()
                        if "[" in x and "]" in x}
    # print(counter)
    # print(filtered_counter)
    assert 0 < len(filtered_counter) <= 2, f"Found some weird counters: \n{filtered_counter}"

    return filtered_counter


def gen_progress_bar(size: int, progress: float, maximum: float, minimum: float = 0) -> str:
    # special_characters = "-░▒▓█"
    special_characters = ".:-=+*#%@█"
    # special_characters = "▁▂▃▄▅▆▇█"
    # special_characters = "-▏▎▍▌▋▊▉█"

    normalized_progress = (progress - minimum)/maximum
    in_units = normalized_progress * size
    whole = int(in_units) * special_characters[-1]
    fractional_part = in_units - int(in_units)
    partial = special_characters[int(fractional_part * len(special_characters))]
    empty = (size - len(whole) - 1) * special_characters[0]

    result = whole + partial + empty

    return f"[{result}]"


LANGUAGE_FOLDERS = sorted(["bash",
                           "c",
                           "c#",
                           "cpp",
                           "forth",
                           "go",
                           "haskell",
                           "java",
                           "julia",
                           "kotlin",
                           "python",
                           "rust",
                           "scala",
                           "typescript"])


with open(progress_template_path, "r") as template_f:
    TEMPLATE_NUMBER_OF_LINES = len(template_f.readlines())


# Generate temp file with the progress.

with open(PROGRESS_PATH, "w") as target_f:
    MAXIMUM_PADDING = max(len(lang) for lang in LANGUAGE_FOLDERS)

    target_f.write("<pre>\n")
    for folder in LANGUAGE_FOLDERS:
        while True:
            this_file_path = folder + "/" + "progress.md"
            try:
                with open(this_file_path, "r") as read_f:
                    read_f_lines = read_f.readlines()
                    if TEMPLATE_NUMBER_OF_LINES != len(read_f_lines):
                        print(f"This file is likely out of date: {this_file_path}")

                    box_counters = count_progress_file(read_f_lines)
                    # print(box_counters)
                    done_boxes = box_counters.get("- [x]", 0)
                    total_counters = sum(v for v in box_counters.values())

                    language = f"{folder.title()}"
                    number_progress = f"{done_boxes}/{total_counters}"
                    progress_bar = gen_progress_bar(PROGRESS_BAR_LENGTH, done_boxes, total_counters)
                    line = f"{language:<{MAXIMUM_PADDING+2}} {number_progress:<5} {progress_bar}\n"
                    target_f.write(line)
                    break
            except FileNotFoundError:
                shutil.copyfile(progress_template_path, this_file_path)
            except Exception as e:
                raise e
    target_f.write("</pre>")


# Generate the temp readme, updated with the progress.


with open(SKELETON_PATH, "r") as trg_f:
    lines = trg_f.readlines()

    # Find the start and end of the progress section:
    start_of_progress_section = -1
    end_of_progress_section = -1
    for i, line in enumerate(lines):
        # print(i, line.strip())
        if line.startswith("## Progress") and start_of_progress_section < 0:
            start_of_progress_section = i + 1
        elif start_of_progress_section >= 0 and line.startswith("##") and end_of_progress_section < 0:
            end_of_progress_section = i - 1  # last line of progress section
    if end_of_progress_section < 0 and start_of_progress_section > 0:
        # It's the last section! It starts but doesn't end.
        end_of_progress_section = max(i, start_of_progress_section)

    # Now, keep the lines OUTSIDE the Progress section
    # Replace the inner lines with the content we want

    # First, assert that we found a Progress section
    assert start_of_progress_section >= 0, "Progress section not found."

    with open(PROGRESS_PATH, "r") as src_f:
        with open(TMP_PATH, "w") as tmp_f:
            # Write stuff before Progress section
            for line in lines[:start_of_progress_section]:
                tmp_f.write(line)

            # Write the Progress section
            tmp_f.write("\n")
            for line in src_f.readlines():
                tmp_f.write(line)
            tmp_f.write("\n")

            # Write what comes after the Progress section
            for line in lines[end_of_progress_section:]:
                tmp_f.write(line)

# Replace the current readme with this new readme.

skeleton_backup_path = SKELETON_PATH+".bak"
os.rename(SKELETON_PATH, skeleton_backup_path)
os.rename(TMP_PATH, SKELETON_PATH)

# Clean up the temporary files.

os.remove(SKELETON_PATH+".bak")
os.remove(PROGRESS_PATH)
