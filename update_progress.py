from collections import Counter
import shutil
from typing import TextIO


progress_template_path = "progresstemplate.md"
PROGRESS_BAR_LENGTH = 25


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
    special_characters = "-░▒█"

    normalized_progress = (progress - minimum)/maximum
    in_units = normalized_progress * size
    whole = int(in_units) * special_characters[-1]
    fractional_part = in_units - int(in_units)
    partial = special_characters[int(fractional_part * len(special_characters))]
    empty = (size - len(whole) - 1) * special_characters[0]

    result = whole + partial + empty

    return f"|{result}|"


LANGUAGE_FOLDERS = ["bash",
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
                    "typescript"]

with open(progress_template_path, "r") as template_f:
    TEMPLATE_NUMBER_OF_LINES = len(template_f.readlines())

with open("progress_summary.md", "w") as target_f:
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

                    language = f"{folder.title()}:"
                    number_progress = f"{done_boxes}/{total_counters}"
                    progress_bar = gen_progress_bar(PROGRESS_BAR_LENGTH, done_boxes, total_counters)
                    line = f"{language:<{MAXIMUM_PADDING+2}} {number_progress:<5} {progress_bar}  \n"
                    target_f.write(line)
                    break
            except FileNotFoundError:
                shutil.copyfile(progress_template_path, this_file_path)
            except Exception as e:
                raise e
    target_f.write("</pre>")
