from unittest.mock import patch, Mock

import pytest
import requests_mock
from requests import Timeout

from opengraph import OpenGraph
from opengraph.opengraph import USER_AGENT, logger

DEFAULT_HEADERS = {"user-agent": USER_AGENT}
URL = "https://example.org"


class TestOpenGraph:
    def test__fetch(self, document):
        with requests_mock.Mocker() as m:
            m.head(URL, headers={'Content-Type': 'text/html; charset=utf-8'})
            m.get(URL, text=document)
            og = OpenGraph(url=URL)
        assert og.title == "Test title"

    def test__fetch__only_http_protocols(self, document):
        with requests_mock.Mocker() as m:
            m.head("http://foo.bar", headers={'Content-Type': 'text/html; charset=utf-8'})
            m.get("http://foo.bar", text=document)
            assert OpenGraph(url="http://foo.bar")._data != {}
            m.head("https://foo.bar", headers={'Content-Type': 'text/html; charset=utf-8'})
            m.get("https://foo.bar", text=document)
            assert OpenGraph(url="https://foo.bar")._data != {}
            m.get("mailto:jay@foo.bar", text=document)
            assert OpenGraph(url="mailto:jay@foo.bar")._data == {}
            m.get("ftp://foo.bar", text=document)
            assert OpenGraph(url="ftp://foo.bar")._data == {}

    def test__fetch__content_type__html_fetched(self, document):
        with requests_mock.Mocker() as m:
            m.head(URL, headers={'Content-Type': 'text/html; charset=utf-8'})
            m.get(URL, text=document)
            og = OpenGraph(url=URL)
        assert og.title == "Test title"

    def test__fetch__content_type__non_html_skipped(self, document):
        with requests_mock.Mocker() as m:
            m.head(URL, headers={'Content-Type': 'video/mp4'})
            m.get(URL, text=document)
            og = OpenGraph(url=URL)
        assert og._data == {}

    def test_contains(self, document):
        og = OpenGraph(html=document)
        assert "title" in og

    def test_get_attr(self, document):
        og = OpenGraph(html=document)
        assert og.title == "Test title"
        with pytest.raises(AttributeError):
            # noinspection PyStatementEffect
            og.attribute_does_not_exist

    @patch("opengraph.opengraph.requests.get", side_effect=Timeout)
    @patch.object(logger, "debug", autospec=True)
    def test_returns_none_on_get_exception(self, mock_logger, mock_get):
        assert OpenGraph(url=URL)._data == {}
        assert mock_logger.called

    def test_str_repr(self, document):
        og = OpenGraph(html=document)
        text_of_data = og._data.__str__()
        assert str(og) ==  text_of_data

    @patch("opengraph.opengraph.BeautifulSoup", autospec=True)
    def test_uses_right_parser(self, mock_bs, document):
        try:
            OpenGraph(html=document)
        except AttributeError:
            pass
        mock_bs.assert_called_once_with(document, "html.parser")
        mock_bs.reset_mock()
        try:
            OpenGraph(html=document, parser="spam")
        except AttributeError:
            pass
        mock_bs.assert_called_once_with(document, "spam")

    @patch("opengraph.opengraph.requests.get", return_value=Mock(text=""))
    def test_uses_timeout(self, mock_get):
        OpenGraph(url=URL)
        mock_get.assert_called_once_with(URL, headers=DEFAULT_HEADERS, timeout=10)
        mock_get.reset_mock()
        OpenGraph(url=URL, timeout=123)
        mock_get.assert_called_once_with(URL, headers=DEFAULT_HEADERS, timeout=123)
