import testinfra


def test_fail2ban_running(host):
    """test that the fail2ban service is running"""

    assert host.service("fail2ban").is_running


def test_fail2ban_file_created(host):
    """test that the fail2ban jail.local file is created"""

    assert host.file("/etc/fail2ban/jail.local")
