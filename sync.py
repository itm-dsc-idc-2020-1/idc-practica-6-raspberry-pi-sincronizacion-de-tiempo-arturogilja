from time import ctime
import datetime
import ntplib
import os

servidor_de_tiempo = "3.mx.pool.ntp.org"
print('\nObteniendo la hora del servidor NTP: ')
cliente_ntp = ntplib.NTPClient()

respuesta = cliente_ntp.request(servidor_de_tiempo)
hora_actual = datetime.datetime.strptime(
    ctime(respuesta.tx_time), "%a %b %d %H:%M:%S %Y")
print("Respuesta de " + servidor_de_tiempo + ":" + str(hora_actual) + "\n")
formated = hora_actual.__format__("%m%d%H%M%Y")

print("Hora formateada para comando date: " + formated)
print("Comando a ejecutar: sudo date -u " + formated)
os.system('sudo date -u '+formated)
print('Hora ajustada con éxito')
