#!/usr/bin/env python

"""
This example shows on how to enable the adhoc mode
Alternatively, you can use the manet routing protocol of your choice
"""

import sys

from mininet.log import setLogLevel, info
from mn_wifi.link import wmediumd, adhoc
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi
from mn_wifi.wmediumdConnector import interference


def topology(args):
    "Create a network."
    net = Mininet_wifi(link=wmediumd, wmediumd_mode=interference)

    info("*** Creating nodes\n")
    kwargs = {}
    if '-a' in args:
        kwargs['range'] = 320

    #network 1
    sta1 = net.addStation('sta1', mac='00:00:00:00:00:01',
                          min_x=200, max_x=300, min_y=300, max_y=400, min_v=5, max_v=10, range=320, wlans=2)

    #sta5 = net.addStation('sta5', mac='00:00:00:00:00:05',
                          #min_x=300, max_x=400, min_y=300, max_y=400, min_v=5, max_v=10, range=320, wlans=2)

    sta11 = net.addStation('sta11', mac='00:00:00:00:00:11',
                           min_x=450, max_x=500, min_y=350, max_y=400, min_v=5, max_v=10, range=320, wlans=2)


    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("\n*** Addressing...\n")
    sta1.setIP('10.0.0.1/8', intf=sta1.wintfs[1].name)
    sta1.setIP('10.0.0.2/8', intf=sta1.wintfs[0].name)

    sta11.setIP('10.0.0.21/8', intf=sta11.wintfs[1].name)
    sta11.setIP('10.0.0.22/8', intf=sta11.wintfs[0].name)


    net.setPropagationModel(model="logDistance", exp=4)

    info("*** Creating links\n")
    # MANET routing protocols supported by proto:
    # babel, batman_adv, batmand and olsr
    # WARNING: we may need to stop Network Manager if you want
    # to work with babel
    protocols = ['babel', 'batman_adv', 'batmand', 'olsrd', 'olsrd2']
    kwargs = {}
    for proto in args:
        if proto in protocols:
            kwargs['proto'] = proto

    net.addLink(sta1, cls=adhoc, intf='sta1-wlan1',
                ssid='adhocNet', mode='g', channel=5, ht_cap='HT40+', **kwargs)
    net.addLink(sta1, cls=adhoc, intf='sta1-wlan0',
                ssid='adhocNet', mode='g', channel=5, ht_cap='HT40+', **kwargs)


    net.addLink(sta11, cls=adhoc, intf='sta11-wlan1',
                ssid='adhocNet', mode='g', channel=5, ht_cap='HT40+', **kwargs)
    net.addLink(sta11, cls=adhoc, intf='sta11-wlan0',
                ssid='adhocNet', mode='g', channel=5, ht_cap='HT40+', **kwargs)


    info("*** setTxPower\n")
    sta1.setTxPower(16, intf=sta1.wintfs[1].name)
    sta1.setTxPower(16, intf=sta1.wintfs[0].name)

    sta11.setTxPower(16, intf=sta11.wintfs[1].name)
    sta11.setTxPower(16, intf=sta11.wintfs[0].name)

    source = sta1
    destination = sta11

    if '-p' not in args:
        net.plotGraph(max_x=800, max_y=800)

    net.setMobilityModel(time=0, model='RandomDirection',
                         max_x=800, max_y=800, seed=20)

    info("*** Starting network\n")
    net.build()

    # coordenadas dos nós
    source_string = str(source.position)
    source_string = source_string.replace('(', '')
    source_string = source_string.replace(')', '')
    source_string = source_string.split(',')

    source_x = float(source_string[0])
    source_y = float(source_string[1])

    destination_string = str(destination.position)
    destination_string = destination_string.replace('(', '')
    destination_string = destination_string.replace(')', '')
    destination_string = destination_string.split(',')

    source_x = float(source_string[0])
    source_y = float(source_string[1])

    destination_x = float(destination_string[0])
    destination_y = float(destination_string[1])

    # vértices do retângulo
    vertices_x = [300, 300, 400, 400]
    vertices_y = [400, 300, 400, 300]

    # Equação reduzida da reta
    # y = ax + b

    # 1 - encontrar o coeficiente angular
    # a = y2 - y1/x2 - x1

    a = (destination_y - source_y) / (destination_x - source_x)

    # 2 - encontrar o coeficiente linear

    b = source_y - (a * source_x)

    # calcula f(x) = -(a*x) + y-(b)

    signal_first = ''
    result = ''
    signal = ''
    error = False
    for i in range(0, 4):
        fx = -(a * vertices_x[i]) + vertices_y[i] - (b)
        if i == 0:
            value = fx
            if value > 0:
                signal_first = 'positive'
            elif value < 0:
                signal_first = 'negative'
        if fx > 0:
            signal = 'positive'
        elif fx < 0:
            signal = 'negative'

        if signal != signal_first:
            error = True
            result = '\nstations have no line of sight'

    if error == False:
        print(source.cmd('ping', '-c 1 -q', '-I ' + source.wintfs[0].ip, destination.wintfs[0].ip))

    print(result)

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology(sys.argv)
