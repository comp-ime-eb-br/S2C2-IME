from abc import ABC, abstractmethod
import time

from mininet.node import Controller
from mn_wifi.link import adhoc
from mn_wifi.net import Mininet_wifi
from mininet.log import info

class MininetDecoratorComponent(ABC):
    @abstractmethod
    def configure(self):
        pass

    @abstractmethod
    def getNetwork(self):
        pass
class MininetNetwork(MininetDecoratorComponent):
    def __init__(self, networkAttributes, nodes, isAdhoc):
        self.__network = None
        self.__nodes = nodes
        self.__networkAttributes = networkAttributes
        self.__isAdhoc = isAdhoc

    def getNetwork(self):
        return self.__network

    def configure(self):
        info("*** Creating network\n")

        if self.__isAdhoc:
            self.__network = Mininet_wifi(**self.__networkAttributes)
        else:
            self.__network = Mininet_wifi(controller=Controller, **self.__networkAttributes)
            self.__network.addController('c1')
        
        info("*** Creating nodes\n")
        for node in self.__nodes:
            if node["type"] == "station":
                self.__network.addStation(node["name"], **node["args"], **node["interface"]["args"])
            if node["type"] == "accesspoint":
                self.__network.addAccessPoint(node["name"], **node["args"], **node["interface"]["args"])
            if node["type"] == "host":
                self.__network.addHost(node["name"], **node["args"], **node["interface"]["args"])
            if node["type"] == "switch":
                self.__network.addSwitch(node["name"], **node["args"], **node["interface"]["args"])

        info("*** Configuring wifi nodes\n")
        self.__network.configureWifiNodes()

class MininetBaseDecorator(MininetDecoratorComponent):
    def __init__(self, component):
        self.__network = None
        self.__component = component

    def getNetwork(self):
        return self.__network

    def configure(self):
        self.__component.configure()
        self.__network = self.__component.getNetwork()

class PropagationModelDecorator(MininetBaseDecorator):
    ARGS_MAP = {
        "exponent": "exp"
    }

    def __init__(self, component, propagationModel):
        super().__init__(component)
        self.__propagationModel = propagationModel
        self.__args = {}
        self.__parseArgs()

    def __parseArgs(self):
        self.__args = {}
        for arg in self.__propagationModel["args"]:
            self.__args[self.ARGS_MAP[arg]] = self.__propagationModel["args"][arg]

    def configure(self):
        info("***Setting Propagation Model\n")
        super().configure()
        self.getNetwork().setPropagationModel(model=self.__propagationModel["model"], **self.__args)

class MobilityModelDecorator(MininetBaseDecorator):
    ARGS_MAP = {
        "seed": "seed",
        "min_velocidade": "min_v",
        "max_velocidade": "max_v",
        "min_x": "min_x",
        "max_x": "max_x",
        "min_y": "min_y",
        "max_y": "max_y",
        "min_z": "min_z",
        "max_z": "max_z",
    }

    def __init__(self, component, mobilityModel):
        super().__init__(component)
        self.__mobilityModel = mobilityModel
        
        self.__args = {}
        self.__parseArgs()

    def __parseArgs(self):
        self.__args = {}
        for arg in self.__mobilityModel["args"]:
            value = self.__mobilityModel["args"][arg]
            if arg == "seed":
                value = int(value)

            self.__args[self.ARGS_MAP[arg]] = value

    def configure(self):
        info("***Setting Mobility Model\n")
        super().configure()
        self.getNetwork().setMobilityModel(time=0, model=self.__mobilityModel["model"], **self.__args)

class NetworkStarterDecorator(MininetBaseDecorator):
    def __init__(self, component, links, isAdhoc):
        super().__init__(component)
        self.__links = links
        self.__isAdhoc = isAdhoc
    
    def configure(self):
        super().configure()
        info("*** Starting network\n")
        network = self.getNetwork()

        for link in self.__links:
            network.addLink(link["node1"], link["node2"], **link["args"])

        network.telemetry(nodes=network.stations, single=True)
        network.build()

        if self.__isAdhoc:
            for station in network.stations:
                network.addLink(station, cls=adhoc, intf=station.wintfs[0].name, ssid='adhocNet')
        else:
            network.get("c1").start()
            for ap in network.aps:
                network.get(ap.name).start([network.get("c1")])

            for s in network.switches:
                network.get(s.name).start([network.get("c1")])