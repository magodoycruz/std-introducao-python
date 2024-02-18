# Dicionario - Coleção não ordenada de pares chave => valor

pessoa = {"nome": "Marcela", "idade": 35, "cidade": "Salto"}

print(pessoa["nome"])

# Incluir um novo valor ou atualizar
pessoa["sobrenome"] = "Cruz"
print(pessoa)

pessoa["idade"] = 36
print(pessoa)

# Remoção de um elemento - del()
del pessoa["sobrenome"]
print(pessoa)

# Retorno de todas as chaves - keys()
chaves = list(pessoa.keys())
print(chaves)

# Retorno de todos os valores - values()
valores = list(pessoa.values())
print(valores)

# Retorna cada elemento como uma tupla chave->valor - items()
itens = list(pessoa.items())
print(itens)

# list() utilizado para transformar os retornos em listas, para podermos manipular as informações retornadas