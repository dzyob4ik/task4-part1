import json
from fastapi import APIRouter

router = APIRouter(tags=['Last CVEs in 5 days'])
@router.get("/get/all")
def get_recent_cves():
    json_file = "/home/taras/Desktop/Python-final/task4-part1/src/known_exploited_vulnerabilities.json"
    
    with open(json_file, "r") as file:
        data = json.load(file)
    recent_cves = []
    max_cves=40
    recent_dates = ["2024-11-21", "2024-11-20", "2024-11-19", "2024-11-18", "2024-11-17"]
    for vulnerability in data['vulnerabilities']:
        if vulnerability['dateAdded'] in recent_dates:
            recent_cves.append(vulnerability)
        
        if len(recent_cves) == max_cves:
            break

    return recent_cves