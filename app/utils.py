import pandas as pd
from app.database import SessionLocal
from app.models import School, City, Province

def import_schools_from_excel(file_path: str):
    df = pd.read_excel(file_path)
    db = SessionLocal()

    for _, row in df.iterrows():
        province = db.query(Province).filter_by(name=row["Province"]).first()
        if not province:
            province = Province(name=row["Province"])
            db.add(province)
            db.commit()

        city = db.query(City).filter_by(name=row["City"], province_id=province.id).first()
        if not city:
            city = City(name=row["City"], province_id=province.id)
            db.add(city)
            db.commit()

        school = School(name=row["School"], city_id=city.id)
        db.add(school)

    db.commit()
    db.close()
