from fastapi import APIRouter  # Імпортує APIRouter для створення маршрутизатора в FastAPI
import json  # Імпортує модуль для роботи з JSON-файлами

router = APIRouter(tags=['10 knownRansomwareCampaignUse CVEs'])  
@router.get("/get/known")  
def getcritical():  
    cves_found = [] #  порожній список для збереження знайдених CVE 
    json_file = "/home/taras/Desktop/Python-final/task4-part1/src/known_exploited_vulnerabilities.json"  
    # Вказує шлях до JSON-файлу з відомими вразливостями
    
    with open(json_file, "r") as file:  # Відкриває JSON-файл для читання
        data = json.load(file)  # Завантажує дані з JSON-файлу у змінну data
    for i in range(len(data["vulnerabilities"])):  # Ітерує через індекси списку вразливостей у JSON-даних.
        if data["vulnerabilities"][i]["knownRansomwareCampaignUse"] == 'Known':  
            # Перевіряє, чи значення поля 'knownRansomwareCampaignUse' дорівнює Known
            cves_found.append(data["vulnerabilities"][i])  # Додає вразливість до списку cves_found
        if len(cves_found) == 10:  # Перериває цикл, якщо знайдено 10 CVE
            break
    return cves_found  # Повертає список знайдених CVE
    

        