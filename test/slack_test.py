from utils.slack import send_message


def test_slack():
    result = send_message("#data-monitoring", "Test message")
    assert result is True