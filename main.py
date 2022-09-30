# ADS - 1º Semestre - Paradigmas de Linguagens de Programação em Python - Lista de Revisão – 1. Implemente um código capaz de ler as notas de um aluno (AV1 e AV2) e informar se ele está ou não aprovado na disciplina. Para isso, considere: Média >= 6 pontos = APROVADO. Média entre 4 e 5,9 = FINAL e Média menor que 4 pontos = REPROVADO. Para cada uma das situações, imprima uma mensagem na tela para que o aluno fique ciente.

# Apresentação do programa.

print('Seja bem-vindo(a) ao portal de notas.\n')

# Solicitação das notas, o modelo só solicita duas e para que sejam solicitadas mais notas será necessário que sejam feitas modificações. 

nota1 = (float(input('Digite a nota da Avaliação 1.:\n')))
nota2 = (float(input('Digite a nota da Avaliação 2.:\n')))

# Cálculo da média.

media = (nota1 + nota2) /2

# Resultado.

if media >= 6:
  print('Caro(a) aluno(a), sua média foi:',media,' pontos, você foi APROVADO(A).')

elif media < 5.9:
  print('Caro(a) aluno(a), sua média foi:', media,'pontos, você foi para FINAL.' )

elif media < 4: 
  print('Caro(a) aluno(a) você foi REPROVADO(A).')