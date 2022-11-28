# Linux

## Account

### User

```shell
useradd USER -m -s /bin/bash -G sudo 
passwd USER                              # interactively
echo "USER:PASSWORD" | sudo chpasswd     # in shell script

usermod USER -aG sudo           
userdel -r USER    # -r for remove all directories related to USER
```

```shell
who        # show all login users
whoami     # show my username
```


#### Change login account
```shell
su -        # change to root
su - USER
```

### Group

```shell
groupadd GROUP
groupmod GROUP -n NEWGROUPNAME
groupdel GROUP
gpasswd GROUP [-a|-d] USER    # add/delete USER from GROUP

groups USER    # print the groups that USER is in
```

### Example usage
1.  add user into a group
    ```shell
    usermod USER -aG GROUP
    gpasswd GROUP -a USER
    ```
2.  remove user from a group
    ```shell
    gpasswd GROUP -d USER
    ```
3.  list USER's groups
    ```shell
    groups USER
    ```
4.  list all group members in GROUP
    ```shell
    cat /etc/group | grep GROUP    # simple usage
    getent group GROUP         # a command that get entries from system
    ```

## Networking

### Fixed IP

1.  For Ubuntu desktop (using network manager), modify `/etc/netplan/<something>.yaml`

    ```yaml
    # Let NetworkManager manage all devices on this system
    network:
      version: 2
      renderer: NetworkManager
      ethernets:
        enp6s0:  # network card name. acquire the name by `ip a`
          dhcp4: no
          addresses: [192.168.0.5/24]  # ip, mask
          gateway4: 192.168.0.1        # gateway ip
          nameservers:   # dns server (optional)
            addresses: [1.1.1.1, 8.8.8.8]
    ```
2.  Apply the netplan file

    ```
    sudo netplan try
    sudo netplan apply
    ```

