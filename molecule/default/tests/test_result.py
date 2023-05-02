import testinfra


def test_os_release(host):
    """test host release for good measure"""

    assert host.file("/etc/os-release").contains("Ubuntu")


def test_nsd_running(host):
    """test that the fail2ban service is running"""

    assert host.service("fail2ban").is_running


def test_nsd_zone_file_created(host):
    """test that the fail2ban jail.local file is created"""

    assert host.file("/etc/fail2ban/jail.local")
