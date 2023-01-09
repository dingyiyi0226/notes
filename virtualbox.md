# Virtual Box

## Networking

[a good blog](https://blogs.oracle.com/scoter/post/oracle-vm-virtualbox-networking-options-and-how-to-manage-them)

-   When you want to create a vm in your host, choose NAT + Host-only network. NAT network for accessing the internet, Host-only network for accessing from your host.

-   When you want to create a vm on your lan, choose bridged network.

<img src="https://raw.githubusercontent.com/dingyiyi0226/notes/master/img/virtualbox_network.png" alt="vbox network" width="800"/>

[Reference Page](https://www.virtualbox.org/manual/ch06.html)


## Vboxmanage Usage

[Reference Page](https://www.virtualbox.org/manual/ch08.html)

### List VM

```shell
vboxmanage list vms
vboxmanage list runningvms

```

### Control VM

```shell
vboxmanage startvm <vm> [--type gui|headless]           # default: gui
vboxmanage controlvm <vm> <acpipowerbutton|poweroff>    # recommend: acpipowerbutton

```

### Import VM

```shell
vboxmanage import <vm.ova> --vsys 0 --vmname <vm> --cpus <2> --memory <4096> [--dry-run]
```

### Delete VM

```shell
vboxmanage unregistervm <vm> --delete
```

### Modify VM

```shell
vboxmanage modifyvm <vm> --nic1 bridged --bridgeadapter1 eno1  # change nic1 to bridged mode and to eno1 interface
vboxmanage modifyvm <vm> --nic1 hostonly --hostonlyadapter1 vboxnet0  # change nic1 to hostonly mode and to vboxnet0 interface
```

### VM Infos

You may need to install virtualbox extension pack from website.

```shell
vboxmanage guestproperty enumerate <vm>
vboxmanage guestproperty get <vm> <property>

```
