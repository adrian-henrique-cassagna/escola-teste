import pytest

def calcular_media_do_aluno(valor):

    if isinstance(valor, str):
        raise ValueError("Erro")

    elif valor > 7 or valor == 10:
        raise ValueError("passou")

    elif valor < 7 and valor > 5.6:
        raise ValueError("recuperação")

    elif valor < 5.7:
        raise ValueError("reprovado")

    return valor