# Lab7/Task6/main.py

"""Main script for finding the Longest Increasing Subsequence (LIS) of a sequence."""

import os
from typing import List, Tuple
from lab7.Task6.src.LISFinder import LISFinder
from lab7.utils.IOHandler import IOHandler
from lab7.utils.consts import TXT_DIR, INPUT_FILES_DIR, OUTPUT_FILES_DIR
from lab7.utils.decorate import measure_time_and_memory


@measure_time_and_memory
def main() -> None:
    """Main function to read input, compute LIS, and write output."""
    current_directory: str = os.path.dirname(os.path.abspath(__file__))
    txt_directory: str = IOHandler.get_path(current_directory, TXT_DIR)
    input_file_path: str = IOHandler.get_path(txt_directory, INPUT_FILES_DIR, 'input.txt')
    output_file_path: str = IOHandler.get_path(txt_directory, OUTPUT_FILES_DIR, 'output.txt')

    file_lines: List[str] = IOHandler.read_file(input_file_path)
    if not file_lines:
        # If there is no input data, do not proceed
        return

    # First line contains the number of elements in the sequence
    num_elements_str: str = file_lines[0].strip()
    num_elements: int = int(num_elements_str)

    # Second line contains the sequence of integers
    sequence_str: str = file_lines[1].strip()
    sequence: List[int] = list(map(int, sequence_str.split()))

    # Initialize the LIS finder and compute the LIS length and sequence
    lis_finder: LISFinder = LISFinder()
    lis_length: int
    lis_sequence: List[int]
    lis_length, lis_sequence = lis_finder.find_lis(sequence)

    # Write the LIS length and sequence to the output file
    IOHandler.write_file(output_file_path, f"{lis_length}\n" + " ".join(map(str, lis_sequence)))
    print("Обработка завершена. Результат записан в output.txt")  # Original print statement


if __name__ == "__main__":
    main()
