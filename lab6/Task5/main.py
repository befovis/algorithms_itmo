# Lab6/Task5/main.py

"""Main script for processing election results."""

import os
from typing import List, Tuple
from lab6.Task5.src.ElectionsProcessor import ElectionsProcessor
from lab6.utils.IOHandler import IOHandler
from lab6.utils.consts import TXT_DIR, INPUT_FILES_DIR, OUTPUT_FILES_DIR
from lab6.utils.decorate import measure_time_and_memory


@measure_time_and_memory
def main() -> None:
    """Main function to read input, process election results, and write output."""
    current_directory: str = os.path.dirname(os.path.abspath(__file__))
    txt_directory: str = IOHandler.get_path(current_directory, TXT_DIR)
    input_file_path: str = IOHandler.get_path(txt_directory, INPUT_FILES_DIR, 'input.txt')
    output_file_path: str = IOHandler.get_path(txt_directory, OUTPUT_FILES_DIR, 'output.txt')

    file_lines: List[str] = IOHandler.read_file(input_file_path)
    if not file_lines:
        # If there is no data, do not proceed
        return

    election_entries: List[Tuple[str, str]] = []
    for entry_line in file_lines:
        parts = entry_line.strip().split()
        if len(parts) == 2:
            candidate, vote_str = parts
            election_entries.append((candidate, vote_str))

    election_processor: ElectionsProcessor = ElectionsProcessor()
    processed_results: List[str] = election_processor.process_elections(election_entries)

    # Write the processed election results to the output file
    IOHandler.write_file(output_file_path, "".join(processed_results))
    print("Обработка завершена. Результаты записаны в output.txt")  # Original print statement


if __name__ == '__main__':
    main()
