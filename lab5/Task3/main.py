# Lab5/Task3/main.py

"""Main script for processing network packets."""

import os
from typing import List, Tuple
from lab5.Task3.src.NetworkPacketsProcessor import NetworkPacketsProcessor
from lab5.utils.IOHandler import IOHandler
from lab5.utils.consts import TXT_DIR, INPUT_FILES_DIR, OUTPUT_FILES_DIR
from lab5.utils.decorate import measure_time_and_memory


@measure_time_and_memory
def main() -> None:
    """Main function to read input, process network packets, and write output."""
    current_dir: str = os.path.dirname(os.path.abspath(__file__))
    txtf_dir: str = IOHandler.get_path(current_dir, TXT_DIR)
    input_path: str = IOHandler.get_path(txtf_dir, INPUT_FILES_DIR, 'input.txt')
    output_path: str = IOHandler.get_path(txtf_dir, OUTPUT_FILES_DIR, 'output.txt')

    lines: List[str] = IOHandler.read_file(input_path)
    if not lines:
        # If there are no packets, do not output anything
        return

    # First line contains buffer_size and number of packets
    first_line = lines[0].strip().split()
    if len(first_line) == 1:
        buffer_size: int = int(first_line[0])
        n: int = 0
    else:
        buffer_size: int = int(first_line[0])
        n: int = int(first_line[1])

    packets: List[Tuple[int, int]] = []
    for line in lines[1:]:
        arr, proc = line.strip().split()
        packets.append((int(arr), int(proc)))

    processor: NetworkPacketsProcessor = NetworkPacketsProcessor()
    results: List[str] = processor.network_packets(buffer_size, packets)

    # Convert start times to strings, keeping '-1' for dropped packets
    output_lines: List[str] = [time_start for time_start in results]
    IOHandler.write_file(output_path, "\n".join(output_lines))
    print("Обработка завершена. Результаты записаны в output.txt")


if __name__ == '__main__':
    main()
