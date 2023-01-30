# Linux

## Case Sensitivity

- Almost everything in Linux is case sensitive. `cd` is not the same as `CD`.
- `tip`: careful of usernames when logging in.

```
cd
CD
```



## Create New Root User and Disable Root Account

- Best practise to remove the root user and create a new administrative account on new boxes. We'll use the the following commands in this section:
  - `adduser` command
  - `usermod` command
  - `whoami` command
- Begin by creating a new root user:

```bash
sudo adduser user1
sudo usermod -aG sudo user1
# login with new user1
whoami
sudo whoami
exit 
exit
```

- Now login with user1 and lock out the root account from SSH

```bash
sudo nano /etc/ssh/sshd_config
```

- Change `PermitRootLogin` to `no`
- `ctrl + O` to save
- `ctrl + X` to save
- Restart the SSH server:

```bash
sudo service ssh restart
```

# Enable Firewall using UFW

- Increase security by using the built-in firewall service `ufw` or Uncomplicated Firewall.
- Check firewall status:

```bash
sudo ufw status
```

- Set firewall rules to allow only incoming SSH traffic, and deny everything else inbound and outbound:

```bash
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw default deny outgoing
sudo ufw enable
```

- Check firewall status

```bash
sudo ufw status
```

# IPtables vs UFW

- `ufw` is used to to manage `IPtables`.
- IPtables is a program to administer the IP packet filter rules of the Linux Kernel firewall (similar to the Windows Firewall)
- Best practise to use third party firewalls but allows further security hardening.

```bash
sudo iptables --list
```

- Be aware of IPtable rules when troubleshooting.

# AntiVirus

- Many debate the use of AV on Linux but best practise to install it.
- Most customers will have AV for Linux.

```bash
# Install
sudo apt-get install clamav clamav-daemon -y
# Stop to update the service
sudo systemctl stop clamav-freshclam
# Update database
sudo freshclam
# Start service
sudo systemctl start clamav-freshclam
sudo systemctl enable clamav-freshclam
```

# Updating Software

- Best practice to keep software and packages updated:

```bash
sudo apt update
sudo apt upgrade
```

