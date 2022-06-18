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
- move template of fail2ban configs to host (based on jail param)
- reload fail2ban config

Note: this configure fail2ban to add to nftables (not iptables)
