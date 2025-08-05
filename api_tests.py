import requests

def test_get_status_ok():
    """Test that a GET request returns HTTP 200 OK."""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    print("GET", url, "→", response.status_code)
    assert response.status_code == 200, "Expected status 200"

def test_post_creates_resource():
    """Test that a POST request returns HTTP 201 Created."""
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "Hello API",
        "body": "Learning automation!",
        "userId": 123
    }
    response = requests.post(url, json=payload)
    print("POST", url, "→", response.status_code)
    assert response.status_code == 201, "Expected status 201"

def test_multiple_gets():
    """Test GET /posts/1–5 all return 200 and valid JSON structure."""
    for post_id in range(1, 6):
        url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
        response = requests.get(url)
        # 1) Assert status code is 200
        assert response.status_code == 200, f"GET {url} returned {response.status_code}"
        # 2) Parse JSON and assert it has expected keys
        data = response.json()
        expected_keys = {"userId", "id", "title", "body"}
        assert expected_keys.issubset(data.keys()), f"Response JSON missing keys for post {post_id}"
        print(f"✓ GET post {post_id} passed")

if __name__ == "__main__":
    print("\nRunning API tests...\n")
    test_get_status_ok()
    test_post_creates_resource()
    test_multiple_gets()
    print("\n🎉 All tests passed!")

