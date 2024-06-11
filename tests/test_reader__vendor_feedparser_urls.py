from reader._vendor.feedparser.urls import branch_coverage
from reader._vendor.feedparser.urls import make_safe_absolute_uri
from reader._vendor.feedparser.urls import print_coverage_url


def test_make_safe_absolute_uri():
    base = "scheme://netloc/path;params?query#fragment"
    assert make_safe_absolute_uri(base) == ""
    assert make_safe_absolute_uri(base, "scheme") == ""

    print_coverage_url()


test_make_safe_absolute_uri()
