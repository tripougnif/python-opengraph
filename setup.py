from setuptools import setup, find_packages

VERSION = (0, 0, 3)
__version__ = VERSION
__versionstr__ = '.'.join([str(v) for v in VERSION])

install_requires = ['beautifulsoup4>=4.3', 'requests>=2.7']

setup(
    name='python-opengraph',
    version=__versionstr__,
    description='Python module to parse Open Graph metadata on web pages',
    url='https://github.com/jaywink/python-opengraph',
    license='MIT',
    author='Jason Robinson',
    author_email='mail@jasonrobinson.me',
    install_requires=install_requires,
    packages=find_packages(exclude=['tests']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='opengraph')
