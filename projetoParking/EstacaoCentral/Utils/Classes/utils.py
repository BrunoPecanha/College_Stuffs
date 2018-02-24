import datetime as data
import tkinter as tk
from tkinter import messagebox
from EstacaoCentral.Parametros.Forms import frmParametros

_caminhoArqConfig = "C:/Users\Ramilson\Dropbox\Sistemas de Informação\Programação\Trabalho\projetoParking\EstacaoCentral\Arquivos\configuracao"
_caminhoArqRegEntSai = "C:/Users\Ramilson\Dropbox\Sistemas de Informação\Programação\Trabalho\projetoParking\EstacaoCentral\Arquivos/regEntSaida"
_caminhoArqMenuAjuda = "C:/Users\Ramilson\Dropbox\Sistemas de Informação\Programação\Trabalho\projetoParking\EstacaoCentral\Arquivos/help"
_caminhoArqCadClientes = "C:/Users\Ramilson\Dropbox\Sistemas de Informação\Programação\Trabalho\projetoParking\EstacaoCentral\Arquivos/clientes"
_arqConfig = "/configs"+".txt"
_arqCadClientes = "/cadastroClientes"+".txt"
_arqRegEntSai = "/registroEntradaSaida"+".txt"
_arqMenuAjuda = "/menuAjuda"+".txt"
_arqIdiomaEng = "/eng"+".txt"
_arqIdiomaPtbr = "/pt-BR"+".txt"
_arqIdiomaEsp = "/esp"+".txt"

