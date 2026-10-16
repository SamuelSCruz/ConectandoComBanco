# 1. Função de Leitura (Apenas lê e retorna o valor)
def ler_temperatura():
    temperatura = float(input("Informe a temperatura atual do ambiente (°C): "))
    return temperatura


# 2. Função de Processamento (Analisa e retorna um "status" ou "mensagem")
def analisar_temperatura(temp_atual):
    # Definindo os limites do sistema embarcado
    limite_minimo = 18.0
    limite_maximo = 26.0
    
    # Lógica condicional para definir a ação
    if temp_atual < limite_minimo:
        return "Aquecendo..."
    elif temp_atual > limite_maximo:
        return "Resfriando..."
    else:
        return "Temperatura estável."


# 3. Função de Exibição (Apenas mostra o resultado final)
def exibir_resultado(mensagem_acao):
    print("\n[STATUS DO SISTEMA]")
    print(mensagem_acao)


# --- FUNÇÃO PRINCIPAL (Gerencia o fluxo do programa) ---
def main():
    # Passo 1: Lê a temperatura e guarda o valor retornado
    temp = ler_temperatura()
    
    # Passo 2: Passa a temperatura para análise e guarda a resposta
    resultado = analisar_temperatura(temp)
    
    # Passo 3: Passa a resposta para ser exibida na tela
    exibir_resultado(resultado)


# Executa o programa
main()
