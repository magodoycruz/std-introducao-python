print('Exemplo de captura de exceções')

try:
    numero = int(input('Digite um numero inteiro: '))
    resultado = 10/numero

# Erro de valor inesperado
except ValueError as e:
    print(f"Erro de value: {e}")
    raise ValueError("Tipos de variáveis incompatíveis") #Interrompe o programa
except Exception as e:
    print(f"Erro: {e}")

else: #Caso tenha funciona
    print(f"resultado: {resultado}")
    
finally: #Executa mesmo se houver erro da exceção
    print("Operação finalizada")