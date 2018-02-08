from EstacaoCentral.Utils.Classes import utils as arqs
import codecs

class _idiomas():

    if (arqs.utils.recuperarParametros(1) == '3'):
        arq = codecs.open(arqs._caminhoArqConfig + arqs._arqIdiomaEsp, 'rb', 'iso8859-1')
        line = arq.readlines()[0]
        mensAtencao, mensVlrCobrancaCadastrado, mensCliSemCadastro, mensCadNovoCliente, mensLocalizaCli, mensEntradaCli, \
        mensConsultaTempo, mensBaixaCliente, mensAjuda, mensConfigs, mensTodosCli, mensSair, mensOpValida, \
        mensPlaca, mensPrimeiroNome, mensSobreNome, mensCPF, mensTelefone, mensModeloVeiculo, mensAnoVeiculo, mensCliMensalista, mensCadasFeitoComSucesso, \
        mensCliNaoCadastrado, mensCPF, mensTelefone, mensInfoPlaca, \
        mensConfirmacao, confirmEncerrar, mensRefazUltOp, mensVoltMenuPrinc, mensNomeEmp, mensEndereco, mensCidade, mensVlrHora, mensVlrFracao, \
        menVlrMensalidade, mensVlrDiaria, mensIdioma, mensArqConfigParamOk, mensCliIncluidoComSucesso, mensArqConfigNaoParametrizado, mensOp, mensFechar, mensSim, mensNao, mensDesejaCadCli = line.split(
            "@", maxsplit=46)
    elif (arqs.utils.recuperarParametros(1) == '2'):
        arq = codecs.open(arqs._caminhoArqConfig + arqs._arqIdiomaEng, 'rb', 'iso8859-1')
        line = arq.readlines()[0]
        mensAtencao, mensVlrCobrancaCadastrado, mensCliSemCadastro, mensCadNovoCliente, mensLocalizaCli, mensEntradaCli, \
        mensConsultaTempo, mensBaixaCliente, mensAjuda, mensConfigs, mensTodosCli, mensSair, mensOpValida,  \
        mensPlaca, mensPrimeiroNome, mensSobreNome, mensCPF, mensTelefone, mensModeloVeiculo, mensAnoVeiculo, mensCliMensalista, mensCadasFeitoComSucesso, \
        mensCliNaoCadastrado, mensCPF, mensTelefone, mensInfoPlaca, \
        mensConfirmacao, confirmEncerrar, mensRefazUltOp, mensVoltMenuPrinc, mensNomeEmp, mensEndereco, mensCidade, mensVlrHora, mensVlrFracao, \
        menVlrMensalidade, mensVlrDiaria, mensIdioma, mensArqConfigParamOk, mensCliIncluidoComSucesso, mensArqConfigNaoParametrizado, mensOp, mensFechar, mensSim, mensNao, mensDesejaCadCli = line.split(
            "@", maxsplit=46)
    else:
        arq = codecs.open(arqs._caminhoArqConfig + arqs._arqIdiomaPtbr, 'rb', 'iso8859-1')
        line = arq.readlines()[0]
        mensAtencao, mensVlrCobrancaCadastrado, mensCliSemCadastro, mensCadNovoCliente, mensLocalizaCli, mensEntradaCli, \
        mensConsultaTempo, mensBaixaCliente, mensAjuda, mensConfigs, mensTodosCli, mensSair, mensOpValida, \
        mensPlaca, mensPrimeiroNome, mensSobreNome, mensCPF, mensTelefone, mensModeloVeiculo, mensAnoVeiculo, mensCliMensalista, mensCadasFeitoComSucesso, \
        mensCliNaoCadastrado, mensCPF, mensTelefone, mensInfoPlaca, \
        mensConfirmacao, confirmEncerrar, mensRefazUltOp, mensVoltMenuPrinc, mensNomeEmp, mensEndereco, mensCidade, mensVlrHora, mensVlrFracao, \
        menVlrMensalidade, mensVlrDiaria, mensIdioma, mensArqConfigParamOk, mensCliIncluidoComSucesso, mensArqConfigNaoParametrizado, mensOp, mensFechar, mensSim, mensNao, mensDesejaCadCli = line.split(
            "@", maxsplit=46)

