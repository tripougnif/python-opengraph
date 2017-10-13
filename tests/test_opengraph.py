from unittest.mock import patch

import pytest
import requests_mock

from opengraph import OpenGraph

URL = "https://example.org"


class TestOpenGraph:
    def test__fetch(self, document):
        with requests_mock.Mocker() as m:
            m.get(URL, text=document)
            og = OpenGraph(url=URL)
        assert og.title == "Test title"

    def test__fetch__only_http_protocols(self, document):
        with requests_mock.Mocker() as m:
            m.get("http://foo.bar", text=document)
            assert OpenGraph(url="http://foo.bar") != {}
            m.get("https://foo.bar", text=document)
            assert OpenGraph(url="https://foo.bar") != {}
            m.get("mailto:jay@foo.bar", text=document)
            assert not OpenGraph(url="mailto:jay@foo.bar") == {}
            m.get("ftp://foo.bar", text=document)
            assert not OpenGraph(url="ftp://foo.bar") == {}

    def test_contains(self, document):
        og = OpenGraph(html=document)
        assert "title" in og

    def test_get_attr(self, document):
        og = OpenGraph(html=document)
        assert og.title == "Test title"
        with pytest.raises(AttributeError):
            # noinspection PyStatementEffect
            og.attribute_does_not_exist

    def test__fetch(self, document):
        with requests_mock.Mocker() as m:
            m.get(URL, text=document)
            og = OpenGraph(url=URL)
        assert og.title == "Test title"

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
