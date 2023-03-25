dia = int(input("Qual seu dia de nascimento? "))
mes = int(input("Qual seu mês de nascimento? "))
ano = int(input("Qual seu ano de nascimento em 4 digitos? "))

print("Escolha o formato de exibição da data:")
print("1 – Data simples. Ex.: 10/08/1990")
print("2 – Data abreviada. Ex.: 10/ago/1990")
print("3 – Data completa. Ex.: 10 de agosto de 1990")
formato = int(input("Digite o código do formato desejado: "))

if formato == 1:
    print(f"{dia:02}/{mes:02}/{ano}")
elif formato == 2:
    meses = ["", "jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
    print(f"{dia:02}/{meses[mes]}/{ano}")
elif formato == 3:
    meses = ["", "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    print(f"{dia} de {meses[mes]} de {ano}")

# Solicita a data e hora
