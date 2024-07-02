import string
from datetime import datetime
from models import URL

BASE62 = string.digits + string.ascii_letters


def uuid_to_base62(uuid):
    """UUID를 62진법 문자열로 변환"""
    base62 = []
    # UUID를 정수로 변환
    uuid_int = uuid.int
    # 62진법으로 변환
    while uuid_int:
        uuid_int, remainder = divmod(uuid_int, 62)
        base62.append(BASE62[remainder])
    return "".join(reversed(base62))


def check_url_expiry(url: URL):
    if url.expiry_date and url.expiry_date <= datetime.now():
        return True
    return False
