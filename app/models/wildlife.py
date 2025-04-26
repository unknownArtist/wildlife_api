from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Float, Date, Boolean
from datetime import date



class Wildlife(Base):
    __tablename__ = 'wildlife'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    department: Mapped[str] = mapped_column(String(254))
    conservation_name_english: Mapped[str] = mapped_column(String(254))
    conservation_area: Mapped[str] = mapped_column(String(254))
    conservation_status: Mapped[str] = mapped_column(String(254))
    count: Mapped[float] = mapped_column(Float)
    location: Mapped[str] = mapped_column(String(254))
    united: Mapped[str] = mapped_column(String(254))
    site: Mapped[str] = mapped_column(String(254))
    mountain: Mapped[str] = mapped_column(String(254))
    wadi: Mapped[str] = mapped_column(String(254))
    ranger: Mapped[str] = mapped_column(String(254))
    contact_person: Mapped[str] = mapped_column(String(254))
    telephone_number: Mapped[float] = mapped_column(Float)
    east: Mapped[float] = mapped_column(Float)
    north: Mapped[float] = mapped_column(Float)
    date_entry: Mapped[date] = mapped_column(Date)
    time_entry: Mapped[str] = mapped_column(String(254))
    remark: Mapped[str] = mapped_column(String(254))
    date_entry: Mapped[date] = mapped_column(Date)
    created_user: Mapped[str] = mapped_column(String(255))
    created_date: Mapped[date] = mapped_column(Date)
    last_edited_user: Mapped[str] = mapped_column(String(255))
    last_edited_date: Mapped[date] = mapped_column(Date)
    animal_name_arabic: Mapped[int] = mapped_column(Integer)
    governorates: Mapped[int] = mapped_column(Integer)
    pasture: Mapped[int] = mapped_column(Integer)
    time_zone: Mapped[int] = mapped_column(Integer)
    person_entry: Mapped[int] = mapped_column(Integer)
    years: Mapped[int] = mapped_column(Integer)
    type_of_view: Mapped[int] = mapped_column(Integer)
    animal_name_english: Mapped[int] = mapped_column(Integer)
    wilaya: Mapped[int] = mapped_column(Integer)
    male: Mapped[float] = mapped_column(Float)
    female: Mapped[float] = mapped_column(Float)
    young: Mapped[float] = mapped_column(Float)
    attachment_1: Mapped[str] = mapped_column(String(255))
    attachment_2: Mapped[str] = mapped_column(String(255))
    attachment_3: Mapped[str] = mapped_column(String(255))
    attachment_4: Mapped[str] = mapped_column(String(255))
    attachment_5: Mapped[str] = mapped_column(String(255))
    create_by: Mapped[str] = mapped_column(String(50))
    change_by: Mapped[str] = mapped_column(String(50))
    create_dat: Mapped[date] = mapped_column(Date)
    change_dat: Mapped[date] = mapped_column(Date)
    deleted: Mapped[bool] = mapped_column(Boolean, default=False)
    client_id: Mapped[str] = mapped_column(String(50), nullable=True)
    gid: Mapped[str] = mapped_column(String(500), nullable=True)
    wilaya_new: Mapped[int] = mapped_column(Integer)
    years_new: Mapped[int] = mapped_column(Integer)
    

    def __repr__(self) -> str:
        return f"Wildlife(id={self.id}, user_id={self.user_id})"
