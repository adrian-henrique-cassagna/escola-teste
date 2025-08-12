import pytest
from escola.aluno import calcular_media

def test_calcular_media_lista_vazia():
    #entrada
    entrada = []
    #executando e esperando o erro da função
    with pytest.raises(ValueError, match="lista invalida\, lista vazia"):
        calcular_media(entrada)