![Molecule test](https://github.com/pimvh/fail2ban/actions/workflow/test.yaml/badge.svg)
# Requirements

1. Ansible installed:

```
sudo apt install python3
python3 -m ensurepip --upgrade
pip3 install ansible
```

## Required variables

Set the variables as shown in defaults.

Currently available fail2ban_jails are:

- sshd
- nginx
- postfix

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
