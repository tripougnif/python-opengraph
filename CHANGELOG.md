# Changelog

## 0.0.3.dev (unreleased)

### Added

* `OpenGraph` now allows passing in a `parser` argument, which defaults to `html.parser`.

  A valid `parser` is anything `BeautifulSoup` supports, for example `lxml` or `html5lib`. You must have the right parser installed when calling `OpenGraph`, except the default `html.parser` which is built-in to Python.

## 0.0.2 (2015-06-14)

First release on Pypi with basic OG tags parsing.
