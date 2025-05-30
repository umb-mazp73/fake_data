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
            "gasTanks": 20,
            "hvacHours": 5,
            "lightBulbs": 24
        },
        "food": {
            "dairy": 14,
            "redMeat": 14,
            "vegetarian": 21,
            "whiteMeat": 21
        },
        "transport": {
            "carKm": 1000,
            "domesticFlights": 500,
            "internationalFlights": 20,
            "publicKm": 10
        },
        "waste": {
            "foodWaste": 20,
            "paperPackages": 20,
            "plasticBottles": 50,
            "trashBags": 20
        },
        "result": 66.3
    }
    return {"response_data": json_recomendaciones}
