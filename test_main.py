from main import es_mayor_de_edad


def test_mayor_positivo():
    assert es_mayor_de_edad(20)


def test_exacto():
    assert es_mayor_de_edad(18)


def test_menor():
    assert not es_mayor_de_edad(17)


def test_edad_negativa():
    assert not es_mayor_de_edad(-1)


def test_edad_cero():
    assert not es_mayor_de_edad(0)


def test_float_positivo():
    assert es_mayor_de_edad(18.5)


def test_float_menor():
    assert not es_mayor_de_edad(17.9)
