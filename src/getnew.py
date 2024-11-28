import json
from fastapi import APIRouter

router = APIRouter(tags=['10NEW CVEs'])

@router.get("/get/new")
def getnew10():
    json_file = "/home/taras/Desktop/Python-final/task4-part1/src/known_exploited_vulnerabilities.json"
    
    # Load the JSON data
    with open(json_file, "r") as file:
        data = json.load(file)
    
    # Collect results
    results = []
    for i in range(10):
        results.append({
            "CVE": data["vulnerabilities"][i]["cveID"],
            "Name": data["vulnerabilities"][i]["vulnerabilityName"],
            "Date Added": data["vulnerabilities"][i]["dateAdded"]
        })
    
    return results
