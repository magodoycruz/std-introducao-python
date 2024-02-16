# Declaração
nome_completo = "Marcela Godoy"

texto_completo_aspas = """Marcela
Com quebra
De linha"""

nome_completo_quebra = "Marcela \
Godoy"

nome = "Marcela"
sobrenome = "Godoy"

nome_completo_concatenado = nome +" "+ sobrenome
print(nome_completo_concatenado)

# Formatação
print("Nome:", nome_completo) # Garante espaçamento entre itens de concatenação
print("Nome:" + nome_completo) # Necessário incluir espaço para concatenar
print("Nome:" + "Marcela" + "Godoy")
print("Nome: %s %s" % (nome, sobrenome)) # Considerada a mais "Segura" em relação a tipagem
print(f"Nome Completo: {nome} {sobrenome}")
print("Nome Completo: {} {}".format(nome, sobrenome))