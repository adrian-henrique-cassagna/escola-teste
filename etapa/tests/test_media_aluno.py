import pytest
from etapa.resultado import calcular_media_do_aluno


def test_com_nota_string():
    nota = ""

    with pytest.raises(ValueError, match = "Por favor, digite um valor válido"):
        calcular_media_do_aluno(nota)

def test_com_nota_alta():
    nota = 9

    with pytest.raises(ValueError, match = "passou"):
        calcular_media_do_aluno(nota)

def test_com_nota_baixa():
    nota = 5.7

    with pytest.raises(ValueError, match = "recuperação"):
        calcular_media_do_aluno(nota)

def test_com_nota_reprovado():
    nota = 2

    with pytest.raises(ValueError, match = "reprovado"):
        calcular_media_do_aluno(nota)