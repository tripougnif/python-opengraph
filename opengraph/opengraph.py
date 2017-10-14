import re

import requests
from bs4 import BeautifulSoup

from opengraph import __version__

USER_AGENT = "python-opengraph-jaywink/%s (+https://github.com/jaywink/python-opengraph)" % __version__


class OpenGraph:
    def __init__(self, url=None, html=None, useragent=None, parser="html.parser"):
        self._data = {}
        self.useragent = useragent or USER_AGENT
        content = html or self._fetch(url)
        self._parse(content, parser=parser)

    def __contains__(self, item):
        return item in self._data

    def __getattr__(self, name):
        if name in self._data:
            return self._data[name]
        raise AttributeError(
            "Open Graph object has no attribute '{}'".format(name))

    def __repr__(self):
        return self._data.__str__()

    def __str__(self):
        return self.__repr__()

    def _fetch(self, url):
        if not re.search(r"^https?://", url):
            return
        headers = {
            "user-agent": self.useragent,
        }
        response = requests.get(url, headers=headers)
        return response.text

    def _parse(self, html, parser):
        if not html:
            return self._data
        doc = BeautifulSoup(html, parser)
        ogs = doc.html.head.findAll(property=re.compile(r"^og"))

        for og in ogs:
            if og.has_attr("content"):
                self._data[og["property"][3:]] = og["content"]
