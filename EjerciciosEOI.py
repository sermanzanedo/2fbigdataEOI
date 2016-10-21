# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 12:09:10 2016
#prueba11
@author: Sergio
"""

import collections
ruta = raw_input ("¿dime donde esta el fichero?")
apertura = open (ruta, "r")
texto = apertura.read()
milista = texto.split()
print milista
desglose= collections.Counter(milista)
desglose = str(desglose)
#items = list(desglose.items())
#print items
#miCadena = ",".split(items)
#print miCadena
#print desglose
#type(desglose)
#ConvCadena = ",".join(desglose)
#print ConvCadena
rutasalida = raw_input ("¿Dime donde quieres que lo guarde?, incluyendo nombre fichero salida")
aperturasalida = open (rutasalida, "w")
aperturasalida.write(desglose)
aperturasalida.close()
