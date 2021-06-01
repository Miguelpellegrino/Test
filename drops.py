def retornos(retornos):
    # print para observar los valores
    return print(retornos)

def plic_plac_ploc(numero):
    if type(numero) == int:
        #Cree un diccionario para trabajar por Clave Valor
        gotas = {3:'Plic', 5:'Plac', 7:'Ploc'}
        #Cree un mensaje que por defecto esta vacicio
        mensaje = ''
        #hago un ciclo for para poder sacar el factor del numero
        #utilizando la clave del diccionario
        for i in gotas.keys():
            if(numero % i == 0):
                #concateno el texto "Plic, Plac, Ploc" si cumnple la condicion
                mensaje += gotas[i]
        #Si el texto sigue vacio es porque el numero no cumple
        #con las condiciones y entonces le agrego el numero evaluado
        if mensaje == '':
            mensaje = str(numero)
        
        retornos(mensaje)
    else: return print('El argumento no es un numero')

plic_plac_ploc(30000)