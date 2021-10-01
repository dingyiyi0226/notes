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

see [Documentation](https://wiki.archlinux.org/title/TigerVNC)

