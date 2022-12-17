# Requirements

1. Ansible installed:

```
sudo apt install python3
python3 -m ensurepip --upgrade
pip3 install ansible
```

## Required variables

Set the variables as shown in defined.

Currently available jails are:

- sshd
- nginx

# Example playbook

```
hosts:
  - foo
roles:
  - ansible-fail2ban

```

# TLDR - What will happen if I run this

- install fai2ban
- move template of fail2ban configs to host (based on jail params)
- reload fail2ban config

Note: this configures fail2ban to add to nftables (not iptables)

# Future Improvements

- Allow non authorative zones and key directives
- Improve sane defaults of variables (see defaults defined in defaults/main.yaml)
- Allow TTL to be passed in records
- Add automated KSK rollover to dnssecpls script
- Allow duplicates of dnssecpls script with different variables from ZSK rollover etc as specified in nsd_zone_attributes
- Only update serial when required, instead of when running role

# License

The GPLv3 License (GPLv3)

Copyright (c) 2022 Author

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
