print("Calculadora em python")

numero1 = float(input("Digite o primeiro numero :"))
numero2 = float(input("Digite o segundo numero :"))

print ("1 - somar")
print ("2 - subtrair")
print ("3 - multiplicação")
print ("4 - divisão")

opcao = input("Escolha uma opção :")

if opcao == "1":
    resultado = numero1 + numero2
    print ("Resultado :", resultado)

elif opcao == "2":
    resultado = numero1 - numero2
    print ("Resultado :", resultado)

elif opcao == "3":
    resultado = numero1 * numero2
    print("Resultado :", resultado)

elif opcao == "4":
    resultado = numero1 / numero2
    print("Resultado :", resultado)

else:
    print("Opção invalida")



