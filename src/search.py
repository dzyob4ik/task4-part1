from fastapi import APIRouter, Query  # Імпортує APIRouter для створення маршрутизатора та Query для обробки параметрів запиту.
import json  # Імпортує модуль для роботи з JSON-файлами.

router = APIRouter(tags=['Search by keyword'])  
@router.get('/get')  
def search_by_key(query: str = Query(description="Keyword to search for in vulnerabilities")):  
    
    json_file = "/home/taras/Desktop/Python-final/task4-part1/src/known_exploited_vulnerabilities.json"  
    # Вказує шлях до JSON-файлу з відомими вразливостями.
    with open(json_file, "r") as file:  # Відкриває JSON-файл для читання
        data = json.load(file)  # Завантажує дані з JSON-файлу у змінну data
        
    filtered_vulnerabilities = []  # порожній список для збереження знайдених вразливостей
    for vulnerability in data["vulnerabilities"]:  # Ітерує через кожну вразливість у списку
        if query.lower() in json.dumps(vulnerability).lower():  # Перевіряє, чи ключове слово query є у вразливості (case-insensitive)
            filtered_vulnerabilities.append(vulnerability)  # Додає знайдену вразливість до списку filtered_vulnerabilities
    return {"result": filtered_vulnerabilities}  # Повертає словник з ключем result, що містить знайдені вразливості

    
