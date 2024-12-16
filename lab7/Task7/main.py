# Lab7/Task7/main.py

"""Main script for checking if a string matches a given pattern."""

import os
from typing import List
from lab7.Task7.src.PatternMatcher import PatternMatcher
from lab7.utils.IOHandler import IOHandler
from lab7.utils.consts import TXT_DIR, INPUT_FILES_DIR, OUTPUT_FILES_DIR
from lab7.utils.decorate import measure_time_and_memory


@measure_time_and_memory
def main() -> None:
    """Main function to read input, check pattern matching, and write output."""
    current_directory: str = os.path.dirname(os.path.abspath(__file__))
    txt_directory: str = IOHandler.get_path(current_directory, TXT_DIR)
    input_file_path: str = IOHandler.get_path(txt_directory, INPUT_FILES_DIR, 'input.txt')
    output_file_path: str = IOHandler.get_path(txt_directory, OUTPUT_FILES_DIR, 'output.txt')

    file_lines: List[str] = IOHandler.read_file(input_file_path)
    if len(file_lines) < 2:
        # If there are not enough lines for pattern and string, do not proceed
        IOHandler.write_file(output_file_path, "NO")
        print("Обработка завершена. Результат записан в output.txt")
        return

    # First line contains the pattern
    pattern: str = file_lines[0].strip()
    # Second line contains the string to be matched
    string_to_match: str = file_lines[1].strip()

    # Check if the pattern matches the string
    pattern_matcher: PatternMatcher = PatternMatcher()
    match_result: str = pattern_matcher.matches_pattern(pattern, string_to_match)

    # Write the result to the output file
    IOHandler.write_file(output_file_path, match_result)
    print("Обработка завершена. Результат записан в output.txt")  # Original print statement


if __name__ == "__main__":
    main()
