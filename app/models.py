from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Country(Base):
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    iso3 = Column(String)
    iso2 = Column(String)
    numeric_code = Column(Integer)
    phone_code = Column(Integer)
    capital = Column(String)
    currency = Column(String)
    currency_name = Column(String)
    native_name = Column(String)
    region = Column(String)
    subregion = Column(String)
    nationality = Column(String, unique=True)
    
class Province(Base):
    __tablename__ = "provinces"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    country_id = Column(Integer, ForeignKey("countries.id"))
    country_code = Column(String)
    country_name = Column(String)
    state_code = Column(String)

class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    province_id = Column(Integer, ForeignKey("provinces.id"))
    country_id = Column(Integer, ForeignKey("provinces.country.id"))

class School(Base):
    __tablename__ = "schools"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)  # primary, secondary or combined
    city_id = Column(Integer, ForeignKey("cities.id"))
