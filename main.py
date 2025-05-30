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
            "applianceHours": 1,
            "gasTanks": 3,
            "hvacHours": 4,
            "lightBulbs": 1
        },
        "food": {
            "dairy": 5,
            "redMeat": 1,
            "vegetarian": 0,
            "whiteMeat": 1
        },
        "transport": {
            "carKm": 1,
            "domesticFlights": 1,
            "internationalFlights": 0,
            "publicKm": 1
        },
        "waste": {
            "foodWaste": 5,
            "paperPackages": 1,
            "plasticBottles": 1,
            "trashBags": 1
        },
        "result": 66.3
    }
    return {"response_data": json_recomendaciones}
