from src.payment import calcular_total

def test_calcular_total_com_desconto():
    assert calcular_total(100, 0.1) == 90

def test_calcular_total_sem_desconto():
    assert calcular_total(100, 0) == 100
