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

@app.post("/enviar_calculos")
async def enviar_calculos():
    json_recomendaciones = {
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
    return {"response_data": json_recomendaciones}
