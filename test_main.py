from par import es_mayor_de_edad


def test_mayor_positivo():
    assert es_mayor_de_edad(20)


def test_exacto():
    assert es_mayor_de_edad(18)


def test_menor():
    assert not es_mayor_de_edad(17)
    