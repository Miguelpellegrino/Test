def helloworld(c1, c2):
    #verifica que los argumentos sean de tipo string
    if type(c1) == str and type(c2) == str:
        #print para el primer parametro que recibe "c1"
        print(c1)
        #print para el segundo parametro que recibe "c2"
        print(c2)
        #concatenando los 2 paramtros para mostrar mensaje completo
        print('{},{}'.format(c1, c2))
    else: return print('Uno de los argumentos no es un string')
    
helloworld("¡Hola","Mundo!")