# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 10:42:33 2016

@author: Sergio
"""

#programa para enviar correo por gmail.
import smtplib

# Datos
def mandarEmail():
    print ""
    print "Este es un programa para enviar correos electronicos"
    servidorCorreo = raw_input ("Dime tu servidor smtp salida: \n")
    puerto = raw_input ("Dime puerto de salida \n")
    username = raw_input ("Dime tu direccón de gmail:\n")
    password = raw_input ("¿Dime tu clave:\n")
 # Enviando el correo
    server = smtplib.SMTP(servidorCorreo, puerto)
    print server.ehlo() 
    server.starttls()
    print server.ehlo() 
    server.login(username,password)

    fromaddr = username
    toaddrs  = raw_input("Dime dirección gmail destino: \n")
    msg = raw_input ("Escribe el contenido del email que quieres enviar: \n")

    confirmacion = raw_input ("¿Desea enviar el mensaje: S o N:\n")
    if confirmacion == "S":
        try:
            server.sendmail(fromaddr, toaddrs, msg)
        except:
            print "Ha sido imposible mandar el email"
            
        #print "Mensaje enviado correctamente"
            
    else:
        print " El mensaje no se ha enviado"
    server.quit()
while True:
    mandarEmail()
    Repetir = raw_input ("¿Quiere volver a mandar otro email: S o N:\n")
    if Repetir == "N" or Repetir == "n":
        break
print "Gracias por usar el programa"

