import locale # Módulo nativo para formatação de padrões de um país

def calculo_folha():
    
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') # Define a configuração regional para BR

    nome_funcinario = input("Informe seu nome: ")
    horas_trabalhadas_semana = int(input("Informe horas trbalhadas na semana: "))
    horas_trabalhadas_normais = int(input("Informe suas horas normais da semana: "))
    valor_hora_normal = float(input("Informe valor da hora normal: "))
    
    print(f"\nNome do funcionário: {nome_funcinario} Horas trabalhadas na semana: {horas_trabalhadas_semana} Valor do horário: {valor_hora_normal}")
    
    if horas_trabalhadas_semana > horas_trabalhadas_normais:
        print(f"[COMUNICADO] Seu horário ultrapassou às {horas_trabalhadas_normais} horas semanais adicional de 50%")
        
        calculo_horas_normais = horas_trabalhadas_normais * valor_hora_normal      
        horas_extras_trabalhadas = horas_trabalhadas_semana - horas_trabalhadas_normais
        horas_extras_com_adicional = valor_hora_normal * 1.5
        pagamento_horas_extras = horas_extras_trabalhadas * horas_extras_com_adicional
        salario_semana_total = calculo_horas_normais + pagamento_horas_extras
                  
        calculo_horas_normais_formatado = locale.currency(calculo_horas_normais, grouping=True) # Formata o valor como moeda
        horas_extras_com_adicional_formatado = locale.currency(horas_extras_com_adicional, grouping=True) 
        pagamento_horas_extras_formatado = locale.currency(pagamento_horas_extras, grouping=True)
        salario_semana_total_formatado = locale.currency(salario_semana_total, grouping=True)
        
        print(f"\nCalculo de horas normais: R$ {calculo_horas_normais_formatado}")
        print(f"Horas extras trabalhadas: {horas_extras_trabalhadas}")
        print(f"Horas extras com adicional de 50%: {horas_extras_com_adicional_formatado}")
        print(f"Valor das horas extras: R$ {pagamento_horas_extras_formatado}")
        print(f"Salário semanal total: R$ {salario_semana_total_formatado}")
        
    elif horas_trabalhadas_semana < horas_trabalhadas_normais:
        print("[COMUNICADO] Seu horário foi abaixo do horário semanal")

        

calculo_folha()        

     