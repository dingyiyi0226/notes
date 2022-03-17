# Linux Account

## User

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


### Change login account
```shell
su -        # change to root
su - USER
```

## Group

```shell
groupadd GROUP
groupmod GROUP -n NEWGROUPNAME
groupdel GROUP
gpasswd GROUP [-a|-d] USER    # add/delete USER from GROUP

groups USER    # print the groups that USER is in
```

## Example usage
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
