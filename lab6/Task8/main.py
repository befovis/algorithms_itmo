# Lab6/Task8/main.py

"""Main script for solving hash-related tasks."""

import os
from typing import List
from lab6.Task8.src.HashSolver import HashSolver
from lab6.utils.IOHandler import IOHandler
from lab6.utils.consts import TXT_DIR, INPUT_FILES_DIR, OUTPUT_FILES_DIR
from lab6.utils.decorate import measure_time_and_memory


@measure_time_and_memory
def main() -> None:
    """Main function to read input, solve the hash task, and write output."""
    current_directory: str = os.path.dirname(os.path.abspath(__file__))
    txt_directory: str = IOHandler.get_path(current_directory, TXT_DIR)
    input_file_path: str = IOHandler.get_path(txt_directory, INPUT_FILES_DIR, 'input.txt')
    output_file_path: str = IOHandler.get_path(txt_directory, OUTPUT_FILES_DIR, 'output.txt')

    file_lines: List[str] = IOHandler.read_file(input_file_path)
    if not file_lines:
        # If there is no input data, do not proceed
        return

    # First line contains N, X, A, B
    first_line_values: List[int] = list(map(int, file_lines[0].strip().split()))
    # Second line contains AC, BC, AD, BD
    second_line_values: List[int] = list(map(int, file_lines[1].strip().split()))

    input_data: List[List[int]] = [first_line_values, second_line_values]

    # Initialize the solver and perform the hash task
    hash_solver: HashSolver = HashSolver()
    solution_result: str = hash_solver.solve_hash(input_data)

    # Write the result to the output file
    IOHandler.write_file(output_file_path, solution_result)
    print("Обработка завершена. Результат записан в output.txt")  # Original print statement


if __name__ == '__main__':
    main()
