
from fastapi import APIRouter
import json


router = APIRouter(tags=['10 knownRansomwareCampaignUse CVEs'])

@router.get("/get/known")
def getcritical():
    cves_found = []
    json_file = "/home/taras/Desktop/Python-final/task4-part1/src/known_exploited_vulnerabilities.json"
    
    with open(json_file, "r") as file:
        data = json.load(file)

    for i in range(len(data["vulnerabilities"])):
        if data["vulnerabilities"][i]["knownRansomwareCampaignUse"] == 'Known':
            cves_found.append(data["vulnerabilities"][i]) 
        if len(cves_found) == 10:  
            break

    return cves_found
        