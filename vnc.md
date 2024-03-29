# VNC

This is a tutorial of  [tigervnc](https://tigervnc.org)

## Process

You cant't use xvnc and x0vncserver simultaneously.

### xvnc
Used in headless mode (沒有連接螢幕)

If you need to connect to the monitor, you must kill this process.

### x0vncserver
Control your physical monitor directly.


## Install

### Ubuntu

    apt install tigervnc-standalone-server   # for xvnc
    apt install tigervnc-scraping-server     # for x0vncserver

### Centos

    dnf install tigervnc-server

## Usage

1. Set the vnc password by `vncpasswd`
2. Follow the instructions below

### xvnc

Set `$localhost = "no"` in [custom configuration](#configuration)

Start a session by `vncserver -rfbport 5903`

List all sessions by `vncserver -list`

Close this session by `vncserver -kill :3`


### x0vncserver

You can start the session either in shell or by a service file

#### Start session in shell

Start a session by `x0vncserver -display :0 -rfbauth ~/.vnc/passwd -rfbport 5903`

#### Start session by service file

Create the service file by `systemctl edit --user --force --full x0vncserver.service`  
or simply create the file at `~/.config/systemd/user/x0vncserver.service`

Start this service by `systemctl --user start x0vncserver`

Autostart this service at login by `systemctl --user enable x0vncserver`

#### Service file

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

## Configuration

-  Global configuration: `/etc/vnc.conf`
-  Custom configuration: `~/.vnc/vnc.conf`

## Documentation

- [TigerVNC](https://wiki.archlinux.org/title/TigerVNC)
- [Ubuntu](http://manpages.ubuntu.com/manpages/focal/en/man5/vnc.conf.5x.html)

## Issues

### Authentication is required to create a color profile

Add this file `/etc/polkit-1/localauthority.conf.d/02-allow-colord.conf` and set owner root:root, mod 644

```js
polkit.addRule(function(action, subject) {
  if ((action.id == "org.freedesktop.color-manager.create-device"  ||
       action.id == "org.freedesktop.color-manager.create-profile" ||
       action.id == "org.freedesktop.color-manager.delete-device"  ||
       action.id == "org.freedesktop.color-manager.delete-profile" ||
       action.id == "org.freedesktop.color-manager.modify-device"  ||
       action.id == "org.freedesktop.color-manager.modify-profile"
      )
     )
  {
    return polkit.Result.YES;
  }
});
```

[Reference](https://askubuntu.com/questions/1033390/ubuntu-18-04-tigervnc-authentication-is-required-to-create-a-color-profile)
