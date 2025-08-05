import pytest

def calcular_media(valor:list[float]) -> float:

    if not isinstance(valor,list):
        raise ValueError("isso não é uma lista")
    if len(valor) == 0:
        raise ValueError("lista invalida, lista vazia")

    soma = 0
    divisao = len(valor)
    for i in valor:
        soma+=i
        print(soma/divisao);
    return float("{:.1f}".format(soma/divisao));
