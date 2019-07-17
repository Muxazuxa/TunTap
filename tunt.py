from pytun import TunTapDevice, IFF_NO_PI, IFF_TUN

tun = TunTapDevice(name="tun", flags=(IFF_TUN | IFF_NO_PI))
tun.addr = '192.168.13.10'
tun.dstaddr = '192.168.13.1'
tun.netmask = '255.255.0.0'
tun.persist(True)
tun.mtu = 1500
buf = tun.read(tun.mtu)
tun.write(buf)
