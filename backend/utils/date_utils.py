from datetime import datetime, date, timedelta
import calendar

def get_data_inicio_mes():
    hoje = date.today()
    return date(hoje.year, hoje.month, 1)

def get_data_fim_mes():
    hoje = date.today()
    ultimo_dia = calendar.monthrange(hoje.year, hoje.month)[1]
    return date(hoje.year, hoje.month, ultimo_dia)

def formatar_data(data):
    if data:
        return data.strftime('%Y-%m-%d %H:%M:%S')
    return None

def formatar_data_somente_data(data):
    if data:
        return data.strftime('%Y-%m-%d')
    return None

def get_data_relativa dias):
    return datetime.utcnow() - timedelta(days=dias)

def eh_data_valida(data_str, formato='%Y-%m-%d'):
    try:
        datetime.strptime(data_str, formato)
        return True
    except ValueError:
        return False