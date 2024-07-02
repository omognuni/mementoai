from sqlalchemy.orm import Session
from datetime import datetime, timezone
from models import URL
from utils import uuid_to_base62, check_url_expiry


def create_short_url(db: Session, url: str, expiry: datetime = None):
    # URL 존재여부 확인
    existing_url = db.query(URL).filter(URL.url == url).first()
    if existing_url:
        return existing_url

    new_url = URL(url=url, expiry_date=expiry, created_at=datetime.now())
    db.add(new_url)
    db.flush()

    # UUID를 Base62로 인코딩하여 단축 키 생성
    short_key = uuid_to_base62(new_url.id)[:8]
    new_url.short_key = short_key
    db.commit()
    db.refresh(new_url)

    return new_url


def fetch_original_url(db: Session, short_key: str):
    url = db.query(URL).filter(URL.short_key == short_key).first()
    is_expired = check_url_expiry(url)
    if is_expired:
        db.delete(url)
        return

    if url:
        url.stats += 1
        db.commit()
    return url


def fetch_urls(db: Session):
    return db.query(URL).all()


def fetch_url_detail(db: Session, short_key: str):
    return db.query(URL).filter(URL.short_key == short_key).first()
