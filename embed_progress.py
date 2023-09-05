SKELETON_PATH = "README.md"
PROGRESS_PATH = "progress_summary.md"
TMP_PATH = ".tmp.md"

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




