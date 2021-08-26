type = bool(input("Se alcool digite false ou se gasolina digite true"))
preco_gas = float(3.3)
preco_alc = float(2.9)
desconto = float
preco = float

if type == true:
    true = float(input("Digite a quantidade de gasolina:"))
        if true <= 20:
        desconto = preco_gas * 0.96
        preco = desconto * true
        print("O valor total é: " + preco)
        if true > 20:
        desconto = preco_gas * 0.94
        preco = desconto * true
        print("O valor total é: " + preco)
else:
    false = float(input("Digite a quantidade alcool: "))
    if false >= 20:
    desconto = preco_alc * 0.97
    preco = desconto * false
    print("O valor total é: " + preco)
    if false > 20:
    desconto = preco_alc * 0.95
    preco = desconto * false
    print("O valor total é: " + preco)