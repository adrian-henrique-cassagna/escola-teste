import pytest
from etapa.resultado import calcular_media_do_aluno


def teste_com_nota_vaxia():
    nota = ""

    with pytest.raises(ValueError, match = "Por favor, digite um valor válido"):
        calcular_media_do_aluno(nota)
 