"""
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
"""

def fibonacci(v):
    valores = [0,1]
    p=False
    for i in range(2,v+5):
        n = valores[i-1] + valores[i-2]
        valores.append(n)
    
    for i in valores:
        if i == v:
            return True
    return False


valor = int(input('Digite um valor: '))
print(f'O valor {valor} Pertence a Sequencia de Fibonacci' if fibonacci(valor) else f'O valor {valor} Nao Pertence a Sequencia de Fibonacci')
