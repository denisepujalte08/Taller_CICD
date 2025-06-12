import pytest
from main import es_mayor_de_edad
from api import app


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


# Tests para la API Flask
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False  # Deshabilitar CSRF para tests
    with app.test_client() as client:
        yield client


def test_api_mayor_de_edad(client):
    """Test API endpoint para persona mayor de edad"""
    response = client.get('/mayor?edad=25')
    assert response.status_code == 200
    data = response.get_json()
    assert data['mayor_de_edad'] is True


def test_api_menor_de_edad(client):
    """Test API endpoint para persona menor de edad"""
    response = client.get('/mayor?edad=16')
    assert response.status_code == 200
    data = response.get_json()
    assert data['mayor_de_edad'] is False


def test_api_exactamente_18(client):
    """Test API endpoint para persona de exactamente 18 años"""
    response = client.get('/mayor?edad=18')
    assert response.status_code == 200
    data = response.get_json()
    assert data['mayor_de_edad'] is True


def test_api_sin_parametro_edad(client):
    """Test API endpoint sin parámetro edad (debería usar 0 por defecto)"""
    response = client.get('/mayor')
    assert response.status_code == 200
    data = response.get_json()
    assert data['mayor_de_edad'] is False


def test_api_edad_float(client):
    """Test API endpoint con edad decimal"""
    response = client.get('/mayor?edad=17.9')
    assert response.status_code == 200
    data = response.get_json()
    assert data['mayor_de_edad'] is False


def test_api_health_check(client):
    """Test endpoint de health check"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert data['service'] == 'edad-verificador'


def test_valores_extremos():
    """Test con valores extremos"""
    assert es_mayor_de_edad(100)  # Muy mayor
    assert not es_mayor_de_edad(-100)  # Negativo extremo
    assert es_mayor_de_edad(18.0)  # Float exacto
    assert not es_mayor_de_edad(17.999)  # Muy cerca pero menor
