# Константы для директорий и файлов
NUM_TASKS = 10
TASK_DIR_PREFIX = 'Task'
MAIN_SCRIPT = 'main.py'
TXT_DIR = 'txt'
INPUT_FILES_DIR = 'input_files'
OUTPUT_FILES_DIR = 'output_files'
TESTS_DIR = 'tests'


def read_input(file_path):
    """Читает данные из файла и возвращает их в виде списка целых чисел."""
    with open(file_path, "r") as file:
        n = int(file.readline().strip())
        arr = list(map(int, file.readline().strip().split()))
    return n, arr

def write_output(file_path, result):
    """Записывает результат в файл."""
    with open(file_path, "w") as file:
        if isinstance(result, list):
            file.write(" ".join(map(str, result)) + "\n")
        else:
            file.write(str(result) + "\n")