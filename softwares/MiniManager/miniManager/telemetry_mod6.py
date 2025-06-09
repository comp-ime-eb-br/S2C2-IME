#!/usr/bin/python

'This uses telemetry() to enable a graph with live statistics'
import socket
import threading
import time

from mininet.log import info, setLogLevel
from mininet.node import Controller
from mn_wifi.cli import CLI
from mn_wifi.link import wmediumd
from mn_wifi.net import Mininet_wifi
from mn_wifi.wmediumdConnector import interference


def topology():
    "Create a network."
    net = Mininet_wifi(controller=Controller, link=wmediumd,
                       wmediumd_mode=interference,
                       noise_th=-91, fading_cof=3)

    info("*** Creating nodes\n")
    ap1 = net.addAccessPoint('ap1', ssid='new-ssid', mode='n', channel='6',
                             position='15,30,0')
    net.addStation('sta1', mac='00:00:00:00:00:02', ip='10.0.0.1/8',
                   min_x=10, max_x=30, min_y=50, max_y=70, min_v=5, max_v=10)
    net.addStation('sta2', mac='00:00:00:00:00:03', ip='10.0.0.2/8',
                   min_x=0, max_x=60, min_y=25, max_y=80, min_v=2, max_v=10)
    net.addStation('sta3', mac='00:00:00:00:00:04', ip='10.0.0.3/8',
                   min_x=60, max_x=70, min_y=10, max_y=20, min_v=1, max_v=5)
    c1 = net.addController('c1')

    info("*** Configuring Propagation Model\n")
    net.setPropagationModel(model="logDistance", exp=4)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    nodes = net.stations

    # net.plotGraph(max_x=100, max_y=100)
    net.setMobilityModel(time=0, model='RandomDirection',
                         max_x=90, max_y=90, seed=20)
    # net.stopMobility(time=120)

    # net.telemetry(nodes=nodes, single=True)
    # net.telemetry(nodes=nodes, single=True, data_type='position')
    #

    info("*** Starting network\n")
    net.build()
    c1.start()
    ap1.start([c1])

    # for i in range(1, 119):
    # net.iperf([nodes[0],nodes[1]])
    # print(time.ctime(time.time()), nodes[0].wintfs[0].rssi,nodes[0].wintfs[0].channel)
    #    monNode(nodes)
    #    time.sleep(1)
    #
    # myping(net, nodes[0], nodes[1], 3)
    #
    t1 = threading.Thread(target=nwMon, args=(nodes[0], 1, "/home", ['rssi']))
    t1.daemon = True
    t1.start()
    t2 = threading.Thread(target=nwMon, args=(nodes[1], 1, "/home", ['rssi']))
    t2.daemon = True
    t2.start()
    t3 = threading.Thread(target=myPing, args=(nodes[0], nodes[1]))
    t3.daemon = True
    t3.start()
    # t4 = threading.Thread(target=myPing, args=(nodes[2], nodes[1]))
    # t4.daemon = True
    # t4.start()
    #t5 = threading.Thread(target=setIperfServer, args=(nodes[1]))
    # t5.daemon = True
    # t5.start()
    # nwMon(nodes[0], 1, "/home", ['rssi'])
    # net.socketServer(ip='127.0.0.1', port=12345)
    #myIperf(nodes[0], nodes[1])
    #setIperfServer(net, [nodes[0], nodes[1]])
    #
    info("*** Running CLI - my message\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()


def myPing(src, dst, period=5):
    path = '/home/wifi/vboxshare/miniManager/'
    filename = path + 'nwPingTest_' + src.wintfs[0].name+'.txt'
    #
    f = open(filename, 'w')
    f.close()
    #
    time.sleep(5)
    perfDict = {}
    while True:
        pingResult = src.cmd('ping', '-c 10 -q', '-I ' +
                             src.wintfs[0].ip, dst.wintfs[0].ip)
        # print(pingResult.split('\r\n')[3:5])
        f = open(filename, 'a')
        perfDict.clear()
        perfDict.update({'timestamp': time.ctime(time.time())})
        perfDict.update({'source': src.wintfs[0].name})
        perfDict.update({'destination': dst.wintfs[0].name})
        perfDict.update({'pingResult': pingResult.split('\r\n')[3]})
        perfDict.update({'rttResult': pingResult.split('\r\n')[4]})
        #
        f.write(str(perfDict.items())+'\n')
        f.close()
        time.sleep(period)


def setIperfServer(nw, lstSrv):
    iperfResult = nw.iperf(lstSrv[0], lstSrv[1])
    print(iperfResult)


def myIperf(src, dst, period=5):
    path = '/home/wifi/vboxshare/miniManager/'
    filename = path + 'nwIperfTest_' + src.wintfs[0].name+'.txt'
    #
    # f = open(filename, 'w')
    # f.close()
    #
    time.sleep(5)
    perfDict = {}
    dst.cmd('iperf -s -D')
    while True:
        #
        iperfResult = src.cmd('iperf -d -c ' + dst.wintfs[0].ip)

        print(iperfResult)
        time.sleep(period)


def monNode(nwnode):
    attrList = ['name', 'rssi', 'channel', 'band',
                'ssid', 'txpower', 'associatedTo', 'ip', 'mode']
    #
    for eachNode in nwnode:
        measList = []
        measList.append(time.ctime(time.time()))
        measList.append(eachNode.position)
        for eachAttr in attrList:
            var = getattr(eachNode.wintfs[0], eachAttr)
            measList.append(var)
        print(measList)


def nwMon(nwnode, period, path, list=None):
    path = '/home/wifi/vboxshare/miniManager/'
    filename = path + 'nwmon_' + nwnode.wintfs[0].name+'.txt'
    #
    f = open(filename, 'w')
    f.close()
    #
    measDict = {}
    while True:
        f = open(filename, 'a')
        measDict.clear()
        measDict.update({'node': nwnode.wintfs[0].name})
        measDict.update({'timestamp': time.ctime(time.time())})
        measDict.update({'position': nwnode.position})
        if list == None:
            measDict.update({'nwmeas': nwnode.wintfs[0].__dict__})
        else:
            for eachAttr in list:
                measDict.update(
                    {eachAttr: getattr(nwnode.wintfs[0], eachAttr)})
        # print(measDict.items())
        f.write(str(measDict.items())+'\n')
        f.close()
        time.sleep(period)


if __name__ == '__main__':
    setLogLevel('info')
    topology()
