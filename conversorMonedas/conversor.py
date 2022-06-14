from cmath import e


tipo_cambio = int(input("¿Quieres convertir mx-usd(1) o usd-mx?(2)"))

if tipo_cambio >= 1 and tipo_cambio <= 2:
    if tipo_cambio == 1:
        pesos_mexicanos = float(input("¿Cuántos pesos mexicanos tienes?: "))
        valor_dolar = 20.47
        dolares = pesos_mexicanos / valor_dolar
        dolares = round(dolares, 2)
        dolares = str(dolares)
        print("Tienes $" + dolares + " dólares")
    else:
        dolares = float(input("¿Cuántos dolares tienes?: "))
        valor_mxn = 0.049
        mxn = dolares / valor_mxn
        mxn = round(mxn, 2)
        mxn = str(mxn)
        print("Tienes " + mxn + " pesos mexicanos")
else:
    print("Opción inexistente")
