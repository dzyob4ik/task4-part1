from fastapi import FastAPI
import getnew, getall, getknown, search

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
        "app_name": "NIST CVE finder",
        "Creator": "Taras Dzoban",

    }
   
app.include_router(getnew.router)
app.include_router(getall.router)
app.include_router(getknown.router)
app.include_router(search.router)