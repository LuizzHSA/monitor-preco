from services.alerta_service import AlertaService

def iniciar_verificacao_precos():
    """
    Função que é executada periodicamente para verificar variações de preço
    e criar alertas automaticamente
    """
    print("Iniciando verificação automática de preços...")
    
    try:
        alertas_criados = AlertaService.verificar_variacoes_preco()
        print(f"Verificação concluída. {len(alertas_criados)} novos alertas criados.")
        
        for alerta in alertas_criados:
            print(f"Alerta criado: {alerta.mensagem}")
            
    except Exception as e:
        print(f"Erro durante verificação automática: {e}")

def verificar_precos_em_massa():
    """
    Função para verificar preços em massa (útil para execução manual)
    """
    print("Executando verificação em massa de preços...")
    
    try:
        alertas_criados = AlertaService.verificar_variacoes_preco()
        print(f"Verificação em massa concluída. {len(alertas_criados)} novos alertas criados.")
        
        for alerta in alertas_criados:
            print(f"Alerta criado: {alerta.mensagem}")
            
        return alertas_criados
        
    except Exception as e:
        print(f"Erro durante verificação em massa: {e}")
        return []