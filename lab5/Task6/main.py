# Lab5/Task6/main.py

"""Main script for processing priority queues."""

import os
from typing import List
from lab5.Task6.src.PriorityQueueProcessor import PriorityQueueProcessor
from lab5.utils.IOHandler import IOHandler
from lab5.utils.consts import TXT_DIR, INPUT_FILES_DIR, OUTPUT_FILES_DIR
from lab5.utils.decorate import measure_time_and_memory


@measure_time_and_memory
def main() -> None:
    """Main function to read input, process priority queue operations, and write output."""
    current_directory: str = os.path.dirname(os.path.abspath(__file__))
    txt_directory: str = IOHandler.get_path(current_directory, TXT_DIR)
    input_file_path: str = IOHandler.get_path(txt_directory, INPUT_FILES_DIR, 'input.txt')
    output_file_path: str = IOHandler.get_path(txt_directory, OUTPUT_FILES_DIR, 'output.txt')

    file_lines: List[str] = IOHandler.read_file(input_file_path)
    if not file_lines:
        # If there are no operations, do not output anything
        return

    # First line contains the number of operations
    operation_count: int = int(file_lines[0])
    operation_commands: List[str] = file_lines[1:]

    # Initialize the processor and execute operations
    queue_processor: PriorityQueueProcessor = PriorityQueueProcessor()
    processing_results: List[str] = queue_processor.process_operations(operation_commands)

    IOHandler.write_file(output_file_path, "\n".join(processing_results))
    print("Обработка завершена. Результаты записаны в output.txt")  # Original print statement


if __name__ == '__main__':
    main()
