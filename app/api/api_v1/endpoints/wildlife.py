from typing import Any, List, Dict
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from app.dependencies import get_db, get_current_user
from app.repositories.wildlife import wildlife_repository
from app.schemas.wildlife import Wildlife, WildlifeCreate, WildlifeUpdate
from app.models.wildlife import Wildlife as WildlifeModel

wildlife = APIRouter()


@wildlife.get("/", response_model=List[Wildlife])
def read_wildlife(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: Any = Depends(get_current_user),
) -> Any:
    """
    Retrieve wildlife records.
    """
    wildlife_records = wildlife_repository.get_multi(db, skip=skip, limit=limit)
    return wildlife_records


@wildlife.post("/", response_model=Wildlife)
def create_wildlife(
    *,
    db: Session = Depends(get_db),
    wildlife_in: WildlifeCreate,
    current_user: Any = Depends(get_current_user),
) -> Any:
    """
    Create new wildlife record.
    """
    wildlife = wildlife_repository.create(db, obj_in=wildlife_in, created_by=current_user.username)
    return wildlife


@wildlife.get("/{id}", response_model=Wildlife)
def read_wildlife_by_id(
    *,
    db: Session = Depends(get_db),
    id: int,
    current_user: Any = Depends(get_current_user),
) -> Any:
    """
    Get a specific wildlife record by id.
    """
    wildlife = wildlife_repository.get(db, id=id)
    if not wildlife:
        raise HTTPException(status_code=404, detail="Wildlife record not found")
    return wildlife


@wildlife.put("/{id}", response_model=Wildlife)
def update_wildlife(
    *,
    db: Session = Depends(get_db),
    id: int,
    wildlife_in: WildlifeUpdate,
    current_user: Any = Depends(get_current_user),
) -> Any:
    """
    Update a wildlife record.
    """
    wildlife = wildlife_repository.get(db, id=id)
    if not wildlife:
        raise HTTPException(status_code=404, detail="Wildlife record not found")
    
    wildlife = wildlife_repository.update(
        db, db_obj=wildlife, obj_in=wildlife_in, updated_by=current_user.username
    )
    return wildlife


@wildlife.delete("/{id}", response_model=Wildlife)
def delete_wildlife(
    *,
    db: Session = Depends(get_db),
    id: int,
    current_user: Any = Depends(get_current_user),
) -> Any:
    """
    Delete a wildlife record.
    """
    wildlife = wildlife_repository.get(db, id=id)
    if not wildlife:
        raise HTTPException(status_code=404, detail="Wildlife record not found")
    
    wildlife = wildlife_repository.remove(db, id=id)
    return wildlife


@wildlife.get("/geojson/all", response_class=JSONResponse)
def wildlife_geojson(
    *,
    db: Session = Depends(get_db),
    current_user: Any = Depends(get_current_user),
) -> Dict:
    """
    Get wildlife data in GeoJSON format.
    """
    wildlife_records = wildlife_repository.get_multi(db)
    
    features = []
    for record in wildlife_records:
        # Create GeoJSON point geometry
        geometry = {
            "type": "Point",
            "coordinates": [record.east or 0, record.north or 0]
        }
        
        # Create properties dict from all attributes except coordinates
        properties = {}
        for column in WildlifeModel.__table__.columns:
            col_name = column.name
            if col_name not in ["east", "north"]:
                properties[col_name] = getattr(record, col_name)
        
        # Add feature to feature collection
        features.append({
            "type": "Feature",
            "geometry": geometry,
            "properties": properties
        })
    
    # Return GeoJSON feature collection
    return {
        "type": "FeatureCollection",
        "features": features
    }




