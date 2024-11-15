import json  # Импортирую модуль JSON для обработки файлов JSON

def task() -> float: #Определена функция с именем task.Аннотация -> float говорит о том, что  функция должна возвращать значение типа float
    with open("input.json") as f:     # открываю файл JSON, Оператор with гарантирует, что файл будет правильно закрыт, f — это файловый объект, который позволяет нам читать содержимое файла.
        return round(sum(item["score"] * item["weight"] for item in json.load(f)), 3)  # json.load преобразует JSON в Python (список словарей)
print(task())
