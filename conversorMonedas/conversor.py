def conversor(tipo_pesos, valor_dolar):
    if tipo_pesos != "dolares":
        pesos = float(input("¿Cuántos pesos " + tipo_pesos + " tienes?: "))
        dolares = pesos / valor_dolar
        dolares = round(dolares, 2)
        dolares = str(dolares)
        return dolares
    else:
        dolares = float(input("¿Cuántos dolares tienes?: "))
        mxn = dolares / valor_mxn
        mxn = round(mxn, 2)
        mxn = str(mxn)
        return mxn


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
        pesos= "mexicanos"
        moneda = "dólares"
        valor_dolar = 20.47
        total = conversor(pesos, valor_dolar)
    elif opcion == 2:
        pesos = "dolares"
        moneda = "pesos mexicanos"
        valor_mxn = 0.049
        total = conversor(pesos, valor_mxn)
    elif opcion == 3:
        pesos = "colombianos"
        moneda = "dólares"
        valor_dolar = 3991.33
        total = conversor(pesos, valor_dolar)
    else:
        pesos = "argentinos"
        moneda = "dólares"
        valor_dolar = 122.31
        total = conversor(pesos, valor_dolar)
    print("Tienes $" + total + " " + moneda)
else:
    print("Opción inexistente")
