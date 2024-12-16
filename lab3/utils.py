import tracemalloc
import time


NUM_TASKS = 10
TASK_DIR_PREFIX = 'task'
MAIN_SCRIPT = 'main.py'
TXT_DIR = 'txt'
INPUT_FILES_DIR = 'input_files'
OUTPUT_FILES_DIR = 'output_files'
TESTS_DIR = 'tests'


def read_file(file_path):
    """Чтение содержимого файла и возвращение строк в виде списка."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def write_file(data, file_path):
    """Запись данных в файл."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(data)

def measure_time_and_memory(func):
    """Декоратор для измерения времени выполнения и памяти."""
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"Время работы: {end_time - start_time:.4f} секунд")
        print(f"Максимальная память: {peak / 1024:.2f} KB")

        return result
    return wrapper
