# SSH

## SSH Commands

- `ssh-copy-id user@hostname`  
  Login without password

- `ssh-keygen -R hostname`  
  Remove entries in `~/.ssh/known_hosts`


## SSH Config

Connect via `ssh alias` by setting the alias in `~/.ssh/config`

### Basic

`ssh user@10.10.10.10 -p 4000`

```shell
Host alias
  HostName 10.10.10.10
  Port 4000
  User user
```

### Forward Port

`ssh -L 6000:localhost:5901 user@10.10.10.10 -p 4000`

```shell
Host alias
  HostName 10.10.10.10
  Port 4000
  LocalForward 6000 localhost:5901
  User user
```

### Local Command

Execute command on local machine

```shell
Host alias
  HostName 10.10.10.10
  Port 4000
  LocalForward 6000 localhost:5901
  LocalCommand echo "Connect VNC @ \033[0;33mvnc://localhost:6000\033[0m"
  PermitLocalCommand yes  # or set in General Rules section
  User user
```

### Remote Command

Execute command on remote machine

```shell
Host alias
  HostName 10.10.10.10
  Port 4000
  RemoteCommand cd folder/ && bash -l
  RequestTTY force
  User user
```

### General Rules

```shell
Host *
  AddKeysToAgent yes     # MacOS only
  UseKeychain yes        # MacOS only
  ServerAliveInterval 60  # For not disconnecting
  ServerAliveCountMax 10  # For not disconnecting
  PermitLocalCommand yes
```
