# Programa de Cálculo de Consumo de Energia Elétrica
# Autor: Alexandre Mota


# Entrada

aparelho = input ("Digite o nome do aparelho: ")
potencia = float(input ("Digite a potência do aparelho em watts: "))
tempo = float(input ("Digite o tempo médio de uso diário em horas: "))

# Processamento

consumo = (potencia * tempo * 30) / 1000
custo = (consumo * 0.787) 

# Saída

print(f"Aparelho: {aparelho}")
print(f"Consumo Estimado: {consumo:.2f} kWh/mês.")
print(f"Custo Estimado: R$ {custo:.2f} por mês.")
