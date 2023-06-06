pergunta1 = input("telefonou para a vitima? (sim)ou(nao): ")
pergunta2 = input("esteve no local do crime? (sim)ou(nao): ")
pergunta3 = input("mora perto da vitima? (sim)ou(nao):  ")
pergunta4 = input("devia para a vitima? (sim)ou(nao):  ")
pergunta5 = input("já trabalhou com a vitima? (sim)ou(nao): ")
soma = 0
if pergunta1 == ("sim"):
    soma = soma+1
if pergunta2 == ("sim"):
    soma = soma+ 1
if pergunta3 == ("sim"):
    soma = soma +1
if pergunta4 == ("sim"):
    soma = soma+1
if pergunta5 == ("sim"):
    soma = soma+1
if soma<2:
    print ("inocente")
elif soma == 2:
    print ("suspeito")
elif soma <= 4:
    print("cumplice")
else:
    print("assaltante")