import pytest


@pytest.fixture
def document():
    return """
        <html>
            <head>
                <meta property="og:title" content="Test title">
            </head>
            <body></body>
        </html>
    """
