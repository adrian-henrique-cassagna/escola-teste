import pytest

def calcular_media_do_aluno(valor):

    if isinstance(valor, str):
        print("erro")

    if valor > 7 or valor == 10:
        print("aprovado")

    if valor < 7 or valor == 5.7:
        print("recuperação")

    if valor < 5.7:
        print("reprovado")

    return valor

calcular_media_do_aluno()