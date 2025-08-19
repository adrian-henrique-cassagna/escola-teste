import pytest
from etapa.resultado import calcular_media_do_aluno


def test_com_nota_string():
    nota = ''

    with pytest.raises(ValueError, match = "Erro"):
        calcular_media_do_aluno(nota)

def test_com_nota_alta():
    nota = 9.0

    with pytest.raises(ValueError, match = "passou"):
        calcular_media_do_aluno(nota)

def test_com_nota_baixa():
    nota = 6.0

    with pytest.raises(ValueError, match = "recuperação"):
        calcular_media_do_aluno(nota)

def test_com_nota_reprovado():
    nota = 2.0

    with pytest.raises(ValueError, match = "reprovado"):
        calcular_media_do_aluno(nota)