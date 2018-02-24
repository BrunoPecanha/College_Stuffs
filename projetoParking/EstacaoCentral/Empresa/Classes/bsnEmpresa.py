from EstacaoCentral.Utils.Classes import utils
from EstacaoCentral.Utils.Classes import idiomas

class _bsnEmpresa:

    def recuperaDadosEmpresa(menu):
        # from projEstacionamento.mensagens import classMensagens as msgs

        try:
            open(utils._caminhoArqConfig+utils._arqConfig,'r')
        except:
            open(utils._caminhoArqConfig+utils._arqConfig,'w')
            utils.utils.alertaArquivo(idiomas._idiomas.mensAtencao, idiomas._idiomas.mensArqConfigNaoParametrizado)
            #alerts.alerts.alertaArquivo("Teste", "Mensagem")  # msgs._mensagens._msg01, msgs._mensagens._msg40)
            #configuracao.confuracaoes('')

        arq = open(utils._caminhoArqConfig + utils._arqConfig,  'r')
        config = arq.readlines()[0]
        nomeEmp, endEmp, cidadeEmp, vlrTx, vlrFrac, vlrMens, idioma, vlrDiaria = config.split("@", maxsplit=7)
        ret = 0
        if menu.__eq__(1):
            ret = nomeEmp
        elif menu.__eq__(2):
            ret = endEmp
        elif menu.__eq__(3):
            ret = cidadeEmp
        elif menu.__eq__(4):
            ret = vlrTx
        elif menu.__eq__(5):
            ret = vlrFrac
        elif menu.__eq__(6):
            ret = vlrMens
        elif menu.__eq__(7):
            ret = idioma
        else:
            ret = vlrDiaria
        return ret