from reader._vendor.feedparser.urls import _urljoin
from reader._vendor.feedparser.urls import make_safe_absolute_uri


def test_make_safe_absolute_uri():
    base = "scheme://netloc/path;params?query#fragment"
    assert make_safe_absolute_uri(base) == ""
    assert make_safe_absolute_uri(base, "scheme") == ""
