from datetime import date
class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 


class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso = ''
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self, f):
        self.__fecha_ingreso = f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n  
    
    def eliminarMedicamento(self,medic):
        
        for t in self.__lista_medicamentos:
            if t.verNombre() == medic:
                self.__lista_medicamentos.remove(t)
                return True
                
        return False


class sistemaV:
    def __init__(self):
        self.__lista_mascotas = []
    
    def verificarExiste(self,historia):
        for m in self.__lista_mascotas:
            if historia == m.verHistoria():
                return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False

    def verNumeroMascotas(self):
        return len(self.__lista_mascotas) 
    
    def ingresarMascota(self,mascota):
        self.__lista_mascotas.append(mascota) 

    def verFechaIngreso(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verFecha() 
        return None

    def verMedicamento(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verLista_Medicamentos() 
        return None
    
    def eliminarMascota(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                self.__lista_mascotas.remove(masc)  #opcion con el pop
                return True  #eliminado con exito
        return False 
    
    def verificarMedicamento(self,historia_,medicamento):
        for q in self.__lista_mascotas:
            if historia_ == q.verHistoria():
                for l in q.verLista_Medicamentos():
                    if medicamento == l.verNombre():
                        return True
        return False
    
    def verMascota(self,historia_2):
        for masc in self.__lista_mascotas:
            if historia_2 == masc.verHistoria():
                return masc
            
        return None


def main():
    servicio_hospitalario = sistemaV()
    lista_felinos = {}
    lista_caninos = {}
    
    # sistma=sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota
                       \n6- Eliminar medicamento de una mascota 
                       \n7- Salir 
                       \nUsted ingresó la opción: ''' ))
        
        if menu==1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            historia=int(input("Ingrese la historia clínica de la mascota: "))
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia) == False:

                while True:

                    tipo = input("""Ingrese el tipo de mascota: 
                                'F' si es felino
                                'C' si es canino
                                
                                > """)
                    tipo = tipo.upper()

                    if tipo == 'F':
                        break
                    elif tipo == 'C':
                        break
                    else:
                        print('No es una opción válida. Intente de nuevo.')

                nombre=input("Ingrese el nombre de la mascota: ")
                nombre=nombre.upper()

                peso=int(input("Ingrese el peso de la mascota (Kg): "))

                while True:
                    try:
                        dia = int(input('Ingrese el día de ingreso: '))
                        mes = int(input('Ingrese el mes de ingreso: '))
                        año = int(input('Ingrese el año de ingreso: '))

                        fecha = date(año,mes,dia).strftime('%d/%m/%Y')
                        break

                    except ValueError:
                        print('Hay un dato incorrecto. Intente de nuevo.')


                nm=int(input("Ingrese cantidad de medicamentos: "))
                lista_med=[]

                for i in range(0,nm):
                    while True:
                        nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                        nombre_medicamentos = nombre_medicamentos.upper()
                        
                        if servicio_hospitalario.verificarMedicamento(historia,nombre_medicamentos) == True:
                            print('El medicamento ingresado ya existe en la historia clínica de esta mascota')
                            
                        else:
                            dosis =int(input("Ingrese la dosis: "))
                            medicamento = Medicamento()
                            medicamento.asignarNombre(nombre_medicamentos)
                            medicamento.asignarDosis(dosis)
                            lista_med.append(medicamento)

                            mas= Mascota()
                            servicio_hospitalario.ingresarMascota(mas)
                            mas.asignarNombre(nombre)
                            mas.asignarHistoria(historia)
                            mas.asignarPeso(peso)
                            mas.asignarTipo(tipo)
                            mas.asignarFecha(fecha)
                            mas.asignarLista_Medicamentos(lista_med)


                            break

                if tipo == 'F':
                    listaMed_1 = servicio_hospitalario.verMedicamento(historia)
                    if listaMed_1 != None: 
                        for k in listaMed_1:
                            name = k.verNombre()
                            dos = k.verDosis()

                    lista_felinos[historia] = {'nombre': mas.verNombre(),'peso': mas.verPeso(), 'fecha':mas.verFecha(), 'medicamentos': {'nombre': name, 'dosis': dos}}
                
                elif tipo == 'C':
                    listaMed_2 = servicio_hospitalario.verMedicamento(historia)
                    if listaMed_2 != None: 
                        for k in listaMed_2:
                            name = k.verNombre()
                            dos = k.verDosis()

                    lista_caninos[historia] = {'nombre': mas.verNombre(),'peso': mas.verPeso(), 'fecha':mas.verFecha(), 'medicamentos': {'nombre': name, 'dosis': dos}}
                


                for j in lista_felinos:
                    print(f'\nLa historia clínica {j} corresponde a un felino llamado {lista_felinos[j]["nombre"]}, su peso es de {lista_felinos[j]["peso"]}, llegó el {lista_felinos[j]["fecha"]}')
                
                for r in lista_caninos:
                    print(f'\nLa historia clínica {r} corresponde a un felino llamado {lista_caninos[r]["nombre"]}, su peso es de {lista_caninos[r]["peso"]}, llegó el {lista_caninos[r]["fecha"]}')
                

            else:
                print("Ya existe la mascota con el numero de histoira clinica")


        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")

        elif menu == 6:
            w = int(input('Ingrese la historia clínica de la mascota: '))
            t = input('Ingrese el medicamento a eliminar: ')

            if servicio_hospitalario.verificarExiste(w):
                pet = servicio_hospitalario.verMascota(w)

                if pet:
                    pet.eliminarMedicamento(t)
                    print('Medicamento eliminado exitosamente')

            
                else:
                    print('No se ha podido eliminar el medicamento. Intente de nuevo.')
        
        elif menu==7:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()





            

                

