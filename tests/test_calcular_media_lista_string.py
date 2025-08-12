import pytest
from escola.aluno import calcular_media

def test_calcula_media_eviando_uma_lista_de_string():
    entrada = ["oi", 30]

    with pytest.raises(ValueError, match="string dentro da lista\, não suportado"):
        calcular_media(entrada)

