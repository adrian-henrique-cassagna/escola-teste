from escola.aluno import calcular_media

def test_calcular_media_entrada_basica_sem_erro():
    #definindo a entrada
    entrada = [10.0, 5.0, 7.0, 2.0]

    #executo o codigo
    resultado = calcular_media(entrada)

    #checo a saida
    assert resultado == 6.0