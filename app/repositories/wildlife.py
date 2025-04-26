from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.wildlife import Wildlife
from app.schemas.wildlife import WildlifeCreate, WildlifeUpdate
from datetime import date
from app.dependencies import get_current_user

class WildlifeRepository:
    def get(self, db: Session, id: int) -> Optional[Wildlife]:
        return db.query(Wildlife).filter(Wildlife.id == id).first()

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Wildlife]:
        return db.query(Wildlife).offset(skip).limit(limit).all()
        
    def create(self, db: Session, *, obj_in: WildlifeCreate, created_by: str = None) -> Wildlife:
        db_obj = Wildlife(
            department=obj_in.department,
            conservation_name_english=obj_in.conservation_name_english,
            conservation_area=obj_in.conservation_area,
            conservation_status=obj_in.conservation_status,
            count=obj_in.count,
            location=obj_in.location,
            united=obj_in.united,
            site=obj_in.site,
            mountain=obj_in.mountain,
            wadi=obj_in.wadi,
            ranger=obj_in.ranger,
            contact_person=obj_in.contact_person,
            telephone_number=obj_in.telephone_number,
            east=obj_in.east,
            north=obj_in.north,
            date_entry=obj_in.date_entry,
            time_entry=obj_in.time_entry,
            remark=obj_in.remark,
            animal_name_arabic=obj_in.animal_name_arabic,
            governorates=obj_in.governorates,
            pasture=obj_in.pasture,
            time_zone=obj_in.time_zone,
            person_entry=obj_in.person_entry,
            years=obj_in.years,
            type_of_view=obj_in.type_of_view,
            animal_name_english=obj_in.animal_name_english,
            wilaya=obj_in.wilaya,
            male=obj_in.male,
            female=obj_in.female,
            young=obj_in.young,
            attachment_1=obj_in.attachment_1,
            attachment_2=obj_in.attachment_2,
            attachment_3=obj_in.attachment_3,
            attachment_4=obj_in.attachment_4,
            attachment_5=obj_in.attachment_5,
            wilaya_new=obj_in.wilaya_new,
            years_new=obj_in.years_new,
            created_user=created_by,
            created_date=date.today(),
            create_by=created_by,
            create_dat=date.today(),
            last_edited_user=created_by,
            last_edited_date=date.today(),
            change_by=created_by,
            change_dat=date.today(),
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Wildlife, obj_in: WildlifeUpdate, updated_by: str = None
    ) -> Wildlife:
        obj_data = obj_in.dict(exclude_unset=True)
        
        # Update the audit fields
        obj_data["last_edited_user"] = updated_by
        obj_data["last_edited_date"] = date.today()
        obj_data["change_by"] = updated_by
        obj_data["change_dat"] = date.today()
        
        for field, value in obj_data.items():
            setattr(db_obj, field, value)
            
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, id: int) -> Wildlife:
        obj = db.query(Wildlife).get(id)
        db.delete(obj)
        db.commit()
        return obj


wildlife_repository = WildlifeRepository() 