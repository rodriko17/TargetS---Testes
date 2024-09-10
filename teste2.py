"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
"""

import random

faturamentos = []
for i in range(0,31):
    x = random.randint(0,99999)
    faturamentos.append(x)
    if i%7==0:
        faturamentos[i] = 0
        faturamentos[i-1] = 0


sem_faturamento = [num for num in faturamentos if num > 0]
media_total = 0
for num in sem_faturamento:
    media_total += num

media_total = media_total / len(sem_faturamento)
dias_com_maior_faturamento = [] 

for i in range(len(faturamentos)):
    if faturamentos[i] > media_total:
        dias_com_maior_faturamento.append(i)

print(f'Menor faturamento: {min(sem_faturamento)}')
print(f'Maior faturamento: {max(faturamentos)}')
print(f'Dias com maior faturamento: {'º, '.join(map(str,dias_com_maior_faturamento))}')