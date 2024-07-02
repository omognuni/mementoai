import pytest
from datetime import datetime, timedelta
from crud import create_short_url, fetch_original_url

SHORT_URL_LENGTH = 8


def test_create_short_url(test_db):
    url = "https://example.com"
    result = create_short_url(test_db, url)
    assert result.url == url
    assert len(result.short_key) == SHORT_URL_LENGTH


def test_fetch_original_url(test_db):
    url = "https://example.com"
    short_url = create_short_url(test_db, url)
    result = fetch_original_url(test_db, short_url.short_key)
    assert result.url == url


def test_expired_url(test_db):
    url = "https://example-expired.com"
    expiry_date = datetime.now() - timedelta(days=1)
    short_url = create_short_url(test_db, url, expiry_date=expiry_date)
    result = fetch_original_url(test_db, short_url.short_key)
    assert result is None


def test_stats_increment(test_db):
    url = "https://example-stats.com"
    short_url = create_short_url(test_db, url)
    assert short_url.stats == 0
    fetch_original_url(test_db, short_url.short_key)
    updated_url = fetch_original_url(test_db, short_url.short_key)
    assert updated_url.stats == 2
