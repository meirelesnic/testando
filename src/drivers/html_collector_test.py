from .html_collector import HtmlCollector
from .mocks.http_requester_mock import mock_request_from_page

def test_collect_essencial_information():
    http_request_response = mock_request_from_page()
    html_collector_instance = HtmlCollector()
    essencial_information = html_collector_instance.collect_essencial_information(http_request_response["html"])

    assert isinstance(essencial_information, list)
    assert isinstance(essencial_information[0], dict)
    assert 'name' in essencial_information[0]
    assert 'link' in essencial_information[0]
