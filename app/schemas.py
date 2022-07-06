from typing import Union

from pydantic import BaseModel


class VehicleBase(BaseModel):
    identifier: int
    domain: str


class VehicleCreate(VehicleBase):
    pass


class Vehicle(VehicleBase):
    id: int

    class Config:
        orm_mode = True
