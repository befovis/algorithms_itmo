# Задание №7: Сопоставление строки с шаблоном
## Вариант 11
Студентка ИТМО, Жмачинская Диана Станиславовна 471934

## Задание
Реализовать алгоритм, который проверяет соответствие строки шаблону, содержащему специальные символы:
- `?` — соответствует любому одиночному символу.
- `*` — соответствует любому количеству символов (включая 0).

## Input / Output

| Input | Output |
|-----------------|----------|
| a?b, acb | YES |
| a*b, aab | YES |
| ab, abc | NO |

## Ограничения по времени и памяти
- Время: 1 сек.
- Память: 64 МБ.

## Запуск проекта

1. Клонируйте репозиторий:
```bash
git clone https://github.com/befovis/algorithms_and_data_structures
```

2. Перейдите в папку с проектом:
```bash
cd algorithms_and_data_structures/lab7/task7
```

3. Запустите программу:
```bash
python src/main.py
```

<<<<<<< HEAD
4. Для запуска тестов выполните:
```bash
pytest tests/
```
=======
3. Для запуска всех задач и тестов выполните команду:  
```bash  
python run_all.py  
```  
>>>>>>> 97d8e4d6c15bc0c46f69ce2ee047e868e975f69b