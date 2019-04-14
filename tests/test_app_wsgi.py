import os


def dummy_plugin(reader):
    reader._dummy_was_here = True


def test_app_wsgi(monkeypatch, db_path):
    # This assumes no-one else imports reader.app.wsgi.app.
    # Also, further imports will yield the same app from this test.
    monkeypatch.setitem(os.environ, 'READER_DB', db_path)
    monkeypatch.setitem(os.environ, 'READER_PLUGIN', 'test_app_wsgi:dummy_plugin')

    from reader.app.wsgi import app
    from reader.app import get_reader

    with app.app_context():
        assert get_reader()._dummy_was_here

