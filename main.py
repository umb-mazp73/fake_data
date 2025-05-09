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
            "applianceHours": 6,
            "lightBulbs": 2,
            "gasTanks": 3,
            "hvacHours": 7
        },
        "food": {
            "redMeat": 9,
            "whiteMeat": 5,
            "dairy": 7,
            "vegetarian": 0
        },
        "transport": {
            "carKm": 8,
            "publicKm": 0,
            "domesticFlights": 11,
            "internationalFlights": 0
        },
        "waste": {
            "trashBags": 9,
            "foodWaste": 0,
            "plasticBottles": 111,
            "paperPackages": 0
        },
        "total": 50.0
    }

@app.post("/procesar_datos")
async def procesar_datos(request: Request):
    data = await request.json()
    print("Servicio receptor recibió:\n", json.dumps(data, indent=4))
    return {"message": "Datos procesados correctamente"}