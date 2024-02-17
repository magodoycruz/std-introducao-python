# Métodos do tipo string
nome = "Marcela"
sobrenome = "Godoy"
nome_completo = "Marcela Godoy"

# Deixando a string em caixa alta
print(nome.upper())

# Deixando a string toda em caixa baixa
print(nome.lower())

# Buscando por caracter em posição específica na string
print(nome[0])

# Conta a quantidade de ocorrencias de um caracter em uma string
print(nome_completo.count("a"))

# Localiza o indice da primeira vez que caracter aparece na string
print(nome_completo.find("a"))
print(nome_completo.find("b")) # não existe o caracter, retornando -1

# Transforma string em bites
print(nome.encode())

# Traz de bites para string
print(nome.encode().decode()) 

# Substituição de caracteres em uma string
print(nome_completo.replace("a", "4"))

# Adiciona um separador a cada caracter da string
print("-".join(nome))

# Dividir uma string em lista com base em um caracter alvo
print(nome_completo.split(" "))

# Remove caracteres das extremidades (primeiro e ultimo caracter) que correspondem a um valor alvo
texto_markdown = "**Aqui está um texto em destaque**"
print(texto_markdown.strip("**"))
print(texto_markdown.rstrip("**")) # Remove apenas o ultimo
print(texto_markdown.lstrip("**")) # Remove apenas o primeiro

###### Comparadores - Retornam Boolean

# Verifica se string começa com o valor esperado
print(nome_completo.startswith("Ma"))

# Existe a ocorrencia dentro da string a ser comparada
print("Go" in nome_completo)

# Não existe a ocorrencia dentro da string a ser comparada
print("Go" not in nome_completo)