#Paquetes
import random
import time 
import math
import os
import numpy_financial as npf
import tabulate as tab
from datetime import date
from dateutil.relativedelta import relativedelta
from ctypes.wintypes import PINT
from time import process_time_ns


#---------------------------Omar Guillermo Aquino Mena 21-0689---------------------------

#Parte 2 (Impresión de Tabla de Amortización)
os.system('cls')
print('                                              .:MENU:.                                               ')
print('=====================================================================================================')
print('1. Visualización de Tabla de Amortización\n2. Estado de Cuenta de Prestamo\n3. Historial de Pagos')
print('=====================================================================================================')

menu= int(input("\nDigite la opcion deseada: "))

if menu == 1: # Opción 1 del Menú, que enseña y printea la Tabla de Amortización del restante de un prestamo
  os.system('cls')
  capital = int(input('Cantidad de Capital pendiente: '))
  capital_real = abs(capital)
  tasa = float(input('Tasa de Interés: '))
  tasa_real = tasa/100
  plazo = int(input('Cantidad de Plazos: '))
  cuota = round(npf.pmt(tasa_real, plazo, -capital, 0), 0)
  datos = []
  saldo = capital
  fecha = date.today()

  for i in range(1, plazo+1):
    pago_capital = npf.ppmt(tasa_real, i, plazo, -capital_real, 0)
    pago_int = cuota - pago_capital
    saldo -= pago_capital
    if fecha == date.today() or fecha != date.today(): # Visualización futura del las fechas de pago
      fecha += relativedelta(months=1)
    saldo_real = abs(saldo)
    linea = [fecha, i, format(cuota, '0,.0f'), format(pago_capital, '0,.0f'), format(pago_int, '0,.0f'), format(saldo_real, '0,.0f')]
    datos.append(linea)

  print(tab.tabulate(datos, headers=['Fecha','Periodo', 'Cuota', 'Capital', 'Intereses', 'Saldo'], tablefmt='psql')) # Printea todos los datos del Historial de Pago con formato de con tablas

  time.sleep(8)
  os.system('cls')

  with open("Historial de Proyecciones.txt","a") as f: # Guardará todos los datos de las tablas en este archivo
    f.write(f"\n\n___________________________________________________________________________________________________________________\n\n")
    f.write(tab.tabulate(datos, headers=['Fecha','Periodo', 'Cuota', 'Capital', 'Intereses', 'Saldo'], tablefmt='psql'))

# Parte 9 (Impresión de Estado de Cuenta)

elif menu == 2: # Opción 2 del Menú, que enseña y printea el Historial de Estado de Cuenta de un prestamo
  os.system('cls')
  prestamo = 100000
  plazo = 1
  tasa = float(input('Tasa de Interés del Préstamo: '))
  tasa_real = tasa/100
  pago_int = prestamo * tasa_real
  saldo = prestamo + pago_int

  for i in range(1,plazo+999):
    abono = int(input('Cantidad de Abono de abono: '))

    if abono <= 0:
      print ('No es posible abonar esta cantidad') # Si el abono es mas pequeño de lo definido, printea este mensaje
      break

    elif abono > prestamo:
      print ('Esta cantidad es mayor a la cantidad faltante del prestamo actual') # Si el abono es mas grande de lo definido, printea este mensaje
      break;
    
    cuota = round(npf.pmt(tasa_real, plazo, -prestamo, 0), 0)
    datos = []
    pago_prestamo = abono
    saldo -= pago_prestamo
    fecha = date.today()
    linea = [fecha, i, format(cuota, '0,.0f'), format(pago_prestamo, '0,.0f'), format(pago_int, '0,.0f'), format(saldo, '0,.0f')]
    datos.append(linea)

    print(tab.tabulate(datos, headers=['Fecha','Periodo', 'Prestamo', 'Abono', 'Intereses', 'Saldo'], tablefmt='psql')) # Printea todos los datos del Historial de Pago con formato de con tablas
    
    if abono == saldo or saldo == 0: # Si el abono es igual al saldo o el saldo se hace 0, printea este mensaje
      print ('Prestamo pagado con exito!')
      break

  time.sleep(3)
  os.system('cls')

  with open("Historial de Estado de Cuenta.txt","a") as f: # Guardará todos los datos de las tablas en este archivo
    f.write(f"\n\n___________________________________________________________________________________________________________________\n\n")
    f.write(tab.tabulate(datos, headers=['Fecha','Periodo', 'Cuota', 'Abono', 'Intereses', 'Saldo'], tablefmt='psql'))

# Parte 10 (Historial de Pago)

