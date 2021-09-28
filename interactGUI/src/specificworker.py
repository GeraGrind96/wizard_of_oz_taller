#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#    Copyright (C) 2021 by YOUR NAME HERE
#
#    This file is part of RoboComp
#
#    RoboComp is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    RoboComp is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with RoboComp.  If not, see <http://www.gnu.org/licenses/>.
#

from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QApplication
from genericworker import *
from fpdf import FPDF
import time
import sys
from random import *
import json
import pandas as pd
import threading
import cv2
#sys.path.insert(0, os.path.join(os.getenv('HOME'), ".learnblock", "clients"))

from learnbot_dsl.Clients import EBO_sim
from learnbot_dsl.Clients import EBO_remote_sim
from learnbot_dsl.Clients import EBO
from learnbot_dsl.Clients.Client import *

# If RoboComp was compiled with Python bindings you can use InnerModel in Python
sys.path.append('/opt/robocomp/lib')

# import librobocomp_qmat
# import librobocomp_osgviewer
# import librobocomp_innermodel

class Movements(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.accionaleatoria = False
        self.randomfunctions = False
        self.instlastaction = time.time()
        self.start_time = self.instlastaction
        self.timemax = 1
        self.timemin = 1
        self.velmax = 20
        self.velmin = 20
        self.quieto = True
        self.angmax = 90
        self.angmin = -self.angmax
        self.frecmovementmin = 1
        self.frecmovementmax = 3
        self.desvio_respect_start = 0
        self.sec = randint(self.frecmovementmin, self.frecmovementmax)
        self.robot = None
        self.stopped = False
        self.posestadoactual = 4
        self.estadoactual = "Neutral"


    def run(self):

        start = time.time()

        while not self.stopped:
            if self.quieto != True:
                if time.time() - start > self.sec:
                    #if not self.accionaleatoria:
                        # self.randomMovementrotate()
                    choice([self.randomMovementbackfront(), self.randomMovementrotate()])
                    start = time.time()
                    self.sec = uniform(self.frecmovementmin, self.frecmovementmax)

    def randomMovementrotate(self):

        randomtime = uniform(self.timemin, self.timemax)
        # speed = randint(self.velmin, self.velmax)
        angle = randint(self.angmin, self.angmax)
        tact = time.time()
        while (time.time() <= tact + randomtime):
            self.robot.setBaseSpeed(0, angle)
        self.desvio_respect_start += angle*randomtime
        # tact = time.time()
        # while (time.time() <= tact + randomtime):
        #     self.robot.setBaseSpeed(-speed, angle)
        self.robot.setBaseSpeed(0, 0)
        self.start_time = time.time()
        self.sec = uniform(self.frecmovementmin, self.frecmovementmax)

    def randomMovementbackfront(self):
        tact = time.time()
        randomtime = uniform(self.timemin, self.timemax)
        speed = randint(self.velmin, self.velmax)
        while (time.time() <= tact + randomtime):
            self.robot.setBaseSpeed(speed, 0)
            self.robot.setBaseSpeed(-speed, 0)
        self.robot.setBaseSpeed(0, 0)
        self.start_time = time.time()
        self.sec = uniform(self.frecmovementmin, self.frecmovementmax)

    def afirmacion(self):
        tact = time.time()
        while (time.time() <= tact + 0.15):
            self.robot.setBaseSpeed(100, 0)
        tact = time.time()
        while (time.time() <= tact + 0.3):
            self.robot.setBaseSpeed(-100, 0)
        tact = time.time()
        while (time.time() <= tact + 0.15):
            self.robot.setBaseSpeed(100, 0)
        self.robot.setBaseSpeed(0, 0)
        self.instlastaction = time.time()

    def negacion(self):
        tact = time.time()
        while (time.time() <= tact + 0.15):
            self.robot.setBaseSpeed(100, 90)
        tact = time.time()
        while (time.time() <= tact + 0.3):
            self.robot.setBaseSpeed(100, -90)
        tact = time.time()
        while (time.time() <= tact + 0.15):
            self.robot.setBaseSpeed(100, 90)
        self.robot.setBaseSpeed(0,0)
        self.instlastaction = time.time()

    def adelante(self):
        self.robot.setBaseSpeed(50, 0)
    def atras(self):
        self.robot.setBaseSpeed(-50, 0)
    def izquierda(self):
        self.robot.setBaseSpeed(0, -45)
    def derecha(self):
        self.robot.setBaseSpeed(0, 45)

    def posicion_inicial(self):
        tiempo_rot = abs(self.desvio_respect_start)/90
        if(self.desvio_respect_start > 0):
            tact = time.time()
            while (time.time() <= tact + tiempo_rot):
                self.robot.setBaseSpeed(0, -90)
            self.robot.setBaseSpeed(0, 0)
        else:
            tact = time.time()
            while (time.time() <= tact + tiempo_rot):
                self.robot.setBaseSpeed(0, 90)
            self.robot.setBaseSpeed(0, 0)
        self.desvio_respect_start = 0

    def enviarmovimiento(self, mov):
        if mov == "Rotacion":
            tact = time.time()
            while (time.time() <= tact + 5):
                self.robot.setBaseSpeed(150, 90)
            self.robot.setBaseSpeed(0, 0)
        elif mov == "BackFront":
            tact = time.time()
            while (time.time() <= tact + 0.05):
                self.robot.setBaseSpeed(150, 0)
            tact = time.time()
            while (time.time() <= tact + 0.1):
                self.robot.setBaseSpeed(-150, 0)
            tact = time.time()
            while (time.time() <= tact + 0.1):
                self.robot.setBaseSpeed(150, 0)
            tact = time.time()
            while (time.time() <= tact + 0.1):
                self.robot.setBaseSpeed(-150, 0)
            tact = time.time()
            while (time.time() <= tact + 0.05):
                self.robot.setBaseSpeed(150, 0)
            self.robot.setBaseSpeed(0, 0)

    def stop(self):
        self.stopped = True
        self.join()

class SpecificWorker(GenericWorker):
    def __init__(self, proxy_map, startup_check=False):
        super(SpecificWorker, self).__init__(proxy_map)
        self.Period = 200
        if startup_check:
            self.startup_check()
        else:
            self.timer.timeout.connect(self.compute)
            self.timer.start(self.Period)
        try:
            self.movements = Movements()
        
        except:
            print("Es un portátil, no EBO")

        try:
            self.ui.textoaenviar.returnPressed.connect(self.mandarvoz)
        except:
            print("Falta cuadro de texto")

        self.strhorainicio = time.strftime("%H-%M-%S")
        self.timeultimainteraccion = time.time()

        self.ui.nuevaconv.clicked.connect(self.comenzardenuevo)
        self.ui.finprograma.clicked.connect(self.end_program)
        # self.ui.toexcel.clicked.connect(self.toExcel)
        try:
            self.ui.mandarfrase.clicked.connect(self.enviarfrasedesplegable)
        except:
            print("Falta botón enviar frase")
        try:
            self.ui.botonmiedo.clicked.connect(self.estadoMiedo)
        except:
            print("Falta boton de emocion miedo")        
        try:
            self.ui.botonalegria.clicked.connect(self.estadoAlegre)
        except:
            print("Falta boton de emocion alegre")
        try:
            self.ui.botonsorpresa.clicked.connect(self.estadoSorpresa)
        except:
            print("Falta boton de emocion sorpresa")
        try:
            self.ui.botontriste.clicked.connect(self.estadoTriste)
        except:
            print("Falta boton de emocion triste")
        try:
            self.ui.botonneutral.clicked.connect(self.estadoNeutral)
        except:
            print("Falta boton de emocion neutral")
        try:
            self.ui.botondisgustado.clicked.connect(self.estadoDisgustada)
        except:
            print("Falta boton de emocion disgustada")
        try:
            self.ui.botonenfadado.clicked.connect(self.estadoEnfadada)
        except:
            print("Falta boton de emocion enfadada")
        try:
            self.ui.botonquieto.clicked.connect(self.estadoQuieto)
            self.ui.gostraight.pressed.connect(self.movements.adelante)
            self.ui.goback.pressed.connect(self.movements.atras)
            self.ui.turnleft.pressed.connect(self.movements.izquierda)
            self.ui.turnright.pressed.connect(self.movements.derecha)
        except: 
            print("faltan botones de desplazamiento")

        self.ui.inicioconversacion.clicked.connect(self.page2)

        try:
            self.ui.finconversacion.clicked.connect(self.page3)
        except:
            print("Falta fin conversación")

        try:
            self.movements.start()
        except:
            print("Es un portátil, no EBO")

        try:
            self.ui.conversacion.hideColumn(1)
        except:
            print("falta arbol de conversación")

        self.state = 1

        self.usuario = ""

        self.ui.stackedWidget.setCurrentIndex(0)

    def __del__(self):
        print('SpecificWorker destructor')

    def setParams(self, params):
        return True

    @QtCore.Slot()
    def compute(self):
        return True

    ####################### Envío de frases #######################

    def enviarfrasedesplegable(self):
        textoadecir = self.ui.conversacion.currentItem()
        try:
            self.ponerCara(int(textoadecir.text(1)))
        except:
            print("no existe la cara")
        frase = textoadecir.text(0)
        print(frase)
        if("+self.usuario+") in frase:
            print("está")
            frase = frase.replace("+self.usuario+",self.usuario)
        self.speech_proxy.setPitch(self.ui.pitchBar.value())
        self.speech_proxy.setTempo(self.ui.tempoBar.value())
        self.speech_proxy.say(frase, True)
        textoadecir.setBackgroundColor(0, QColor(255, 255, 0, 100))
        self.timeultimainteraccion = time.time()

    def mandarvoz(self):

        if (self.usuario != ""):
            textoadecir = self.ui.textoaenviar.text()
            print(textoadecir)
            if("+self.usuario+") in textoadecir:
                print("está")
                textoadecir = textoadecir.replace("+self.usuario+",self.usuario)
            self.ui.textoaenviar.clear()
            try:
                if(textoadecir != ""):
                    self.speech_proxy.setPitch(self.ui.pitchBar.value())
                    self.speech_proxy.setTempo(self.ui.tempoBar.value())
                    self.speech_proxy.say(textoadecir, True)
                    self.instlastaction = time.time()

            except:
                print("Error")

    ####################### Control de la interfaz #######################

    def page2(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.usuario = self.ui.nombre_usuario.text()

    def page3(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def comenzardenuevo(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.state = 0
        iterator = self.conversacion.QTreeWidgetItemIterator
        self.conversacion.setBackground(0,QColor(255, 255, 255, 255))

    ####################### Estados de ánimo #######################

    def estadoTriste(self):
        self.emotionalmotor_proxy.expressSadness()
        try:
            self.movements.quieto = False        
            self.movements.estadoactual = "Triste"
            self.movements.posestadoactual = 3
            self.movements.instlastaction = time.time()
            self.movements.timemax = 0.9
            self.movements.timemin = 1.2
            self.movements.velmax = 10
            self.movements.velmin = 1
            self.movements.frecmovementmin = 4
            self.movements.frecmovementmax = 8
            self.movements.angmax = 30
        except:
            print("Es un portátil, no EBO")
        self.timeultimainteraccion = time.time()

    def estadoAlegre(self):  
        self.emotionalmotor_proxy.expressJoy()
        try:
            self.movements.quieto = False
            self.movements.estadoactual = "Alegre"
            self.movements.posestadoactual = 0
            self.movements.instlastaction = time.time()
            self.movements.timemax = 0.15
            self.movements.timemin = 0.3
            self.movements.velmax = 140
            self.movements.velmin = 100
            self.movements.frecmovementmin = 2
            self.movements.frecmovementmax = 3
            self.movements.angmax = 60
        except:
            print("Es un portátil, no EBO")
        self.timeultimainteraccion = time.time()

    def estadoEnfadada(self):
        self.emotionalmotor_proxy.expressAnger()
        try:
            self.movements.quieto = False
            self.movements.estadoactual = "Enfadada"
            self.movements.posestadoactual = 1
            self.movements.instlastaction = time.time()
            self.movements.timemax = 0.3
            self.movements.timemin = 0.15
            self.movements.velmax = 140
            self.movements.velmin = 100
            self.movements.frecmovementmin = 1
            self.movements.frecmovementmax = 2
            self.movements.angmax = 90
        except:
            print("Es un portátil, no EBO")
        self.timeultimainteraccion = time.time()

    def estadoNeutral(self):
        self.emotionalmotor_proxy.expressNeutral()
        try:
            self.movements.quieto = False
            self.movements.estadoactual = "Neutral"
            self.movements.posestadoactual = 4
            self.movements.instlastaction = time.time()
            self.movements.timemax = 0.3
            self.movements.timemin = 0.15
            self.movements.velmax = 80
            self.movements.velmin = 60
            self.movements.frecmovementmin = 2
            self.movements.frecmovementmax = 4
            self.movements.angmax = 90
        except:
            print("Es un portátil, no EBO")
        self.timeultimainteraccion = time.time()

    def estadoDisgustada(self):
        self.emotionalmotor_proxy.expressDisgust()
        try:
            self.movements.quieto = False
            self.movements.estadoactual = "Disgustada"
            self.movements.posestadoactual = 2
            self.movements.instlastaction = time.time()
            self.movements.timemax = 0.7
            self.movements.timemin = 1
            self.movements.velmax = 40
            self.movements.velmin = 20
            self.movements.frecmovementmin = 4
            self.movements.frecmovementmax = 8
            self.movements.angmax = 30
        except:
            print("Es un portátil, no EBO")
        self.timeultimainteraccion = time.time()

    def estadoSorpresa(self):
        self.emotionalmotor_proxy.expressSurprise()
        try:
            self.movements.quieto = False
            self.movements.estadoactual = "Sorpresa"
            self.movements.posestadoactual = 5
            self.movements.instlastaction = time.time()
            self.movements.timemax = 0.3
            self.movements.timemin = 0.15
            self.movements.velmax = 80
            self.movements.velmin = 60
            self.movements.frecmovementmin = 1
            self.movements.frecmovementmax = 2
            self.movements.angmax = 50
        except:
            print("Es un portátil, no EBO")
        self.timeultimainteraccion = time.time()

    def estadoMiedo(self):
        self.emotionalmotor_proxy.expressFear()
        try:
            self.movements.quieto = False
            self.movements.estadoactual = "Miedo"
            self.movements.posestadoactual = 6
            self.movements.instlastaction = time.time()
            self.movements.timemax = 0.2
            self.movements.timemin = 0.15
            self.movements.velmax = 80
            self.movements.velmin = 60
            self.movements.frecmovementmin = 0.2
            self.movements.frecmovementmax = 1
            self.movements.angmax = 120
        except:
            print("Es un portátil, no EBO")
        self.timeultimainteraccion = time.time()

    def estadoQuieto(self):
        try:
            self.movements.quieto = True
            self.movements.robot.setBaseSpeed(0, 0)
        except:
            print("Es un portátil, no EBO")

    def ponerCara(self, number):
        if(number == 0):
            self.emotionalmotor_proxy.expressFear()
        elif(number == 1):
            self.emotionalmotor_proxy.expressSurprise()
        elif(number == 6):
            self.emotionalmotor_proxy.expressDisgust()
        elif(number == 3):
            self.emotionalmotor_proxy.expressNeutral()
        elif(number == 4):
            self.emotionalmotor_proxy.expressAnger()
        elif(number == 5):
            self.emotionalmotor_proxy.expressJoy()
        else:
            self.emotionalmotor_proxy.expressSadness()

    def select_robot(self):
        print("Introduce el robot a utilizar: ")
        rob = input()
        try:
            if (rob == "sim"):
                try:
                    self.robot = EBO_sim.Robot()
                except Exception as e:
                    print("Problems creating EBO_sim instance")
                    raise (e)
            elif (rob == "remote"):
                try:
                    self.robot = EBO_remote_sim.Robot()
                except Exception as e:
                    print("Problems creating EBO_remote_sim instance")
                    raise (e)
            else:
                try:
                    self.robot = EBO.Robot()
                except Exception as e:
                    print("Problems creating EBO instance")
                    raise (e)
            self.movements.robot = self.robot
        except:
            print("Es un portátil, no EBO")

    def startup_check(self):
        QTimer.singleShot(200, QApplication.instance().quit)

    def end_program(self):
        try:
            self.movements.stop()
            self.robot.stop()
        except:
            print("Es un portátil, no EBO")
        quit()








