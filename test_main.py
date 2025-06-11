from main import es_mayor_de_edad

def test_mayor_edad():
    assert es_mayor_de_edad(20)

def test_menor_edad():
    assert not es_mayor_de_edad(17)

def test_limite_exacto():
    assert es_mayor_de_edad(18)

def test_limite_inferior():
    assert not es_mayor_de_edad(0)

def test_negativo():
    assert not es_mayor_de_edad(-5)

def test_grande():
    assert es_mayor_de_edad(120)
