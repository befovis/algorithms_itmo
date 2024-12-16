# Lab5/Task7/main.py

"""Main script for performing heap-based sorting."""

import os
from typing import List
from lab5.Task7.src.HeapSorter import HeapSorter
from lab5.utils.IOHandler import IOHandler
from lab5.utils.consts import TXT_DIR, INPUT_FILES_DIR, OUTPUT_FILES_DIR
from lab5.utils.decorate import measure_time_and_memory


@measure_time_and_memory
def main() -> None:
    """Main function to read input, perform heap sort, and write output."""
    current_directory: str = os.path.dirname(os.path.abspath(__file__))
    txt_directory: str = IOHandler.get_path(current_directory, TXT_DIR)
    input_file_path: str = IOHandler.get_path(txt_directory, INPUT_FILES_DIR, 'input.txt')
    output_file_path: str = IOHandler.get_path(txt_directory, OUTPUT_FILES_DIR, 'output.txt')

    file_lines: List[str] = IOHandler.read_file(input_file_path)
    if not file_lines:
        # If there are no elements to sort, do not proceed
        return

    # First line contains the number of elements
    num_elements_str: str = file_lines[0].strip()
    num_elements: int = int(num_elements_str)

    # Second line contains the array elements
    array_str: str = file_lines[1].strip()
    array: List[int] = list(map(int, array_str.split()))

    # Initialize the sorter and perform heap sort
    sorter: HeapSorter = HeapSorter()
    sorter.heapsort(array)
    array.reverse()  # Reverse to get descending order

    # Write the sorted array to the output file
    sorted_array_str: str = " ".join(map(str, array))
    IOHandler.write_file(output_file_path, sorted_array_str)
    print("Обработка завершена. Результаты записаны в output.txt")  # Original print statement


if __name__ == '__main__':
    main()
