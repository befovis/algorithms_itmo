# Lab6/Task6/main.py

"""Main script for checking numbers against the Fibonacci sequence."""

import os
from typing import List
from lab6.Task6.src.FibonacciChecker import FibonacciChecker
from lab6.utils.IOHandler import IOHandler
from lab6.utils.consts import TXT_DIR, INPUT_FILES_DIR, OUTPUT_FILES_DIR
from lab6.utils.decorate import measure_time_and_memory


@measure_time_and_memory
def main() -> None:
    """Main function to read input, check Fibonacci numbers, and write output."""
    current_directory: str = os.path.dirname(os.path.abspath(__file__))
    txt_directory: str = IOHandler.get_path(current_directory, TXT_DIR)
    input_file_path: str = IOHandler.get_path(txt_directory, INPUT_FILES_DIR, 'input.txt')
    output_file_path: str = IOHandler.get_path(txt_directory, OUTPUT_FILES_DIR, 'output.txt')

    file_lines: List[str] = IOHandler.read_file(input_file_path)
    if not file_lines:
        # If there are no numbers to check, do not proceed
        return

    # First line contains the number of entries
    num_entries_str: str = file_lines[0].strip()
    num_entries: int = int(num_entries_str)

    # Subsequent lines contain the numbers to check
    numbers_to_check: List[int] = [int(line.strip()) for line in file_lines[1:num_entries + 1]]

    # Initialize the checker and perform Fibonacci checks
    fibonacci_checker: FibonacciChecker = FibonacciChecker()
    check_results: List[str] = fibonacci_checker.process_fibonacci(numbers_to_check)

    # Write the results to the output file
    IOHandler.write_file(output_file_path, "".join(check_results))
    print("Обработка завершена. Результаты записаны в output.txt")  # Original print statement


if __name__ == '__main__':
    main()
