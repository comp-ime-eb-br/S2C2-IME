import random
from abc import ABC, abstractmethod
import time
import math

import constants
import threading
import json

import os

class IMeasurer(ABC):
    @abstractmethod
    def run(self):
        pass

class PositionMeasurer(IMeasurer):
    def __init__(self, start, nodes):
        self.__start = start
        self.__nodes = nodes

    def run(self):
        while True:
            time.sleep(constants.MininetConstants.DELAY)
            currentTime = math.floor(time.time() - self.__start)

            positions = {}
            for key in self.__nodes:
                for node in self.__nodes[key]:
                    name = getattr(node.wintfs[0],"name")
                    positions[name] = {"type": key, "position": list(node.position)}

            print({
                constants.MininetConstants.TIME_KEY: currentTime,
                constants.MininetConstants.POSITIONS_KEY: positions
            })

class RadioFrequencyMeasurer(IMeasurer):
    def __init__(self, start, stations, measurements, isAdhoc):
        self.__start = start
        self.__stations = stations
        self.__measurements = measurements
        self.__isAdhoc = isAdhoc

    def run(self):
        while True:
            time.sleep(constants.MininetConstants.DELAY)
            currentTime = math.floor(time.time() - self.__start)

            measures, hasAtLeastOne = self.__getValidMeasures(currentTime)
            if not hasAtLeastOne:
                continue

            radioFrequency = []
            for eachNode in self.__stations:
                measObj = {}
                measObj["time"] = currentTime

                for measure in measures:
                    measureName = measure['name']
                    if measure["valid"]:
                        measObj[measureName] = self.__getMetricFromNode(measureName, eachNode)
                    else:
                        measObj[measureName] = ""

                radioFrequency.append(measObj)

            print({
                constants.MininetConstants.TIME_KEY: currentTime,
                constants.MininetConstants.RADIO_FREQUENCY_KEY: radioFrequency
            })
    
    def __isValidMeasurement(self, currentTime, measurement):
        return (currentTime % measurement["period"]) == 0

    def __getValidMeasures(self, currentTime):
        radioFrequencyMeasures = []
        hasAtLeastOne = False
        for measurement in self.__measurements:
            measure = measurement["measure"]
            measure["valid"] = self.__isValidMeasurement(currentTime, measurement)
            radioFrequencyMeasures.append(measure)

            if measure["valid"]:
                hasAtLeastOne = True
        
        radioFrequencyMeasures.append({ "name": "name", "valid": hasAtLeastOne })

        return radioFrequencyMeasures, hasAtLeastOne

    def __getMetricFromNode(self, measureName, node):
        if measureName == "position":
            return list(node.position)


        if measureName == "rssi":
            if self.__isAdhoc:
                return 'adhoc'
            else:
                return getattr(node.wintfs[0],measureName)

        
        if measureName == "associatedTo":
            if self.__isAdhoc:
                if node.wintfs[0].associatedTo:
                    return 'adhoc'
                return "None"
            else:
                if node.wintfs[0].associatedTo:
                    return node.wintfs[0].associatedTo.node.wintfs[0].name
                return "None"
        if measureName == "name":
            return node.name
        if measureName == "ip_if0":
            ip_interf0 = str(node.wintfs[0].ip)
            return ip_interf0
        if measureName == "ip_if1":
            ip_interf1 = str(node.wintfs[1].ip)
            return ip_interf1
        if measureName == "txpower_if0":
            txpower_interf0 = str(node.wintfs[0].txpower)
            return txpower_interf0
        if measureName == "txpower_if1":
            txpower_interf1 = str(node.wintfs[1].txpower)
            return txpower_interf1

        return getattr(node.wintfs[0],measureName)

