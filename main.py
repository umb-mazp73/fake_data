from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

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
            "applianceHours": 0,
            "lightBulbs": 2,
            "gasTanks": 3,
            "hvacHours": 0
        },
        "food": {
            "redMeat": 0,
            "whiteMeat": 5,
            "dairy": 7,
            "vegetarian": 0
        },
        "transport": {
            "carKm": 8,
            "publicKm": 0,
            "domesticFlights": 0,
            "internationalFlights": 0
        },
        "waste": {
            "trashBags": 9,
            "foodWaste": 0,
            "plasticBottles": 0,
            "paperPackages": 0
        },
        "total": 50.0
    }
