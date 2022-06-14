menu = """
Bienvenido al conversor de monedas

1.-mxn-usd
2.-usd-mxn
3.-col-usd
4.-ars-usd

Elige una opción:
"""

opcion = int(input(menu))

if opcion >= 1 and opcion <= 4:
    if opcion == 1:
        pesos_mexicanos = float(input("¿Cuántos pesos mexicanos tienes?: "))
        valor_dolar = 20.47
        dolares = pesos_mexicanos / valor_dolar
        dolares = round(dolares, 2)
        dolares = str(dolares)
        print("Tienes $" + dolares + " dólares")
    elif opcion == 2:
        dolares = float(input("¿Cuántos dolares tienes?: "))
        valor_mxn = 0.049
        mxn = dolares / valor_mxn
        mxn = round(mxn, 2)
        mxn = str(mxn)
        print("Tienes " + mxn + " pesos mexicanos")
    elif opcion == 3:
        pesos_colombianos = float(input("¿Cuántos pesos colombianos tienes?: "))
        valor_dolar = 3991.33
        dolares = pesos_colombianos/valor_dolar
        dolares = round(dolares, 2)
        dolares = str(dolares)
        print("Tienes $" + dolares + " dólares")
    else:
        pesos_argentinos = float(input("¿Cuantos pesos argentinos tienes?: "))
        valor_dolar = 122.31
        dolares = pesos_argentinos/valor_dolar
        dolares = round(dolares,2)
        dolares = str(dolares)
        print("Tienes $" + dolares + " dólares")
    
else:
    print("Opción inexistente")
