
from fastapi import APIRouter
import requests

API = "845fbb0f-e7d2-48d3-a92c-c74cbe4459d0"
router = APIRouter(tags=['10 CRITICAL CVEs'])
#/get/critical - Має виводити 10 критичних CVE
@router.get("/get/critical")
def getcritical():
    # json_file = "/home/taras/Desktop/Python-final/task4-part1/src/known_exploited_vulnerabilities.json"
    # # Load the JSON data
    # with open(json_file, "r") as file:
    #     data = json.load(file)
    
    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    params ={"cvssV3Severity": "CRITICAL",
             "resultsPerPage": 10}
    headers = { 
            "accept": "application/json",
            "apiKey": API
        }
    response = requests.get(url, headers=headers, params=params)
    return response.json()
    