class PerformanceMeasurer(IMeasurer):
    def __init__(self, start, net, measurements, nodes_om, random_choice, mayTalkTo):
        self.__start = start
        self.__net = net
        self.__measurements = measurements
        self.__nodes_om = nodes_om
        self.__random_choice = random_choice
        self.__mayTalkTo = mayTalkTo

    def run(self):
        threads = []
        for measurement in self.__measurements:
            t = threading.Thread(target=self.__collectMeasurement, args=(measurement,))
            t.daemon = True
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

    def __collectMeasurement(self, measurement):
        while True:
            result = self.__getMeasure(measurement["measure"], measurement["source"], measurement["destination"])
            currentTime = math.floor(time.time() - self.__start)
            print({
                constants.MininetConstants.TIME_KEY: currentTime,
                constants.MininetConstants.PERFORMANCE_KEY: result
            })
            time.sleep(measurement["period"])

    def __getMeasure(self, measure, sourceName, destinationName):
        name = measure["name"]

        stations = []  # all stations
        stations_destination = []
        stations_destination_pairs = []
        stations_destination_subordinates = []
        next_hop_commander = ''
        next_hop = ''
        source_commander = ''
        destination_commander = ''
        id_sec_commander = ''
        node_atual = ''
        next_node_name = ''
        commander_network_name = None
        id_sub = ''

        source_commanders = []
        destination_commanders = []
        subordinados_atuais = []
        #value = ''

        ##METADADOS DOS CONTEÚDOS
        precedence = ['urgente', 'urgentissima', 'preferencial', 'rotina']
        security_level = ['ultra-secreto', 'secreto', 'confidencial', 'reservado', 'ostensivo']
        prec = random.choice(precedence)  # escolhe a precedência aleatóriamente
        sec_level = random.choice(security_level)  # escolhe o security_level aleatóriamente

        # captura todas as estações
        for node in self.__nodes_om:
            if node["type"] == "station":
                stations.append(node)

        # CHOOSE RANDOM SOURCE
        s = random.choice(stations)
        source_Name = s["name"]

        if s["commander"] is not None:
            source_commander = s["commander"]["Id"]
        else:
            source_commander = None
        comandante_fonte = source_commander

        source_om = s["military_organization"]
        source_om_name = s["om_name"]
        source = self.__net.get(source_Name)

        #preenche a lista com todos os comandantes de source
        while comandante_fonte != None:
            for node in self.__nodes_om:  # encontra o nó que é o comandante para fazer o encaminhamento
                if node["military_organization"] == comandante_fonte:
                    source_commanders.append(node["name"]) # insere na lista
                    if node["commander"] is not None:
                        comandante_fonte = node["commander"]["Id"] # pega o próximo comandante
                    else:
                        comandante_fonte = None

        # CHOOSE RANDOM DESTINATION
        random_option = 1

        #GET RANDOM TRANSMISSION CHOICE
        for r in self.__random_choice:
            random_option = r["random_choice"]

        if random_option == 2: #2 -> comandante, subordinados e pares
            commander_name = ''
            for node in self.__nodes_om:
                if node["military_organization"] == source_commander:
                    commander_name = node["name"]
                    stations_destination.append(node)

            for node in self.__nodes_om:
                if node["commander"] is not None:
                    if node["commander"]["Id"] == source_om:
                        subordinate_name = node["name"]
                        stations_destination.append(node)
                        stations_destination_subordinates.append(subordinate_name) # add subordinates in list

            for node in self.__nodes_om:
                if node["commander"] is not None:
                    if node["commander"]["Id"] == source_commander:
                        pair_name = node["name"]
                        stations_destination.append(node)
                        stations_destination_pairs.append(pair_name) # add pairs in list

            d = random.choice(stations_destination)
            destination_Name = d["name"]
            destination_om_name = d["om_name"]
            if d["name"] == s["name"]:
                while d["name"] == s["name"]:  # proibir de ser igual ao source
                    d = random.choice(stations_destination)
                    destination_Name = d["name"]
                    destination_om_name = d["om_name"]

            destination = self.__net.get(destination_Name)

            if commander_name == destination_Name:
                value = self.__pingcommander(source, destination)
            elif destination_Name in stations_destination_subordinates:
                value = self.__pingsubordinate(source, destination)
            elif destination_Name in stations_destination_pairs:
                for node in self.__nodes_om:  # encontra o nó que é o comandante para fazer o encaminhamento
                    if node["military_organization"] == source_commander:
                        commander_network_name = node["name"]
                        next_hop = self.__net.get(commander_network_name)
                value = self.__pingcommander(source, next_hop)
                saida = str(value)
                if '0 recebidos' in saida:
                    value = value + list('Falha no encaminhamento')
                else:
                    value = value + self.__pingsubordinate(next_hop, destination)

        elif random_option == 1: #All nodes with message forwarding

            d = random.choice(stations)
            destination_Name = d["name"]
            if d["name"] == s["name"]:
                while d["name"] == s["name"]:  #proibir de ser igual ao source
                    d = random.choice(stations)

            if d["commander"] is not None:
                destination_commander = d["commander"]["Id"]
            else:
                destination_commander = None
            comandante_destino = destination_commander
            destination_om = d["military_organization"]
            destination_om_name = d["om_name"]
            destination = self.__net.get(destination_Name)

            #preenche a lista com todos os comandantes de destination
            destination_commanders.append(d["name"]) #salva o próprio destino na lista para descida
            while comandante_destino != None:
                for node in self.__nodes_om:  # encontra o nó que é o comandante para fazer o encaminhamento
                    if node["military_organization"] == comandante_destino:
                        destination_commanders.append(node["name"]) # insere na lista
                        if node["commander"] is not None:
                            comandante_destino = node["commander"]["Id"] # pega o próximo comandante
                        else:
                            comandante_destino = None
                            destination_commanders.pop() # apaga o último pois é quem vai começar a encaminhar pra baixo


            # PROCEDIMENTO DE ENVIO - ALGORITMO RECURSIVO DE ENCAMINHAMENTO DE MENSAGENS

            #PRIMEIRO CASO: ENVIAR PARA O COMANDANTE
            if source_commander == destination_om:
                value = self.__pingcommander(source, destination)
                saida = str(value)
                if '0 recebidos' in saida:
                    value = value + list('Falha no encaminhamento')

            #SEGUNDO CASO: ENVIAR PARA O SUBORDINADO
            elif source_om == destination_commander:
                value = self.__pingsubordinate(source, destination)
                saida = str(value)
                if '0 recebidos' in saida:
                    value = value + list('Falha no encaminhamento')

            #TERCEIRO CASO: VERIFICAR SE SOURCE E DESTINATION POSSUEM O MESMO COMANDANTE
            elif source_commander == destination_commander:
                for node in self.__nodes_om: # encontra o nó que é o comandante para fazer o encaminhamento
                    if node["military_organization"] == source_commander:
                        commander_network_name = node["name"]
                        next_hop = self.__net.get(commander_network_name)

                value = self.__pingcommander(source, next_hop) #um pra cima
                saida = str(value)
                if '0 recebidos' in saida:
                    value = value + list('Falha no encaminhamento')
                else:
                    value = value + self.__pingsubordinate(next_hop, destination) #e um pra baixo
                    saida = str(value)
                    if '0 recebidos' in saida:
                        value = value + list('Falha no encaminhamento')

            #QUARTO CASO: NÃO É O COMANDANTE, NEM TEM O MESMO COMANDANTE ENTÃO ENVIA PARA O COMANDANTE RECURSIVAMENTE
            #RECURSIVAMENTE ENVIA PARA O COMANDANTE DE NOVO E VERIFICA SE É O DESTINO
            #SUBIDA RECURSIVA
            elif source_commander != destination_commander:
                node_atual = source
                x = 0
                # pega o próximo nó
                next_node_name = source_commanders[0]

                for node in self.__nodes_om:  # encontra o nó que é o comandante para fazer o primeiro encaminhamento
                    if node["name"] == next_node_name:
                        commander_network_name = node["name"]
                        next_hop = self.__net.get(commander_network_name)
                        if node["commander"] is not None:
                            next_hop_commander = node["commander"]["Id"]  # e pega o comandante dele
                            for node in self.__nodes_om:  # encontra o nó que é o comandante para fazer o primeiro encaminhamento
                                if node["military_organization"] == next_hop_commander:
                                    next_hop_commander = node["name"] # pega o nome do comandante dele
                        else:
                            next_hop_commander = None
                value = self.__pingcommander(node_atual, next_hop) # envia para o comandante direto
                node_atual = next_hop
                next_node_name = next_hop_commander
                source_commanders.pop(0) # apaga o próximo nó da lista de comandantes
                #if commander_network_name == destination_Name:
                #    x = 1 # destino final
                saida = str(value)
                if '0 recebidos' in saida:
                    value = value + list('Falha no encaminhamento')
                else:
                    if next_hop_commander == None:
                        x = 1 #não da mais pra subir
                    # entra em loop para subida até encontrar o destino ou o limite
                    while x == 0:
                        for node in self.__nodes_om:  # encontra o nó que é o comandante para fazer o encaminhamento
                            if node["name"] == next_node_name:
                                commander_network_name = node["name"]
                                next_hop = self.__net.get(commander_network_name)
                                if node["commander"] is not None:
                                    next_hop_commander = node["commander"]["Id"]  # e pega o comandante dele
                                    for node in self.__nodes_om:  # encontra o nó que é o comandante para fazer o primeiro encaminhamento
                                        if node["military_organization"] == next_hop_commander:
                                            next_hop_commander = node["name"]  # pega o nome do comandante dele
                                else:
                                    next_hop_commander = None
                        value = value + self.__pingcommander(node_atual, next_hop)
                        node_atual = next_hop
                        next_node_name = next_hop_commander
                        source_commanders.pop(0)  # apaga o próximo nó da lista de comandantes
                        saida = str(value)
                        if '0 recebidos' in saida:
                            value = value + list('Falha no encaminhamento')
                            break
                        else:
                            if commander_network_name == destination_Name:
                                x = 3  # destino final
                            elif next_hop_commander == None:
                                x = 1  # não da mais pra subir

                    # DESCIDA RECURSIVA
                    if x == 1:
                        while x == 1:
                            for node in self.__nodes_om:
                                if node["name"] == destination_commanders[-1]: # o último da lista de comandantes vai ser o primeiro a recebe de cima pra baixo
                                    subordinate_network_name = node["name"]
                                    next_hop = self.__net.get(subordinate_network_name)
                            value = value + self.__pingsubordinate(node_atual, next_hop)
                            node_atual = next_hop
                            destination_commanders.pop() # apaga o nó atual
                            saida = str(value)
                            if '0 recebidos' in saida:
                                value = value + list('Falha no encaminhamento')
                                break
                            else:
                                if subordinate_network_name == destination_Name:
                                    x = 2  # destino final

        elif random_option == 3: # one to one
            source = self.__net.get(sourceName)
            destination = self.__net.get(destinationName)

            source_Name = source.name
            destination_Name = destination.name
            #destination_om_name = ''
            matching_station = None
            for station in stations:
                if station["name"] == source_Name:
                    matching_station = station
                    break
            source_om_name = matching_station["om_name"]

            #source_om_name = ''
            matching_station = None
            for station in stations:
                if station["name"] == destination_Name:
                    matching_station = station
                    break
            destination_om_name = matching_station["om_name"]

            value = self.__ping(source, destination)

            saida = str(value)
            if '0 recebidos' in saida:
                value = value + list('Falha no encaminhamento')

        elif random_option == 4:
            s = random.choice(stations)
            source_Name = s["name"]
            source = self.__net.get(source_Name)

            d = random.choice(stations)
            destination_Name = d["name"]
            if d["name"] == s["name"]:
                while d["name"] == s["name"]:  # proibir de ser igual ao source
                    d = random.choice(stations)
                    destination_Name = d["name"]
            destination = self.__net.get(destination_Name)

            #destination_om_name = ''
            matching_station = None
            for station in stations:
                if station["name"] == destination_Name:
                    matching_station = station
                    break
            destination_om_name = matching_station["om_name"]

            #source_om_name = ''
            matching_station = None
            for station in stations:
                if station["name"] == source_Name:
                    matching_station = station
                    break
            source_om_name = matching_station["om_name"]

            value = self.__ping(source, destination)

            saida = str(value)
            if '0 recebidos' in saida:
                value = value + list('Falha no encaminhamento')

        elif random_option == 5: # mayTalkTo

            may_talk_to = self.__mayTalkTo

            # Choose a random element from "mayTalkTo"
            random_element = random.choice(may_talk_to)

            # Get "talker_1" and "talker_2" values from the chosen element
            talker_1 = random_element["talker_1"]
            talker_2 = random_element["talker_2"]

            # Randomly assign source and destination
            source = random.choice([talker_1, talker_2])
            destination = talker_2 if source == talker_1 else talker_1

            source_Name = source
            destination_Name = destination

            source = source.split('-')
            source = source[0]
            source_n = source
            destination = destination.split('-')
            destination = destination[0]  # ex: sta0
            destination_n = destination

            id_intf_source = source_Name.split('wlan')
            id_intf_source = id_intf_source[1]

            id_intf_dest = destination_Name.split('wlan')
            id_intf_dest = id_intf_dest[1]

            source = self.__net.get(source)
            destination = self.__net.get(destination)

            #source_om_name = ''

            matching_station = None
            for station in stations:
                if station["name"] == destination_n:
                    matching_station = station
                    break
            destination_om_name = matching_station["om_name"] #get destination om name

            matching_station = None
            for station in stations:
                if station["name"] == source_n:
                    matching_station = station
                    break
            source_om_name = matching_station["om_name"] #get source om name

            value = self.__pingMayTalkTo(source, destination,int(id_intf_source),int(id_intf_dest))

            saida = str(value)
            if '100% perda' in saida:
                value = value + list('Falha total')

        #if name == "ping":
            #value = self.__ping(source, destination)

        #if name == "Iperf":4. Platform
            #value = self.__iperf(source, destination)

        #print(source.cmd('xterm'))

        return {"name": name,
                "source": source_Name +"-"+ source_om_name,
                "destination": destination_Name + "-" + destination_om_name,
                "value": value}

    def __pingcommander(self, source, destination):
        pingResult = source.cmd('ping', '-c 1 -q', '-I ' + source.wintfs[1].ip, destination.wintfs[0].ip)#10
        splittedResult = pingResult.split('\r\n')
        return [splittedResult[3], splittedResult[4]]

    def __pingsubordinate(self, source, destination):
        pingResult = source.cmd('ping', '-c 1 -q', '-I ' + source.wintfs[0].ip, destination.wintfs[1].ip)#01
        splittedResult = pingResult.split('\r\n')
        return [splittedResult[3], splittedResult[4]]

    def __ping(self, source, destination):
        pingResult = source.cmd('ping', '-c 10 -q', '-I ' + source.wintfs[0].ip, destination.wintfs[0].ip)
        splittedResult = pingResult.split('\r\n')
        return [splittedResult[3], splittedResult[4]]

    def __pingMayTalkTo(self, source, destination, id_intf_source, id_intf_dest):
        pingResult = source.cmd('ping', '-c 10 -q', '-I ' + source.wintfs[id_intf_source].ip, destination.wintfs[id_intf_dest].ip)
        splittedResult = pingResult.split('\r\n')
        return [splittedResult[3], splittedResult[4]]

    def __iperf(self, source, destination):
        iperfResult = source.cmd('iperf -d -c ' + destination.wintfs[0].ip)
        #splittedResult = iperfResult.split('\r\n')
        print(iperfResult)
        return []


