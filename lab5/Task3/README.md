# Задание №3 по выбору: Обработка сетевых пакетов
## Вариант 11
Студентка ИТМО,  Жмачинская Диана Станиславовна 471934

## Задание
Реализовать алгоритм обработки сетевых пакетов с фиксированным размером буфера. Программа должна корректно вычислять время начала обработки или возвращать -1 для отброшенных пакетов.

## Input / Output

<<<<<<< HEAD
| Input | Output |
|---------------------------------|----------------|
| 2 4 \n 0 1 \n 1 1 \n 2 1 \n 3 1 | 0 \n 1 \n 2 \n 3 |
| 1 3 \n 0 2 \n 1 2 \n 2 2 | 0 \n -1 \n -1 |
| 3 3 \n 0 3 \n 3 1 \n 4 1 | 0 \n 3 \n 4 |

## Ограничения по времени и памяти

- Ограничение по времени: 1 сек.
- Ограничение по памяти: 64 МБ.

## Запуск проекта

<<<<<<< HEAD
1. Клонируйте репозиторий:
```bash
git clone https://github.com/befovis/algorithms_itmo
```
2. Перейдите в папку с проектом:
```bash
cd algorithms_itmo/lab5/task2
```
3. Запустите программу:
```bash
python src/main.py
```

## Тестирование
Для запуска тестов выполните:
```bash
pytest tests/
```
