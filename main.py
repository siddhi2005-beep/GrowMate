from fastapi import FastAPI, File, Form, UploadFile, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Plant
import shutil
import os
from datetime import datetime

# Create uploads folder if it doesn't exist
os.makedirs("uploads", exist_ok=True)

app = FastAPI()

# CORS setup - allow your frontend origin only for better security
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ensure tables are created
Plant.metadata.create_all(bind=engine)

@app.post("/plants/")
async def create_plant(
    name: str = Form(...),
    plant_type: str = Form(...),
    planted_date: str = Form(...),
    notes: str = Form(""),
    image: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    image_url = None

    if image:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        image_filename = f"{timestamp}_{image.filename}"
        image_url = f"uploads/{image_filename}"
        with open(image_url, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

    # Convert date string to date object
    try:
        planted_date_obj = datetime.strptime(planted_date, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")

    new_plant = Plant(
        name=name,
        plant_type=plant_type,
        planted_date=planted_date_obj,
        notes=notes,
        image_url=image_url
    )
    db.add(new_plant)
    db.commit()
    db.refresh(new_plant)
    return {
        "message": "Plant added successfully",
        "plant": {
            "id": new_plant.id,
            "name": new_plant.name,
            "type": new_plant.plant_type,
            "date": new_plant.planted_date.isoformat(),
            "notes": new_plant.notes,
            "image_url": new_plant.image_url
        }
    }

@app.get("/plants/")
def get_plants(db: Session = Depends(get_db)):
    plants = db.query(Plant).all()
    return plants

