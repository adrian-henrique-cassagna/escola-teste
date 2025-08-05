import pytest
from escola.aluno import calcular_media

@pytest.mark.parametrize("entrada, situacao",
[
    ([0.0, 0.0 ,0.0, 0.0], 0),
    ([10.0, 10.0 ,10.0, 10.0], 10), 
    ([10.0], 10),
    ([10.0, 7.0, 9.0, 3.0, 6.0, 7.5, 8.75], 7.3),
    ([10.0, 9.0, 3.0, 7.5, 8.0], 7.5),
    ([0.8, 0.0, 0.0], 0.3),
    ([10, 5, 7, 2], 6)  
])

def test_calcular_media_calculos_basicos_parametrizados(entrada, situacao):
    resultado = calcular_media(entrada)
    assert resultado == situacao