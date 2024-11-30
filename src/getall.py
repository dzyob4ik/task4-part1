import json  # Імпортує модуль для роботи з JSON-файлами
from fastapi import APIRouter  # Імпортує APIRouter для створення маршрутизатора в FastAPI

router = APIRouter(tags=['Last CVEs in 5 days'])  # Створює об'єкт маршрутизатора з тегом для групування маршрутів у документації FastAPI

@router.get("/get/all")  
def get_recent_cves():  
    json_file = "/home/taras/Desktop/Python-final/task4-part1/src/known_exploited_vulnerabilities.json"  
    # Визначає шлях до JSON-файлу з відомими вразливостями
    
    with open(json_file, "r") as file:  # Відкриває JSON-файл для читання
        data = json.load(file)  # Завантажує дані з JSON-файлу у змінну 
    
    recent_cves = []  # Ініціалізує порожній список для збереження нещодавніх CVE
    max_cves = 40  # Визначає максимальну кількість CVE, які потрібно повернути
    recent_dates = ["2024-11-21", "2024-11-20", "2024-11-19", "2024-11-18", "2024-11-17"]  
    # Список дат для фільтрації вразливостей за останні 5 днів
    
    for vulnerability in data['vulnerabilities']:  # Ітерує через список вразливостей у JSON-даних.
        if vulnerability['dateAdded'] in recent_dates:  # Перевіряє, чи дата додавання вразливості є в списку нещодавніх дат
            recent_cves.append(vulnerability)  # Додає вразливість до списку recent_cves
        if len(recent_cves) == max_cves:  # Перевіряє, чи досягнуто максимальну кількість CVE
            break  # Перериває цикл, якщо зібрано максимальну кількість CVE

    return recent_cves  # Повертає список нещодавніх CVE.
