import json # Імпортує модуль для роботи з JSON-файлами
from fastapi import APIRouter# Імпортує APIRouter для створення маршрутизатора в FastAPI

router = APIRouter(tags=['10NEW CVEs'])

@router.get("/get/new")
def getnew10():
    json_file = "/home/taras/Desktop/Python-final/task4-part1/src/known_exploited_vulnerabilities.json"
    # Вказує шлях до JSON-файлу з відомими вразливостями
    with open(json_file, "r") as file: # Відкриває JSON-файл для читання
        data = json.load(file) # Завантажує дані з JSON-файлу у змінну data
    results = [] #  порожній список для збереження знайдених CVE 
    for i in range(10): # Ітерує через перші 10 найновіших вразливостей у списку
        results.append({ # Додає до списку results словник з даними про CVE
            "CVE": data["vulnerabilities"][i]["cveID"],  #ітерує по індексу
            "Name": data["vulnerabilities"][i]["vulnerabilityName"],
            "Date Added": data["vulnerabilities"][i]["dateAdded"]
        })
    
    return results #Повертає список з 10 нових CVE