elif menu == 3: # Opción 3 del Menú, que printea el Historial de Pago
  os.system('cls')
  historial = open("Historial de Estado de Cuenta.txt","r")
  contenido = historial.read()
  print (contenido)
  historial.close()
  seleccion = str(input('Desea salir?(Si lo hace, escribir "Si"): ')).lower()

  if seleccion == 'si': # Si desea salir, presentará este mensaje
    print('Saliendo...')
    time.sleep(1.5)
    os.system('cls')

  else:
    print('Para salir, por favor escribir "Si"') # En caso de que no escriba la opción deseada desea salir, presentará este mensaje

else:
  print("Opción inválida, por favor vuelva a intentarlo") # Si no elige una opción en le Menu presentará este mensaje

#---------------------------Luis Daniel Figuereo Alvarez 21-0587---------------------------
class Proyecto():
	def __init__(self):
		self.inicio_programa = True
		while self.inicio_programa:
			self.finalizacion_programa = "Programa finalizado..."
			self.mensaje_servicio = print(["1-Cancelacion de Prestamo", "2-Calculo de Cuota", "3-Registro" , "4-Salir"])
			self.seleccion_servicio = input("Servicio requerido: ")
			
			if self.seleccion_servicio == "1": #Punto 4
				self.cancelacion_prestamo = input("Desea cancelar el prestamo Y/N? ")
				if self.cancelacion_prestamo == "y" or self.cancelacion_prestamo == "Y":
					self.nombre = input("Por favor, ingrese su nombre: ")
					self.apellido = input("Por favor, ingrese su apellido: ")
					self.cedula = int(input("Por favor, ingrese su cedula: "))
					if self.nombre == "Daniel" and self.apellido == "Figuereo":
						#print("Prestamo cancelado")
						self.n = 5
						while self.n > 0:
							print(self.n)
							time.sleep(1)
							self.n -= 1
						print("Prestamo Cancelado")	
						print(self.finalizacion_programa)
						break;

					else:
						print("No se encuentra en nuestra base de datos.")
						self.intento = input("Desea intentar nuevamente Y/N: ")
						if self.intento == "y" or self.intento == "Y":
							self.nombre = input("Por favor, ingrese su nombre: ")
							self.apellido = input("Por favor, ingrese su apellido: ")
							self.cedula = int(input("Por favor, ingrese su cedula: "))
							if self.nombre == "Daniel" and self.apellido == "Figuereo":
								print("Prestamo cancelado")
								print(self.finalizacion_programa)
								break;

						if self.intento == "n" or self.intento == "N":
						   print(self.finalizacion_programa)	
						   break;					
		
			if self.seleccion_servicio == "2": #Punto 6
				not_string_1 = True
				while not_string_1:
					try:
						self.capital_prestamo = int(input("Capital-Prestamo: "))
						break;
					except ValueError:
						print("Por favor, ingrese un numero")	
				
				not_string_2 = True
				while not_string_2:
					try:
						self.interes = int(input("Intereses: "))
						break;
					except ValueError:
						print("Por favor, ingrese un numero")

				not_string_3 = True
				while not_string_3:
					try:
						self.plazo_amortizacion = int(input("Plazo: "))
						break;
					except ValueError:
						print("Por favor, ingrese un numero.")

				self.calculo_cuota = (self.plazo_amortizacion * 12)
				self.total_cuota = print("Total de Pago Mensual:" , self.capital_prestamo / self.calculo_cuota)
				print(self.finalizacion_programa)
				break;

		
			if self.seleccion_servicio == "3": #Punto 8
				self.tasa_interes = input("Interes: ")
				self.capital = input("Capital: ")
				self.monto_prestado = input("Monto prestado: ")
				self.monto_total = input("Monto total: ")
				print("----------Registro----------")
				print("Intereses: " + self.tasa_interes)
				print("Capital: " + self.capital)
				print("Monto prestado: " + self.monto_prestado)
				print("Monto total: " + self.monto_total)
				print(self.finalizacion_programa)
				break;

			if self.seleccion_servicio == "4":
				self.n = 3
				while self.n > 0:
					print(self.n)
					time.sleep(1)
					self.n -= 1
				print("Gracias por preferirnos.")
				print(self.finalizacion_programa)
				break;	
proyecto = Proyecto()

#---------------------------Fracisco Javier Cordero Contreras 21-0893---------------------------

