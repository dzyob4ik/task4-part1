from fastapi import FastAPI
import getnew, getall, getcritical
import json 
app=FastAPI(
    title="NIST CVE API",
    description="FastAPI додаток для отримання інформації про CVE з NIST"
)

@app.get('/')
def text_hello():
    return{'text': 'hello'}

@app.get("/info")
def get_info():
   
    return {
        "app_name": "NIST CVE API Fetcher",
        "version": "1.0.0",
        "Creator": "Taras Dzoban",

    }
   
app.include_router(getnew.router)
app.include_router(getall.router)
app.include_router(getcritical.router)