# Changelog

## 0.1.0.dev0 (unreleased)

### Added

* Use a default user agent if none given.

### Changed

* No longer fetch other URL's than "http" and "https" protocols.

## 0.0.3 (2017-10-12)

Released to PyPi under the name `python-opengraph-jaywink`.

### Added

* `OpenGraph` now allows passing in a `parser` argument, which defaults to `html.parser`.

  A valid `parser` is anything `BeautifulSoup` supports, for example `lxml` or `html5lib`. You must have the right parser installed when calling `OpenGraph`, except the default `html.parser` which is built-in to Python.

### Fixed

* `OpenGraph` no longer "remembers" old OG tags from previous class instances.

  Data dictionary has been moved from class to instance attributes to ensure clean data is available every time the class is used.

## 0.0.2 (2015-06-14)

First release on Pypi as `python-opengraph` with basic OG tags parsing.
