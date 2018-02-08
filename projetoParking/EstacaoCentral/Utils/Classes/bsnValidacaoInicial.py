from EstacaoCentral.Utils.Classes import utils as arqs
from EstacaoCentral.Parametros.Classes import parametros
from EstacaoCentral.Parametros.Forms import frmParametros
from EstacaoCentral.Utils.Classes import idiomas

class _bsnValidacaoInicial: # Essa validação é somente no início, sendo assim, sempre inicia em portugues.

    def parametrizarConfiguracao(self):

            frmParametros._frmParametros.cabecalhoConfig('')

            config = []

            print(idiomas._idiomas.mensIdioma)
            _idioma = input()
            print(idiomas._idiomas.mensNomeEmp)
            _nomeEmpresa = input()
            print(idiomas._idiomas.mensCidade)
            _cidade = input()
            print(idiomas._idiomas.mensVlrHora)
            _vlrTaxaHora = input()
            print(idiomas._idiomas.mensVlrFracao)
            _vlrFracaoHora = input()
            print(idiomas._idiomas.mensVlrDiaria)
            _vlrDiaria = input()
            print(idiomas._idiomas.menVlrMensalidade)
            _vlrMensalidade = input()

            config.append(_idioma + '@')
            config.append(_nomeEmpresa + '@')
            config.append(_cidade + '@')
            config.append(_vlrTaxaHora + '@')
            config.append(_vlrFracaoHora + '@')
            config.append(_vlrDiaria + '@')
            config.append(_vlrMensalidade)

            arq = open(parametros._parametro._caminhoArqConfig + parametros._parametro._arqConfig, 'w')
            arq.writelines(config)
            arq.close()

            arqs.utils.alertaArquivo(idiomas._idiomas.mensAtencao,
                                     "\n" + idiomas._idiomas.mensArqConfigParamOk)
            exit()