# VNC

使用 [tigervnc](https://tigervnc.org)

## Process

### xvnc
沒有連接螢幕(headless)的時候用這個

如果想接螢幕必須把這個process砍掉才能用

### x0vncserver
當有連接螢幕的時候用這個

## Install

### Ubuntu

    apt install tigervnc-standalone-server   # for xvnc
    apt install tigervnc-scraping-server     # for x0vncserver

### Centos

    dnf install tigervnc-server

## Usage

See [Documentation](https://wiki.archlinux.org/title/TigerVNC)

The usage on [Ubuntu](http://manpages.ubuntu.com/manpages/focal/en/man5/vnc.conf.5x.html)
-  Global configuration: `/etc/vnc.conf`
-  Custom configuration: `~/.vnc/vnc.conf`

1. Set the vnc password by `vncpasswd`
2. Follow the instructions below

### xvnc

Set `$localhost = "no"` in custom configuration

Start a session by `vncserver -rfbport 5903`

List all sessions by `vncserver -list`

Close this session by `vncserver -kill :3`


### x0vncserver

#### Start session in shell

Start a session by `x0vncserver -display :0 -rfbauth ~/.vnc/passwd -rfbport 5903`

#### Start session by service file

Put the service file at `~/.config/systemd/user/x0vncserver.service`

Start this service by `systemctl --user start x0vncserver`

Autostart this service at login by `systemctl --user enable x0vncserver`

##### Service file

-  `-display`: display number, normally :0
-  `-rfbauth`: password file
-  `-rfbport`: service port

```shell
[Unit]
Description=Remote desktop service (VNC)

[Service]
Type=simple
# wait for Xorg started by ${USER}
ExecStartPre=/bin/sh -c 'while ! pgrep -U "$USER" Xorg; do sleep 2; done'
ExecStart=/usr/bin/x0vncserver -display :0 -rfbauth %h/.vnc/passwd -rfbport 5903
# or login with your username & password
#ExecStart=/usr/bin/x0vncserver -PAMService=login -PlainUsers=${USER} -SecurityTypes=TLSPlain

[Install]
WantedBy=default.target

```
