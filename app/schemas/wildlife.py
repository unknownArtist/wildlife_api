from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from decimal import Decimal

class WildlifeBase(BaseModel):
    department: str
    conservation_name_english: str
    conservation_area: str
    conservation_status: str
    count: float
    location: str
    united: str
    site: str
    mountain: str
    wadi: str
    ranger: str
    contact_person: str
    telephone_number: float
    east: float
    north: float
    date_entry: date
    time_entry: str
    remark: str
    animal_name_arabic: int
    governorates: int
    pasture: int
    time_zone: int
    person_entry: int
    years: int
    type_of_view: int
    animal_name_english: int
    wilaya: int
    male: float
    female: float
    young: float
    attachment_1: Optional[str] = None
    attachment_2: Optional[str] = None
    attachment_3: Optional[str] = None
    attachment_4: Optional[str] = None
    attachment_5: Optional[str] = None
    wilaya_new: Optional[int] = None
    years_new: Optional[int] = None

class WildlifeCreate(WildlifeBase):
    pass

class WildlifeUpdate(BaseModel):
    department: Optional[str] = None
    conservation_name_english: Optional[str] = None
    conservation_area: Optional[str] = None
    conservation_status: Optional[str] = None
    count: Optional[float] = None
    location: Optional[str] = None
    united: Optional[str] = None
    site: Optional[str] = None
    mountain: Optional[str] = None
    wadi: Optional[str] = None
    ranger: Optional[str] = None
    contact_person: Optional[str] = None
    telephone_number: Optional[float] = None
    east: Optional[float] = None
    north: Optional[float] = None
    date_entry: Optional[date] = None
    time_entry: Optional[str] = None
    remark: Optional[str] = None
    animal_name_arabic: Optional[int] = None
    governorates: Optional[int] = None
    pasture: Optional[int] = None
    time_zone: Optional[int] = None
    person_entry: Optional[int] = None
    years: Optional[int] = None
    type_of_view: Optional[int] = None
    animal_name_english: Optional[int] = None
    wilaya: Optional[int] = None
    male: Optional[float] = None
    female: Optional[float] = None
    young: Optional[float] = None
    attachment_1: Optional[str] = None
    attachment_2: Optional[str] = None
    attachment_3: Optional[str] = None
    attachment_4: Optional[str] = None
    attachment_5: Optional[str] = None
    wilaya_new: Optional[int] = None
    years_new: Optional[int] = None

class WildlifeInDBBase(WildlifeBase):
    id: int
    created_user: Optional[str] = None
    created_date: Optional[date] = None
    last_edited_user: Optional[str] = None
    last_edited_date: Optional[date] = None
    create_by: Optional[str] = None
    change_by: Optional[str] = None
    create_dat: Optional[date] = None
    change_dat: Optional[date] = None
    deleted: Optional[bool] = None
    client_id: Optional[str] = None
    gid: Optional[str] = None

    class Config:
        orm_mode = True
        from_attributes = True

class Wildlife(WildlifeInDBBase):
    pass

class WildlifeInDB(WildlifeInDBBase):
    pass 