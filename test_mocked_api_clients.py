"""
Can I test mocked API clients with Hypothesis?
"""
from unittest.mock import Mock, patch
import requests
from hypothesis import given, strategies as st
from hypothesis.provisional import urls, domains

class APIClient:
    def __init__(self, url):
        self.url = url

    def get(self, path):
        return requests.get(f"{self.url}/{path}")

""" a typical test case involving a mocked API client
- if we submit a well formed and valid request ( usualy based on some assumptions about the wrapped API, docs, OpenAPI docs, reverse engineering)
- hardcoding the expected response (again based on some assumptions)
- checks if given client methods were called with right params
- Can you use hypothesis strategies to generate well formed urls?
"""


@given(path=domains(), base_url=st.text())
def test_get_calls_requests_get(path: str, base_url:str):
    client = APIClient(base_url)
    with patch("requests.get") as mock_get:
        client.get(path)
        mock_get.assert_called_with(f"{base_url}/{path}")

"""
- Can you use hypothesis strategies to generate the expected response?
"""