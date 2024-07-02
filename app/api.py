# app/routers/api.py
from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from crud import create_short_url, fetch_original_url, fetch_urls
from schemas import URLRequest, URLResponse

router = APIRouter()


@router.get("/shortens", response_model=List[URLResponse])
def get_urls(db: Session = Depends(get_db)):
    urls = fetch_urls(db=db)
    return urls


@router.post("/shortens", response_model=URLResponse)
def post_urls(request: URLRequest, db: Session = Depends(get_db)):
    url = create_short_url(db=db, url=request.url, expiry=request.expiry)
    return url


@router.get("/{short_key}")
def redirect_url(short_key: str, db: Session = Depends(get_db)):
    db_url = fetch_original_url(db=db, short_key=short_key)
    if db_url:
        return RedirectResponse(db_url.url, status_code=301)
    else:
        raise HTTPException(status_code=404, detail="URL이 존재하지 않습니다.")


@router.get(
    "/stats/{short_key}",
)
def get_url_stats(short_key: str, db: Session = Depends(get_db)):
    db_url = fetch_original_url(db=db, short_key=short_key)
    return
