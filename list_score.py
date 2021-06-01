def retornos(retornos):
    # print para observar los valores
    return print(retornos)
    
def game(puntos):
    # validar que es una lista
    if type(puntos) == list:
        #creo una nueva lista para almacenar solo los 3 elementos mas altos de la lista
        maximos = []
        #aqui obtengo el valor mas alto
        retornos(max(puntos))
        #aqui obtengo el valor mas bajo
        retornos(puntos.pop())
        #Utilizo un for que solo recorrera 3 veces para poder sacar los 3 numeros mas altos 
        # y a su vez los elimino para que en la segunda vuelta consiga el numero mas alto antecedente
        for x in range(1,4):maximos.append(max(puntos)), puntos.remove(max(puntos))
        retornos(maximos)
    else: return print('El argumento no es una lista')

game([561,51,51,11,502,00,5])
