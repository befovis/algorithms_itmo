"""Main script for calculating the height of a tree."""

import os
from typing import List
from lab5.Task2.src.TreeHeightCalculator import TreeHeightCalculator
from lab5.utils.IOHandler import IOHandler
from lab5.utils.consts import TXT_DIR, INPUT_FILES_DIR, OUTPUT_FILES_DIR
from lab5.utils.decorate import measure_time_and_memory


@measure_time_and_memory
def main() -> None:
    """Main function to read input, calculate tree height, and write output."""
    current_dir: str = os.path.dirname(os.path.abspath(__file__))
    txtf_dir: str = IOHandler.get_path(current_dir, TXT_DIR)
    input_path: str = IOHandler.get_path(txtf_dir, INPUT_FILES_DIR, 'input.txt')
    output_path: str = IOHandler.get_path(txtf_dir, OUTPUT_FILES_DIR, 'output.txt')

    lines: List[str] = IOHandler.read_file(input_path)
    n: int = int(lines[0].strip())
    parents: List[int] = list(map(int, lines[1].split()))

    calculator: TreeHeightCalculator = TreeHeightCalculator()
    result: int = calculator.tree_height(n, parents)

    IOHandler.write_file(output_path, str(result))
    print("Обработка завершена. Результат записан в output.txt")  # Original print statement


if __name__ == '__main__':
    main()
