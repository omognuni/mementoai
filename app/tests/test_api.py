def test_create_short_url(client):
    response = client.post("/shortens", json={"url": "https://example.com"})
    assert response.status_code == 200
    assert "short_key" in response.json()


def test_redirect_url(client):
    post_response = client.post("/shortens", json={"url": "https://example.com"})
    short_key = post_response.json()["short_key"]
    response = client.get(f"/{short_key}", follow_redirects=False)
    assert response.status_code == 301


def test_get_urls(client):
    response = client.get("/shortens")
    assert response.status_code == 200
    # assert isinstance(response.json(), list)


def test_get_url_stats(client):
    post_response = client.post("/shortens", json={"url": "https://example.com"})
    short_key = post_response.json()["short_key"]
    response = client.get(f"/stats/{short_key}")
    assert response.status_code == 200