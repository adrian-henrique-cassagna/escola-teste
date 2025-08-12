import pytest
from escola.aluno import calcular_media

def test_calcula_media_eviando_um_numero_maior_que_dez():
    entrada = [11, 12, 9, 5]

    with pytest.raises(ValueError, match="numero tem que ser menor ou igual a 10"):
        calcular_media(entrada)