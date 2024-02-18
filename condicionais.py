# if, elif, else

idade = 23
if idade >= 18:
    print("Pode beber")
else:
    print("Não pode beber")

nome = "Marcela"
if nome == "Marcela":
    print("Olá Marcela!")
if nome != "Marcela":
    print("Você não é a Marcela")

# utilizando o elif
nome_cachorro = "Tata"

if nome_cachorro == "Juju":
    print("Você deve tomar remédio")
elif nome_cachorro == "Tata":
    print("Você pode comer tomate")
else:
    print("Qual o seu nome?")