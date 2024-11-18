largura = float(input("Informe a largura do terreno"))
comprimento = float(input("Informe a comprimento do terreno"))
area = largura * comprimento
if area < 100 :
    print("Area do terreno e ", area, "m Terreno popular ")
elif 100 <= area <= 500:
    print("Area do terreno e ", area, "m Terreno master ")
else :
    print("Area do terreno e ", area, "m Terreno vip ")