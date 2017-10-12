import pytest
import requests_mock

from opengraph import OpenGraph

URL = "https://example.org"


class TestOpenGraph:
    def test_loading_from_url(self, document):
        with requests_mock.Mocker() as m:
            m.get(URL, text=document)
            og = OpenGraph(url=URL)
        assert og.title == 'Test title'

    def test_get_attr(self, document):
        og = OpenGraph(html=document)
        assert og.title == 'Test title'
        with pytest.raises(AttributeError):
            # noinspection PyStatementEffect
            og.attribute_does_not_exist

    def test_contains(self, document):
        og = OpenGraph(html=document)
        assert 'title' in og

    def test_str_repr(self, document):
        og = OpenGraph(html=document)
        text_of_data = og.__data__.__str__()
        assert str(og) ==  text_of_data
