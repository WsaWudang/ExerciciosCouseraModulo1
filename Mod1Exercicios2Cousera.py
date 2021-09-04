#Faça um programa em Python que receba quatro notas, calcule e imprima a média aritmética

nota_1 = int(input("Digite a primeira nota: \n"))
nota_2 = int(input("Digite a segunda nota: \n"))
nota_3 = int(input("Digite a terceira nota: \n"))
nota_4 = int(input("Digite a quarta nota: \n"))

soma = nota_1 + nota_2 + nota_3 + nota_4

media = soma / 4

print("A média aritmética é ",media)