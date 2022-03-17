# Linux Account

## User

```shell
useradd user -m -s /bin/bash -G sudo 
passwd user                              # interactively
echo "user:password" | sudo chpasswd     # in shell script

usermod user -aG sudo           
userdel -r user    # -r for remove all directory related to user
```

```shell
who        # show all login users
whoami     # show my username
```


### Change login account
```shell
su -        # change to root
su - user
```

## Group

```shell
groupadd group
groupmod group -n newgroupname
groupdel group
gpasswd group [-a|-d] user    # add/delete user from a group

groups user    # print the groups a user is in
```

## Example usage
1.  add user into a group
    ```shell
    usermod user -aG group
    gpasswd -a user
    ```
2.  remove user from a group
    ```shell
    gpasswd -d user
    ```
3.  list my groups
    ```shell
    groups user
    ```
4.  list all group members
    ```shell
    cat /etc/group | grep groupname    # simple usage
    getent group groupname         # a command that get entries from system
    ```