class utils:

    def verificarArq(caminhoArq, nomeArq):
        ret = False
        try:
            open(caminhoArq + "/" + nomeArq, 'r')
            ret = True
        except:
            open(caminhoArq + "/" + nomeArq, 'w')
            ret = False
        return ret

    def checkLinhaRegistro(placa, caminhoArq, nomeArq):  # Devolve a linha que o cliente foi encontrado
        from EstacaoCentral.Cliente.Classes import bsnCliente as cliente
        while len(placa) != 7:
            placa = cliente._bsnCliente.recuperaPlaca('')
        i = 0
        utils.verificarArq(caminhoArq, nomeArq)
        arq = open(caminhoArq + nomeArq, 'r')
        linha = arq.readline()
        while linha != '':
            x = linha.find(placa, 0, 7)
            if x != -1:
                break
            else:
                i = i + 1
                linha = arq.readline()
        if x != -1:
            ret = i
        else:
            ret = x
        return ret

    def fomataCPF(nums, tipo):
        ret = "%s.%s.%s-%s" % (nums[:3], nums[3:6], nums[6:9], nums[9:])
        return ret
    def fomataCNPJ(nums, tipo):
        ret = "%s.%s.%s/%s-%s" % (nums[0:2], nums[2:5], nums[5:8], nums[8:12], nums[12:14])
        return ret
    def fomataTel(nums, tipo):
        if len(nums) == 8: # Formatacao Telefone Fixo
            ret = "%s-%s" % (nums[0:4], nums[4:8])
        else: # Fomatação Celular
            ret = "%s %s-%s" % (nums[0:2], nums[2:7], nums[7:])
        return ret
    def recuperaDiaHora(self):
        return (data.datetime.now().strftime("%d-%m-%Y %H:%M:%S"'\n'))

    def alertaArquivo(cabecalho, mensagem):
        root = tk.Tk()  # Instancia a classe e associa a root.
        root.withdraw()  # Retira o form padrão que aparece ao fundo junto com a mensagem..
        root.attributes("-topmost", True)  # Trás o form de alerta para a frente.
        tk.messagebox.showinfo(cabecalho, mensagem)



    # def alertPerg(cabecalho, mensagem): # Não sei porque não funciona...
    #     ret = False
    #     root = tk() # Instancia a classe e associa a root.
    #     root.withdraw()  # Retira o form padrão que aparece ao fundo junto com a mensagem..
    #     root.attributes("-topmost", True)  # Trás o form de alerta para a frente.
    #     if root.messagebox.askyesno(cabecalho, mensagem, icon='warning'):
    #         ret = True
    #     return ret

    def mostraInstrucoes(self):
        f = open(_caminhoArqMenuAjuda + _arqMenuAjuda, 'r')
        arq = f.readlines()
        for linha in arq:
            print(linha)
        f.close()

    def criarEstrutura(self):

        __caminho1 = "C:/Users\Ramilson\Dropbox\Sistemas de Informação\Programação\Trabalho\projetoParking\EstacaoCentral\Arquivos/configuracao"
        __caminho2 = "C:/Users\Ramilson\Dropbox\Sistemas de Informação\Programação\Trabalho\projetoParking\EstacaoCentral\Arquivos/regEntSaida"
        __caminho3 = "C:/UsersRamilson\Dropbox\Sistemas de Informação\Programação\Trabalho\projetoParking\EstacaoCentral\Arquivos/help"
        __caminho4 = "C:/Users\Ramilson\Dropbox\Sistemas de Informação\Programação\Trabalho\projetoParking\EstacaoCentral\Arquivos/clientes"

        caminhos = [__caminho1, __caminho2, __caminho3,__caminho4]  # Crio uma lista com todos os caminhos que vou usar.


    def recuperarParametros(menu): #Garantir que o arquivo existe antes de chamar esse método.
        try:
            open(_caminhoArqConfig + _arqConfig, 'r').readlines()[0]
        except:
            frmParametros._frmParametros.cabecalhoConfig('')
            utils.alertaArquivo('Atenção', 'Arquivo de configuração não encontrado. \n' + '          '
                                                                                               '                  ' + 'Por favor,  realize a parametrização agora')
            config = []
            print('Idioma: 1 - Portugues | 2 - Ingles | 3 - Espanhol: ')
            _idioma = input()
            print('Nome Empresa - Maximo 15 caracteres: ')
            _nomeEmpresa = input()
            print('Cidade: ')
            _cidade = input()
            print('Valor Hora: ')
            _vlrTaxaHora = input()
            print('Valor Fracao Hora: ')
            _vlrFracaoHora = input()
            print('Valor da Diaria: ')
            _vlrDiaria = input()
            print('Valor Mensal: ')
            _vlrMensalidade = input()

            config.append(_idioma + '@')
            config.append(_nomeEmpresa + '@')
            config.append(_cidade + '@')
            config.append(_vlrTaxaHora + '@')
            config.append(_vlrFracaoHora + '@')
            config.append(_vlrDiaria + '@')
            config.append(_vlrMensalidade)

            arq = open(_caminhoArqConfig + _arqConfig, 'w')
            arq.writelines(config)
            arq.close()

            utils.alertaArquivo('Atenção',
                                     'Arquivo de configuração parametriazado com sucesso ! \n' + '          '
                                                                                                 '        ' + 'Finalizando aplicação para carregar novas configurações')
            exit()

        arq = open(_caminhoArqConfig + _arqConfig, 'r')
        param = arq.readlines()[0]
        idioma, nomeEmpresa, cidade, vlrHora, vlrFrac, vlrMens, vlrDiaria = param.split("@", maxsplit=7)
        ret = 0
        if menu.__eq__(1):
            ret = idioma
        elif menu.__eq__(2):
            ret = vlrHora
        elif menu.__eq__(3):
            ret = vlrFrac
        elif menu.__eq__(4):
            ret = vlrMens
        elif menu.__eq__(5):
            ret = nomeEmpresa[:15]
        elif menu.__eq__(6):
            ret = cidade
        elif menu.__eq__(7):
            ret = vlrDiaria
        return ret

    def finalizarApp(self):
        from EstacaoCentral.Utils.Classes import idiomas
        ret = False
        print("           ", idiomas._idiomas.mensFechar)
        print(idiomas._idiomas.mensSim, "                                          ", idiomas._idiomas.mensNao)
        resp = eval(input())
        if resp == 1:
            ret = True
        return ret
