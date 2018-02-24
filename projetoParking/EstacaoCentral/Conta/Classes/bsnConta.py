from EstacaoCentral.EntradaSaida.Classes import bsnEntradaSaida
from EstacaoCentral.Utils.Classes import utils
from EstacaoCentral.Utils.Classes import idiomas

class conta:
    def totalAPagar(placa):

        tempo = bsnEntradaSaida.entradaSaida.retornaTempoNoEstacionamento(placa)
        dias, horas, min, mens = tempo.split("@", maxsplit=3)
        dias = int(dias)
        horas = int(horas)
        min = int(min)

        vlrDias = int(utils.utils.recuperarParametros(7))
        vlrHora = int(utils.utils.recuperarParametros(2))
        vlrFrac = int(utils.utils.recuperarParametros(3))

        valorTotal = ((dias*vlrDias)+(horas*vlrHora)+(min*vlrFrac))

        mensagemConta = idiomas._idiomas.mensTotalConta + str(valorTotal)
        utils.utils.alertaArquivo(idiomas._idiomas.mensAtencao, mensagemConta)