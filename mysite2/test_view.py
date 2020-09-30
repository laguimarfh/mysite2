'''
# test_views.py  test to demonstrate a 200 HTTP response status code
'''
def test_index_ok(client):
    # Make a GET request to / and store the response object
    # using the Django test client.
    response = client.get('/')
    # Assert that the status_code is 200 (OK)
    assert response.status_code == 200