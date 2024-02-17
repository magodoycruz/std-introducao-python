# Declaração e acesso de posição específica
minha_lista = [1, 2, 3, 4, 5]
minhas_informacoes = ["Marcela", 35, True]
print(minhas_informacoes[0])

# Extrair uma parte da lista - slice
print(minhas_informacoes[0:2]) # Valor inicial e valor a partir "do qual "cortar"da exclusão"

# Extraindo do começo ao alvo
print(minha_lista[:3]) # [1, 2, 3]

# Extraindo de um elemento especifico ao final
print(minha_lista[3:]) # [4, 5]

### Métodos de Lista

# Adiciona um elemento ao final da lista - append()
minhas_informacoes.append("Desenvolvedora")
print(minhas_informacoes)

# Retorna o indice de um elemento - index()
print(minhas_informacoes.index(35)) # minhas_informacoes[1]

# Insere um elemento em um item específico - insert()
minhas_informacoes.insert(3, "Salto")
print(minhas_informacoes)

# Remove o elemento de um indice específico - pop()
item_removido = minhas_informacoes.pop(2)
print(item_removido)
print(minhas_informacoes)

# Remove o primeiro elemento com valor especificado - remove
minhas_informacoes.remove("Desenvolvedora")
print(minhas_informacoes)

# Organizar uma lista em ordem crescente (Deve ser uma lista numerica) - sort()
lista_numeros = [1, 5, 3, 7, 3, 8, 9]
lista_numeros.sort()
print(lista_numeros)