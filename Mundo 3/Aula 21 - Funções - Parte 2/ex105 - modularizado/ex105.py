
import utils
def notas(*notas,sit=False):
    """

    :param notas: RECEBE N NOTAS dos alunos de uma turma
    :param sit: OPCIONAL - DEFINE SE SERÁ ADICIONADO A SITUAÇÃO DA TURMA AO DICIONARIO
    :return: Um dicionario com as informações da turma
    """
    boletim = dict()
    boletim['TOTnotas'] = len(notas)
    boletim['maiorNota'] = utils.maior(notas)
    boletim['menorNota'] = utils.menor(notas)
    boletim['mediaNotas'] = utils.media(notas)
    if sit:
        boletim['situação'] = utils.situacao(boletim['mediaNotas'])
    return boletim


print("-"*25)
print(notas(3.5,2.5,10,6.5,sit=True))
#help(notas)



