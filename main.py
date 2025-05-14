from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/fake_data")
def get_survey_data():
    return {
        "date": datetime.utcnow().isoformat(),
        "energy": {
            "applianceHours": 24,
            "lightBulbs": 20,
            "gasTanks": 5,
            "hvacHours": 24
        },
        "food": {
            "redMeat": 14,
            "whiteMeat": 14,
            "dairy": 21,
            "vegetarian": 21
        },
        "transport": {
            "carKm": 1000,
            "publicKm": 500,
            "domesticFlights": 20,
            "internationalFlights": 10
        },
        "waste": {
            "trashBags": 20,
            "foodWaste": 20,
            "plasticBottles": 50,
            "paperPackages": 20
        },
        "total": 50.0
    }

@app.post("/procesar_datos")
async def procesar_datos(request: Request):
    data = await request.json()
    print("Servicio receptor recibió:\n", json.dumps(data, indent=4))
    return {"message": "Datos procesados correctamente"}