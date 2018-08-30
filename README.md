# ovs-toolbox

ovs-toolbox.py is a graphical user interface for Open vSwitch (OvS).

OvS bridges managed by this GUI, do not necessarily need to be local to your host. 
(They can be located on AWS, GCP, etc.. and managed remotely by this GUI via ssh/paramiko/sudo ) 

In addition, this GUI will help you with docker and KVM ecosystems (for simple tasks like connecting containers and VMs to OvS).

OvS related settings that you can manage with this GUI:
- bridge creation
- port/interface creation ( vlan, interface types, etc..)
- port statistics
- ingress policy
- mirroring
- bonding
- RSTP, STP
- multicast
- flows (netflow,sflow,ipfix)
- queues and QOS
- OpenFlow flows
- OpenFlow groups
- various OvS databases (controller, manager, Open_vSwitch, ssl )

Docker related settings that you can manage with this GUI:
- docker files creation
- docker image creation, docker image build
- docker run, stop and rm
- docker inspect
- docker containers network parameters and automatic connection to selected OvS through one or multiple network interfaces.

KVM related things you can do with this GUI:
- virt-install settings
- KVM network parameters and automatic connection to selected OvS

iproute related things you can do with this GUI:
- interface creation (dummy, tap, tun, veth pair )
- MTU setting
- ip address setting

Plotnetcfg
- live image of network diagram generated thanks to Plotnetcfg and Graphviz

For documentation, read [ovs-toolbox wiki](https://github.com/nbonnand/ovs-toolbox/wiki)
