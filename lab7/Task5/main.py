# Lab7/Task5/main.py

"""Main script for calculating the length of the LCS for three sequences."""

import os
from typing import List
from lab7.Task5.src.LCS3Finder import LCS3Finder
from lab7.utils.IOHandler import IOHandler
from lab7.utils.consts import TXT_DIR, INPUT_FILES_DIR, OUTPUT_FILES_DIR
from lab7.utils.decorate import measure_time_and_memory


@measure_time_and_memory
def main() -> None:
    """Main function to read input, compute LCS length for three sequences, and write output."""
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

    # Fifth line contains the number of elements in the third sequence
    num_elements_c_str: str = file_lines[4].strip()
    num_elements_c: int = int(num_elements_c_str)

    # Sixth line contains the third sequence
    sequence_c_str: str = file_lines[5].strip()
    sequence_c: List[int] = list(map(int, sequence_c_str.split()))

    # Initialize the LCS3 finder and compute the LCS length
    lcs3_finder: LCS3Finder = LCS3Finder()
    lcs3_length: int = lcs3_finder.longest_common_subsequence_3(
        sequence_a, sequence_b, sequence_c
    )

    # Write the LCS length to the output file
    IOHandler.write_file(output_file_path, str(lcs3_length))
    print("Обработка завершена. Результат записан в output.txt")  # Original print statement


if __name__ == "__main__":
    main()
