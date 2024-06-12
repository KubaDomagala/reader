import datetime

from reader._vendor.feedparser.http import _build_urllib2_request
from reader._vendor.feedparser.http import print_coverage__build


def test_build_urllib2_request():
    open('_build_urllib2_request_coverage.txt', 'w').close()
    url = "https://example.com/#anger"
    request_headers = {'Cookie': 'Something', "X": "data"}
    agent = "agent"
    modified_time = datetime.datetime.now()
    modified_string = "modified_string"
    etag = "etag"
    referer = "referer"
    auth = "auth"
    accept_header = "accept_header"

    test = _build_urllib2_request(
        url=url,
        agent=None,
        accept_header=None,
        etag=None,
        modified=None,
        referrer=None,
        auth=None,
        request_headers=request_headers,
    )
    assert test.get_full_url() == url
    assert test.get_header("If-none-match") == None
    assert test.get_header("If-modified-since") == None
    assert test.get_header("Referer") == None
    assert test.get_header("Authorization") == None
    assert test.get_header("Accept") == None
    assert test.get_header("User-agent") == None
    print_coverage__build()

    test = _build_urllib2_request(
        url=url,
        agent=agent,
        accept_header=None,
        etag=None,
        modified=None,
        referrer=None,
        auth=None,
        request_headers=request_headers,
    )
    assert test.get_header("If-none-match") == None
    assert test.get_header("If-modified-since") == None
    assert test.get_header("Referer") == None
    assert test.get_header("Authorization") == None
    assert test.get_header("Accept") == None
    assert test.get_header("User-agent") == agent
    print_coverage__build()

    test = _build_urllib2_request(
        url=url,
        agent=agent,
        accept_header=None,
        etag=etag,
        modified=None,
        referrer=None,
        auth=None,
        request_headers=request_headers,
    )
    assert test.get_header("If-none-match") == etag
    assert test.get_header("If-modified-since") == None
    assert test.get_header("Referer") == None
    assert test.get_header("Authorization") == None
    assert test.get_header("Accept") == None
    print_coverage__build()

    test = _build_urllib2_request(
        url=url,
        agent=agent,
        accept_header=None,
        etag=etag,
        modified=modified_string,
        referrer=None,
        auth=None,
        request_headers=request_headers,
    )
    assert test.get_header("If-modified-since") == None
    assert test.get_header("Referer") == None
    assert test.get_header("Authorization") == None
    assert test.get_header("Accept") == None
    print_coverage__build()

    test = _build_urllib2_request(
        url=url,
        agent=agent,
        accept_header=None,
        etag=etag,
        modified=modified_time,
        referrer=None,
        auth=None,
        request_headers=request_headers,
    )
    assert test.get_header("If-modified-since") != None
    assert test.get_header("Referer") == None
    assert test.get_header("Authorization") == None
    assert test.get_header("Accept") == None
    print_coverage__build()

    test = _build_urllib2_request(
        url=url,
        agent=agent,
        accept_header=None,
        etag=etag,
        modified=modified_time,
        referrer=referer,
        auth=None,
        request_headers=request_headers,
    )
    assert test.get_header("Referer") == referer
    assert test.get_header("Authorization") == None
    assert test.get_header("Accept") == None
    print_coverage__build()

    test = _build_urllib2_request(
        url=url,
        agent=agent,
        accept_header=None,
        etag=etag,
        modified=modified_time,
        referrer=referer,
        auth=auth,
        request_headers=request_headers,
    )
    assert test.get_header("Authorization") == f"Basic {auth}"
    assert test.get_header("Accept") == None
    print_coverage__build()

    test = _build_urllib2_request(
        url=url,
        agent=agent,
        accept_header=accept_header,
        etag=etag,
        modified=modified_time,
        referrer=referer,
        auth=auth,
        request_headers=request_headers,
    )
    assert test.get_header("Accept") == accept_header
    print_coverage__build()
