from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import vehicle, model, schemas
from .database import SessionLocal, engine


model.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/vehicle_domain/{identifier}", response_model=schemas.Vehicle)
def read_vehicle(identifier: int, db: Session = Depends(get_db)):
    db_vehicle = vehicle.get_vehicle_by_identifier(db, identifier=identifier)

    if db_vehicle is None:
        vehicle_data = {
            "identifier": identifier,
            "domain": vehicle.get_domain(identifier),
        }
        return vehicle.create_vehicle(db=db, vehicle=vehicle_data)

    return db_vehicle


@app.get("/vehicle_identifier/{domain}", response_model=schemas.Vehicle)
def read_vehicle(domain: str, db: Session = Depends(get_db)):
    db_vehicle = vehicle.get_vehicle_by_domain(db, domain=domain)

    if db_vehicle is None:
        vehicle_data = {
            "identifier": vehicle.get_identifier(domain),
            "domain": domain,
        }
        return vehicle.create_vehicle(db=db, vehicle=vehicle_data)

    return db_vehicle
