import pytest
from escola.aluno import calcular_media

def test_calcula_media_eviando_uma_lista_com_numero_negativo():
    entrada = [-10, 9, 8]

    with pytest.raises(ValueError, match="não suportado\, numero negativo"):
        calcular_media(entrada)

