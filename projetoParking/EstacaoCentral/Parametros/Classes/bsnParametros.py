from EstacaoCentral.Utils.Classes import idiomas as language
from EstacaoCentral.Utils.Classes import utils
from EstacaoCentral.Parametros.Forms import frmParametros
from EstacaoCentral.Parametros.Classes import parametros

class bsnParametros_:

    # def criarArqsIdioma(self):
    #     caractersEspeciais = d = ["ç", "á" "à", "ç" "ã"]
    #     arq = {}
    #     arq['language'] = []
    #     arq['language'].append({
    #         'atencao': 'ATTENTION',
    #         'ValorCobrancaCadastrado': 'There is no registered charge amount. \ N Please go to settings in option 7',
    #         'ClienteSemCadastro': '################### The Client does not have a Registration. Register now.',
    #         'op1': '1 - Registration of new customer.',
    #         'op2': '2 - Search customer registration.',
    #         'op3': '3 - New customer entry in the parking lot.',
    #         'op4': '4 - Check customer time in Parking.',
    #         'op5': '5 - Finish customer stay',
    #         'op6': '6 - Help.',
    #         'op7': '7 - Settings.',
    #         'op8': '8 - List all customers in the house',
    #         'op9': '9 - Exit',
    #         'opInvalida': 'A valid option was not entered. Try again.',
    #         'op': 'Operation: ',
    #         'placaCarro': 'Vehicle Plate: ',
    #         'primeiroNome': 'First Name: ',
    #         'sobreNome': 'Last Name : ',
    #         'cpf': 'Customer CPF - Numbers Only:',
    #         'telefone': 'Telephone - Only Numbers:',
    #         'modeloVeiculo': 'Vehicle Model:',
    #         'anoVeiculo': 'Year of Vehicle:',
    #         'cliMensalista': 'Monthly Customer (Y / N): ',
    #         'cadastroHora': '################################## Register successfully performed at',
    #         'cliNaoCadastrado': 'Customer Not Registered!',
    #         'cpf: ': 'CPF: ',
    #         'mostraTelefone': 'Telephone: ',
    #         'infPlaca': 'Informe plate:',
    #         'confirmacao': 'Confirmation',
    #         'confirmacaoEncerrar': 'Are you sure you want to exit?',
    #         'refUltimaOp': '1 - Redo the last operation',
    #         'voltarMenuPrincipal': '2 - Return to the home',
    #         'nomeEmpresa': 'Company Name:',
    #         'enderecao': 'Adress: ',
    #         'cidade': 'City : ',
    #         'vlrHora': 'Hour value',
    #         'vlrFracao': 'Fraction value:',
    #         'vlrMensa': 'Monthly Fee:',
    #         'vlrDiaria': 'Daily Value: ',
    #         'selecioneIdioma': 'Language: 1 - Portuguese | 2 - English | 3 - Spanish: ',
    #         'mensaParamOK': 'Configuration file parameterized successfully. Closing application to load the new settings!',
    #         'cliIncluidoAs': 'Customer Successfully Included at ',
    #         'mensArqNaoExistente': 'Configuration file not parameterized. Set it now.'
    #     })
    #
    #     with open(parametros._parametro._caminhoArqConfig+parametros._parametro._arqIdiomaEng, 'w') as arqSaida:
    #         json.dump(caractersEspeciais,arq, arqSaida, ensure_ascii=False)
    #
    #     arq = {}
    #     arq['language'] = []
    #     arq['language'].append({
    #         'atencao': 'ATENCION',
    #         'ValorCobrancaCadastrado': 'No hay valor de cobro registrado. \n Por favor, acceda a los ajustes en la opción 7',
    #         'ClienteSemCadastro': '####################### El cliente no tiene registro. Regístrate ahora.',
    #         'op1': '1 - Registro de nuevo cliente.',
    #         'op2': '2 - Buscar registro de cliente.',
    #         'op3': '3 - Entrada en nuevo cliente en el aparcamiento',
    #         'op4': '4 - Consultar tiempo de cliente en el aparcamiento.',
    #         'op5': '5 - Dar baja de cliente.',
    #         'op6': '6 - Ayuda.',
    #         'op7': '7 - Configuraciones.',
    #         'op8': '8 - Listar a todos los clientes en la casa',
    #         'op9': '9 - Salir',
    #         'opInvalida': 'No se ha introducido una opcion valida. Intentar nuevamente.',
    #         'op': 'Operacion: ',
    #         'placaCarro': 'Placa del vehiculo: ',
    #         'primeiroNome': 'Primer nombre: ',
    #         'sobreNome': 'Apellidos : ',
    #         'cpf': 'CPF Cliente - Solo Numeros:',
    #         'telefone': 'Telefono - Solo Numeros: ',
    #         'modeloVeiculo': 'Modelo del vehiculo: ',
    #         'anoVeiculo': 'Ano del vehiculo: ',
    #         'cliMensalista': 'Cliente Mensual (S / N): ',
    #         'cadastroHora': 'El registro efectuado con exito a las ',
    #         'cliNaoCadastrado': '¡No hay registro!',
    #         'cpf: ': 'CPF: ',
    #         'mostraTelefone': 'Telefono: ',
    #         'infPlaca': 'Introduzca la tarjeta: ',
    #         'confirmacao': 'Confirmacion',
    #         'confirmacaoEncerrar': '¿Está seguro de que desea cerrar?',
    #         'refUltimaOp': '1 - Rehacer la ultima operación',
    #         'voltarMenuPrincipal': '2 - Volver al menu de inicio',
    #         'nomeEmpresa': 'Nombre de la empresa:',
    #         'enderecao': 'Direccion: ',
    #         'cidade': 'Ciudad : ',
    #         'vlrHora': 'Valor de la hora: ',
    #         'vlrFracao': 'Valor de la fracción: ',
    #         'vlrMensa': 'Valor de la mensualidad: ',
    #         'vlrDiaria': 'Precio diario: ',
    #         'selecioneIdioma': 'Idioma: 1 - Portugues | 2 - Ingles | 3 - Espanhol: ',
    #         'mensaParamOK': 'Archivo de configuracion parametrizado con exito. Cierrando aplicacion para cargar las nuevas configuraciones!',
    #         'cliIncluidoAs': 'Cliente Incluido con exito a las ',
    #         'mensArqNaoExistente': 'Archivo de configuracion no parametrizado. Configure ahora.'
    #     })
    #
    #     with open(parametros._parametro._caminhoArqConfig+parametros._parametro._arqIdiomaEsp, 'w') as arqSaida:
    #         json.dump(caractersEspeciais, arq, arqSaida, ensure_ascii=False)
    #
    #     arq = {}
    #     arq['language'] = []
    #     arq['language'].append({
    #         'atencao': 'ATENCAO',
    #         'ValorCobrancaCadastrado': 'Nao existe valor de cobrança cadastrado. \n Por favor, acesse configuracoes na opcao 7',
    #         'ClienteSemCadastro': '################### O Cliente Nao Possui Cadastro. Cadastre-o agora.',
    #         'op1': '1 - Cadastro de novo cliente.',
    #         'op2': '2 - Localizar cadastro de cliente.',
    #         'op3': '3 - Entrada em novo cliente no Estacioanamento.',
    #         'op4': '4 - Consultar tempo de cliente no Estacionamento.',
    #         'op5': '5 - Dar baixa de cliente.',
    #         'op6': '6 - Ajuda.',
    #         'op7': '7 - Configurações.',
    #         'op8': '8 - Listar todos clientes na casa',
    #         'op9': '9 - Sair',
    #         'opInvalida': 'Não foi inserida uma opcao valida. Tentar novamente.',
    #         'op': 'Operacao: ',
    #         'placaCarro': 'Placa do Veiculo: ',
    #         'primeiroNome': 'Primeiro Nome: ',
    #         'sobreNome': 'Sobrenome : ',
    #         'cpf': 'CPF do Cliente - Somente Numeros: ',
    #         'telefone': 'Telefone - Somente Numeros: ',
    #         'modeloVeiculo': 'Modelo do Veiculo: ',
    #         'anoVeiculo': 'Ano do Veiculo: ',
    #         'cliMensalista': 'Cliente Mensalista (S/N): ',
    #         'cadastroHora': '################################## Cadastro efetuado com sucesso as ',
    #         'cliNaoCadastrado': 'Cliente Nao Cadastrado !',
    #         'cpf: ': 'CPF: ',
    #         'mostraTelefone': 'Telefone: ',
    #         'infPlaca': 'Informe a placa: ',
    #         'confirmacao': 'Confirmacao',
    #         'confirmacaoEncerrar': 'Tem certeza que deseja encerrar ?',
    #         'refUltimaOp': '1 - Refazer a ultima operacao',
    #         'voltarMenuPrincipal': '2 - Voltar para o menu inicial',
    #         'nomeEmpresa': 'Nome da Empresa: ',
    #         'enderecao': 'Endereco: ',
    #         'cidade': 'Cidade : ',
    #         'vlrHora': 'Valor da Hora: ',
    #         'vlrFracao': 'Valor da fracao: ',
    #         'vlrMensa': 'Valor da Mensalidade: ',
    #         'vlrDiaria': 'Valor diaria: ',
    #         'selecioneIdioma': 'Idioma: 1 - Portugues | 2 - Ingles | 3 - Espanhol: ',
    #         'mensaParamOK': 'Arquivo de configuracao parametrizado com sucesso. Encerrando aplicacao para carregar as novas configuracoes !',
    #         'cliIncluidoAs': 'Cliente Incluido com Sucesso as ',
    #         'mensArqNaoExistente': 'Arquivo de configuracao não parametrizado. Configure-o agora.'
    #     })
    #     with open(parametros._parametro._caminhoArqConfig+parametros._parametro._arqIdiomaPtbr, 'w') as arqSaida:
    #         json.dump(caractersEspeciais, arq, arqSaida, ensure_ascii=False

    def parametrizar(self):
        frmParametros._frmParametros.cabecalhoConfig('')
        config = []

        parametros._parametro._idioma = input(language._idiomas.mensIdioma)
        parametros._parametro.nomeEmpresa = input(language._idiomas.mensNomeEmp)
        parametros._parametro.cidade = input(language._idiomas.mensCidade)
        parametros._parametro._vlrTaxaHora = input(language._idiomas.mensVlrHora)
        parametros._parametro._vlrFracaoHora = input(language._idiomas.mensVlrFracao)
        parametros._parametro._vlrMensalidade = input(language._idiomas.mensVlrCobrancaCadastrado)
        parametros._parametro._vlrDiaria = input(language._idiomas.mensVlrCobrancaCadastrado)

        config.append(parametros._parametro._idioma + '@')
        config.append(parametros._parametro.nomeEmpresa + '@')
        config.append(parametros._parametro.cidade + '@')
        config.append(parametros._parametro._vlrTaxaHora + '@')
        config.append(parametros._parametro._vlrFracaoHora + '@')
        config.append(parametros._parametro._vlrMensalidade + '@')
        config.append(parametros._parametro._vlrDiaria)

        arq = open(parametros._parametro._caminhoArqConfig+parametros._parametro._arqConfig, 'w')
        arq.writelines(config)
        arq.close()
        utils.alerts.alertaArquivo(parametros._parametro.atencao, parametros._parametro.mensaParamOK)