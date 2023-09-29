def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"

# Solicita ao usuário que insira o peso e a altura
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

# Calcula o IMC
imc = calcular_imc(peso, altura)

# Classifica o IMC
classificacao = classificar_imc(imc)

# Exibe o resultado
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
