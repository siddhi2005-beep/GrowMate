from sqlalchemy import Column, Integer, String, Date
from database import Base  # ✅ Use absolute import

class Plant(Base):
    __tablename__ = "plants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    plant_type = Column(String)
    planted_date = Column(Date)
    image_path = Column(String, nullable=True)  # Renamed to match backend logic
    notes = Column(String, nullable=True)
