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

### Proxy Server
`ssh -J user@10.10.10.10:4000 user@192.168.0.10`

```shell
Host alias
  HostName 192.168.0.10
  ProxyJump 10.10.10.10:4000
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

`ssh -L 6000:localhost:5901 user@10.10.10.10 -p 4000 -o 'LocalCommand=echo "Connect localhost:6000'`


```shell
Host alias
  HostName 10.10.10.10
  Port 4000
  LocalForward 6000 localhost:5901
  LocalCommand echo "Connect localhost:6000"
  PermitLocalCommand yes  # or set in General Rules section
  User user
```

### Remote Command

`ssh user@10.10.10.10 -p 4000 -t -o 'RemoteCommand=cd folder/ && bash -l'`

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
