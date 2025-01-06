from fastapi import APIRouter, HTTPException
from app.database import SessionLocal
from app.models import School, City, Province, Country
from app.schemas import CountryCreate  # Import the CountryCreate Pydantic model

router = APIRouter()

@router.get("/schools")
async def get_schools():
    db = SessionLocal()
    schools = db.query(School).all()
    db.close()
    return schools

@router.get("/schools/{type}")
async def get_schools_by_type(type: str):
    db = SessionLocal()
    schools = db.query(School).filter_by(type=type).all()
    db.close()
    return schools
# get schools by type and city

@router.get("/schools/{type}/{city}")
async def get_schools_by_type_and_city(type: str, city: str):
    db = SessionLocal()
    schools = db.query(School).filter_by(type=type, city=city).all()
    db.close()
    return schools

@router.post("/add-school")
async def add_school(name: str, type: str, city_id: int):
    db = SessionLocal()
    new_school = School(name=name, type=type, city_id=city_id)
    db.add(new_school)
    db.commit()
    db.close()
    return {"message": f"School '{name}' added successfully"}

# add list of schools from excel with city name
@router.post("/import-schools")
async def import_schools_from_excel(file_path: str):
    try:
        db = SessionLocal()
        import_schools_from_excel(file_path)
        db.close()
        return {"message": "Schools imported successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# add a province
@router.post("/add-province")
async def add_province(name: str, country_id: int, country_code: str, country_name: str, state_code: str):
    db = SessionLocal()
    new_province = Province(name=name, country_id=country_id, country_code=country_code, country_name=country_name, state_code=state_code)
    db.add(new_province)
    db.commit()
    db.close()
    return {"message": f"Province '{name}' added successfully"}

# adding provinces from an excel file
@router.post("/import-provinces")
async def import_provinces_from_excel(file_path: str):
    try:
        db = SessionLocal()
        import_provinces_from_excel(file_path)
        db.close()
        return {"message": "Provinces imported successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    # adding cities from an excel file


# add a city
@router.post("/add-city")
async def add_city(name: str, province_id: int):
    db = SessionLocal()
    new_city = City(name=name, province_id=province_id)
    db.add(new_city)
    db.commit()
    db.close()
    return {"message": f"City '{name}' added successfully"}

@router.post("/import-cities")
async def import_cities_from_excel(file_path: str):
    try:
        db = SessionLocal()
        import_cities_from_excel(file_path)
        db.close()
        return {"message": "Cities imported successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    #adding countries from an excel file

# add a country
@router.post("/add-country")
async def add_country(country: CountryCreate):
    try:
        db = SessionLocal()
        new_country = Country(
            name=country.name,
            iso3=country.iso3,
            iso2=country.iso2,
            numeric_code=country.numeric_code,
            phone_code=country.phone_code,
            capital=country.capital,
            currency=country.currency,
            currency_name=country.currency_name,
            native_name=country.native_name,
            region=country.region,
            subregion=country.subregion,
            nationality=country.nationality
        )
        db.add(new_country)
        db.commit()
        db.close()
        return {"message": f"Country '{country.name}' added successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/import-countries")
async def import_countries_from_excel(file_path: str):
    try:
        db = SessionLocal()
        import_countries_from_excel(file_path)
        db.close()
        return {"message": "Countries imported successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))