print("Bienvenido al menu principal, presione una tecla para continuar..: ")
#Esto es una pausa
input()
print("Eliga que operacion quiere realizar")
print("=====================================================================================================")
print("1. Solicitud de prestamo","2. Consulta de clientes","3. Pago de prestamo")
print("=====================================================================================================")
interes6=0.15
interes12=0.10
interes24=0.08
menu=int(input("Digite la opcion deseada: "))
if menu == 1:
   #MENU DE SOLICITUD DE PRESTAMO
    print('ha seleccionado la opcion "Solicitud de Prestamo", a continuacion llene los campos requeridos')
    nombre_Cli=input("Digite el nombre del solicitante: ")
    apellido_Cli=input("Digite el apellido del solicitante: ")
    cedula_Cli=input("Digite la cedula del solicitante: ")
    monto_solicitado=int(input("Digite el monto que desea solicitar: "))
    print("=====================================================================================================")
    print('Seleccione la cantidad de quotas. Ejemplo:6 meses, 12 meses, 24 meses')
    print("=====================================================================================================")
    tiempo_prestamo=int(input("Tiempo de duracion del prestamo en meses:"))
    with open('clientes.txt','a') as f:
        nombre=nombre_Cli
        apellido=apellido_Cli
        cedula=cedula_Cli
        monto=str(monto_solicitado)
        f.writelines(('Nombre:',nombre,'   Apellido:',apellido,'   Cedula:',cedula,'   Monto desenvolsado:',monto,"\n"))
    input()
    if tiempo_prestamo == 6:
        interes_adeudado6=monto_solicitado*interes6
        capital_adeudado6=monto_solicitado+interes_adeudado6
        cuota6=capital_adeudado6/tiempo_prestamo
        a=6101
        while a < 1: 
            a+1
        print("Usted a seleccionado la opcion a 6 meses, con una tasa de 0.15 mensual","(",interes_adeudado6,")","RD$\n")

        print("El monto adeudado sera",capital_adeudado6,"RD$","con una cuota mensual de",cuota6,"RD$","Durante 6 meses\n")

        print("Su numero de prestamo es ",a,"La fecha de pago de su prestamo es el 1 de cada mes \n")

        input()
    elif tiempo_prestamo == 12:
        interes_adeudado12=monto_solicitado*interes12
        capital_adeudado12=monto_solicitado+interes_adeudado12
        cuota12=capital_adeudado12/tiempo_prestamo
        b=1201
        while b < 1: 
            b+1
        print("Usted a seleccionado la opcion a 12 meses, con una tasa de 0.10 mensual","(",interes_adeudado12,")","RD$\n")

        print("El monto adeudado sera",capital_adeudado12,"RD$","con una cuota mensual de",cuota12,"RD$","Durante 12 meses\n")

        print("Su numero de prestamo es ",b,"La fecha de pago de su prestamo es el 1 de cada mes \n")

        input()
    elif tiempo_prestamo == 24:
        interes_adeudado24=monto_solicitado*interes24
        capital_adeudado24=monto_solicitado+interes_adeudado24    
        cuota24=capital_adeudado24/tiempo_prestamo
        c=2401
        while c < 1: 
            c+1
        print("Usted a seleccionado la opcion a 24 meses, con una tasa de 0.08 mensual","(",interes_adeudado24,")","RD$\n")

        print("El monto adeudado sera",capital_adeudado24,"RD$","con una cuota mensual de",cuota24,"RD$","Durante 24 meses\n")

        print("Su numero de prestamo es ",c,"La fecha de pago de su prestamo es el 1 de cada mes \n")

        input()
    else:
        print("ha seleccionado una opcion invalida, vuelva a intentarlo..")

elif menu == 2:
   #MENU DE CONSULTA DE CLIENTE
     print('ha seleccionado la opcion "Consulta de cliente", a continuacion llene los campos requeridos')
     with open('clientes.txt','r') as f:
        buscar=input("Digite el nombre del cliente: ")
        for i in f:
            if buscar in i:
                print(i)
            


elif menu == 3:
   #MENU DE PAGO DE PRESTAMO
    print('ha seleccionado la opcion "Pago de prestamo", a continuacion llene los campos requeridos...')
    with open('clientes.txt','r') as f:
        buscar=input("Digite el nombre del cliente: ")
        for i in f:
            if buscar in i:
                print(i)
                si= input("Desea pagar el monto desenvolsado? Si/NO: ")
                if si=="si":
                    with open('clientes.txt','w') as f:
                        print("Su pago a sido realizado exitosamente, su nuevo valance pendiente es 0.00 RD$")
                elif si == "no":
                    no=input("Desea pagar la cuota mensual? SI/NO: ")
                    if no=="si":
                        print("La cuota se ha pagado de manera exitosa")
                    elif si=="no":
                        break
else:
    print("ha seleccionado una opcion invalida, vuelva a intentarlo..")		
 