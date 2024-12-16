# Lab6/Task4/main.py

"""Main script for processing associative array operations."""

import os
from typing import List
from lab6.Task4.src.AssocArrayProcessor import AssocArrayProcessor
from lab6.utils.IOHandler import IOHandler
from lab6.utils.consts import TXT_DIR, INPUT_FILES_DIR, OUTPUT_FILES_DIR
from lab6.utils.decorate import measure_time_and_memory


@measure_time_and_memory
def main() -> None:
    """Main function to read input, process associative array commands, and write output."""
    current_directory: str = os.path.dirname(os.path.abspath(__file__))
    txt_directory: str = IOHandler.get_path(current_directory, TXT_DIR)
    input_file_path: str = IOHandler.get_path(txt_directory, INPUT_FILES_DIR, 'input.txt')
    output_file_path: str = IOHandler.get_path(txt_directory, OUTPUT_FILES_DIR, 'output.txt')

    file_lines: List[str] = IOHandler.read_file(input_file_path)
    if not file_lines:
        # If there are no commands, do not proceed
        return

    # First line contains the number of commands
    num_commands_str: str = file_lines[0].strip()
    num_commands: int = int(num_commands_str)

    # Subsequent lines contain the commands
    command_lines: List[str] = file_lines[1:]

    # Initialize the processor and execute commands
    assoc_processor: AssocArrayProcessor = AssocArrayProcessor()
    processing_results: List[str] = assoc_processor.process_commands(command_lines)

    # Write the results to the output file
    IOHandler.write_file(output_file_path, "\n".join(processing_results))
    print("Обработка завершена. Результаты записаны в output.txt")  # Original print statement


if __name__ == "__main__":
    main()
