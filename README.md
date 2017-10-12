[![](https://travis-ci.org/jaywink/python-opengraph.svg?branch=master)](https://travis-ci.org/jaywink/python-opengraph)

# python-opengraph

Python module to parse Open Graph metadata on web pages. For more information on the Open Graph Protocol, see http://ogp.me/.

Fork of [HenrikOssipoff/python-opengraph](https://github.com/HenrikOssipoff/python-opengraph).

## Compatability

Python 3.4+

Other versions may work, but testing is only done against the above versions.

## Installation

Currently only using GitHub VCS urls in your dependency file, for example. PyPi later.

## Usage

### Using URL

    from opengraph import OpenGraph

    og = OpenGraph(url='http://someurl.com')
    og.title  # would yield the 'title' open graph element
    
### Using HTML document

    from opengraph import OpenGraph
    
    document = "<html><head><meta property="og:title" content="Test title"></head><body></body></html>"
    og = OpenGraph(html=document)
    og.title  # would yield the 'title' open graph element

## Development

Create a Python 3.4+ virtualenv and then:

    pip install -r dev-requirements.txt

## Testing

    py.test

## License

MIT

## Author

This fork by Jason Robinson (@jaywink / https://jasonrobinson.me).

Original author Henrik Ossipoff Hansen (@HenrikOssipoff).
