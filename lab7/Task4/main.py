# Lab7/Task4/main.py

"""Main script for finding the length of the LCS of two sequences."""

import os
from typing import List
from lab7.Task4.src.LCSFinder import LCSFinder
from lab7.utils.IOHandler import IOHandler
from lab7.utils.consts import TXT_DIR, INPUT_FILES_DIR, OUTPUT_FILES_DIR
from lab7.utils.decorate import measure_time_and_memory


@measure_time_and_memory
def main() -> None:
    """Main function to read input, compute LCS length, and write output."""
    current_directory: str = os.path.dirname(os.path.abspath(__file__))
    txt_directory: str = IOHandler.get_path(current_directory, TXT_DIR)
    input_file_path: str = IOHandler.get_path(txt_directory, INPUT_FILES_DIR, 'input.txt')
    output_file_path: str = IOHandler.get_path(txt_directory, OUTPUT_FILES_DIR, 'output.txt')

    file_lines: List[str] = IOHandler.read_file(input_file_path)
    if not file_lines:
        # If there is no input data, do not proceed
        return

    # First line contains the number of elements in the first sequence
    num_elements_a_str: str = file_lines[0].strip()
    num_elements_a: int = int(num_elements_a_str)

    # Second line contains the first sequence
    sequence_a_str: str = file_lines[1].strip()
    sequence_a: List[int] = list(map(int, sequence_a_str.split()))

    # Third line contains the number of elements in the second sequence
    num_elements_b_str: str = file_lines[2].strip()
    num_elements_b: int = int(num_elements_b_str)

    # Fourth line contains the second sequence
    sequence_b_str: str = file_lines[3].strip()
    sequence_b: List[int] = list(map(int, sequence_b_str.split()))

    # Initialize the LCS finder and compute the LCS length
    lcs_finder: LCSFinder = LCSFinder()
    lcs_length: int = lcs_finder.longest_common_subsequence(sequence_a, sequence_b)

    # Write the LCS length to the output file
    IOHandler.write_file(output_file_path, str(lcs_length))
    print("Обработка завершена. Результат записан в output.txt")  # Original print statement


if __name__ == "__main__":
    main()
