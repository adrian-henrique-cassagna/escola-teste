import pytest
from etapa.resultado import calcular_media_do_aluno

def calcular_media(valor:list[float]) -> float:
    """"
    calcula a media de uma lista de notas

    parametros:
    nota(list[float]): lista de nota a serem calculadas

    retorna:
    float: a media das notas, arredonda para uma casa decimal

    """
    if not isinstance(valor, list):
        raise TypeError("não e uma lista, tipo não suportado (String)")
    if len(valor) == 0:
        raise ValueError("lista invalida, lista vazia")
    
    for i in valor:
        if isinstance(i, str):
            raise ValueError("string dentro da lista, não suportado")
        elif i < 0:
            raise ValueError("não suportado, numero negativo")
        elif i > 10:
            raise ValueError("numero tem que ser menor ou igual a 10")
        
    soma = 0
    divisao = len(valor)
    for l in valor:
        soma+=l
    r = soma/divisao
    return float("{:.1f}".format(r))