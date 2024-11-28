from fastapi import APIRouter, Query
import json 

router = APIRouter(tags=['Search by keyword'])
@router.get('/get')
def search_by_key(query: str = Query(description="Keyword to search for in vulnerabilities")):
    json_file = "/home/taras/Desktop/Python-final/task4-part1/src/known_exploited_vulnerabilities.json"
    
    # Load the JSON data
    with open(json_file, "r") as file:
        data = json.load(file)

    filtered_vulnerabilities = []
    for vulnerability in data["vulnerabilities"]:
        if query.lower() in json.dumps(vulnerability).lower():
            filtered_vulnerabilities.append(vulnerability)

    return {"result": filtered_vulnerabilities}
    
