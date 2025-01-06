# schemas.py
from pydantic import BaseModel

class CountryCreate(BaseModel):
    name: str
    iso3: str
    iso2: str
    numeric_code: int
    phone_code: int
    capital: str
    currency: str
    currency_name: str
    native_name: str
    region: str
    subregion: str
    nationality: str

    class Config:
        orm_mode = True  # Allows compatibility with SQLAlchemy models


class CityCreate(BaseModel):
    name: str
    province_id: int

    class Config:
        orm_mode = True
    
class ProvinceCreate(BaseModel):
    name: str
    country_id: int
    country_code: str
    country_name: str
    state_code: str    

    class Config:
        orm_mode = True
        
        
class SchoolCreate(BaseModel):
    name: str
    type: str
    city_id: int
    
    class Config:
        orm_mode = True