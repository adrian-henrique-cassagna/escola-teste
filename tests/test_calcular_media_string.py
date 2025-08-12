import pytest
from escola.aluno import calcular_media

def test_calcula_media_eviando_uma_string():
    entrada = "ola"

    with pytest.raises(TypeError, match="não e uma lista\, tipo não suportado \(String\)"):
        calcular_media(entrada)

