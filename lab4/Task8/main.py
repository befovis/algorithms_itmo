# Task8/main.py

"""Main script for evaluating postfix expressions."""

import os
from lab4.Task8.src.PostfixEvaluator import PostfixEvaluator
from lab4.utils.consts import TXT_DIR, INPUT_FILES_DIR, OUTPUT_FILES_DIR
from lab4.utils.decorate import measure_time_and_memory
from lab4.utils.IOHandler import IOHandler


@measure_time_and_memory
def main():
    """Main function to execute postfix expression evaluation."""
    # Define file paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    txt_dir = IOHandler.get_path(base_dir, TXT_DIR)
    input_file = IOHandler.get_path(txt_dir, INPUT_FILES_DIR, 'input.txt')
    output_file = IOHandler.get_path(txt_dir, OUTPUT_FILES_DIR, 'output.txt')

    evaluator = PostfixEvaluator()

    # Read and validate input
    try:
        total, tokens = evaluator.load_expression(input_file)
    except (ValueError, IndexError) as e:
        print(f"Error reading input: {e}")
        return

    if not evaluator.validate_expression(total, tokens):
        print("Invalid input data.")
        return

    # Evaluate the expression
    try:
        result = evaluator.evaluate_postfix(tokens)
    except (ValueError, IndexError) as e:
        print(f"Error during evaluation: {e}")
        return

    # Write the result
    evaluator.save_result(output_file, result)
    print(f"Evaluation Result: {result}")
    print("Processing completed. Result saved to output.txt.")


if __name__ == '__main__':
    main()
