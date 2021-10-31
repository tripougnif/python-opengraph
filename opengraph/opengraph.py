import logging
import re

import requests
from bs4 import BeautifulSoup
from requests import RequestException

from opengraph import __version__

USER_AGENT = "python-opengraph-jaywink/%s (+https://github.com/jaywink/python-opengraph)" % __version__

logger = logging.getLogger(__name__)


class OpenGraph:
    def __init__(self, url=None, html=None, useragent=None, parser="html.parser", timeout=10):
        self._data = {}
        self.timeout = timeout
        self.headers = {
            "user-agent": useragent or USER_AGENT,
        }
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

    def _fetch_content_type(self, url):
        try:
            response = requests.head(url, headers=self.headers, timeout=self.timeout)
        except RequestException as ex:
            logger.debug("_fetch_content_type - %s when fetching url %s", ex, url)
            return ""
        else:
            return response.headers.get('Content-Type', "")

    def _fetch(self, url):
        if not re.search(r"^https?://", url):
            return
        content_type = self._fetch_content_type(url)
        if not content_type.startswith('text/html'):
            return
        try:
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
        except RequestException as ex:
            logger.debug("_fetch - %s when fetching url %s", ex, url)
            return
        else:
            return response.content

    def _parse(self, html, parser):
        if not html:
            return self._data
        doc = BeautifulSoup(html, parser)
        ogs = doc.html.head.findAll(property=re.compile(r"^og"))

        for og in ogs:
            if og.has_attr("content"):
                self._data[og["property"][3:]] = og["content"]
