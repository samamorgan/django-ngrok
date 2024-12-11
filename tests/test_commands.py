from django.core.management import call_command


def test_runserver_ngrok():
    call_command("runserver_ngrok")
    assert True is False
