import re
from tkinter import messagebox

def parse_price_filter(value):
    
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)

    s = str(value).strip()
    if not s:
        return None
    if s.lower().replace(" ", "") in ("semlimite", "sem_limite", "none"):
        return None

    # Pega último número na string (em caso de intervalos usa o maior)
    nums = re.findall(r'[\d]+', s)
    if not nums:
        return None

    try:
        return float(nums[-1])
    except ValueError:
        return None
    
def str_to_int(valor_str: str) -> int:
    try:
        valor_str = valor_str.replace(',', '.')
        return int(valor_str)
    except (ValueError, AttributeError):
        return 0.0

def validate_empty_fields(forms):
    if not forms["model"] or not forms["plate"] or not forms["year"]:
        messagebox.showwarning("Campos obrigatórios", "Por favor, preencha todos os campos antes de adicionar o carro.")
    else:
        return True

