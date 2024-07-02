import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from fastapi.testclient import TestClient
from main import app
from database import Base, get_db
from config import settings

TEST_DATABASE_URL = f"{settings.DRIVER}://{settings.USERNAME}:{settings.PASSWORD}@{settings.HOST}:{settings.PORT}/{settings.TEST_DATABASE}"

TestingEngine = create_engine(TEST_DATABASE_URL)

TestingEngine = create_engine(settings.SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

if not database_exists(TestingEngine.url):
    create_database(TestingEngine.url)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=TestingEngine
)


@pytest.fixture
def test_db():
    # Create the database tables
    Base.metadata.drop_all(bind=TestingEngine)
    Base.metadata.create_all(bind=TestingEngine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function")
def client(test_db):
    def override_get_db():
        try:
            yield test_db
        finally:
            test_db.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()
