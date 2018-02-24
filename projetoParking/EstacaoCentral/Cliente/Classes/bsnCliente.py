import time
from EstacaoCentral.Utils.Classes import idiomas
import EstacaoCentral.Cliente.Forms.frmCliente as formCabecalho
from EstacaoCentral.Utils.Classes import utils

class _bsnCliente:

    def entradaInfNovoCliente(self):
        formCabecalho._frmCliente.cabecalhoCadNovoCliente('')

        dic = []
        print(idiomas._idiomas.mensPlaca)
        placa = (input().upper() + "%")
        x = placa.replace(' ', '')
        dic.append(x)
        print(idiomas._idiomas.mensPrimeiroNome)
        dic.append(input().upper() + "%")
        print(idiomas._idiomas.mensSobreNome)
        dic.append(input().upper() + "%")
        print(idiomas._idiomas.mensCPF)
        dic.append(input() + "%")
        print(idiomas._idiomas.mensTelefone)
        dic.append(input() + "%")
        print(idiomas._idiomas.mensModeloVeiculo)
        dic.append(input().upper() + "%")
        print(idiomas._idiomas.mensAnoVeiculo)
        dic.append(input() + "%")
        print(idiomas._idiomas.mensCliMensalista)
        dic.append(input().upper() + "%")
        dic.append('Cadastrado em ' + (time.strftime("%d %b %y") + "\n"))

        arq = open(utils._caminhoArqCadClientes+utils._arqCadClientes, 'a')
        arq.writelines(dic)
        arq.close()
        utils.utils.alertaArquivo(idiomas._idiomas.mensAtencao ,idiomas._idiomas.mensCadasFeitoComSucesso + time.strftime("%H:%M:%S"))

        formCabecalho._frmCliente.cabecalhoCadNovoCliente('')


    def recuperaPlaca(self):
        return input(idiomas._idiomas.mensPlaca).upper()

    def recuperaCadastro(nLinha):
        formCabecalho._frmCliente.cabecalhoConsultarCliente('')
        arq = open(utils._caminhoArqCadClientes + utils._arqCadClientes, 'r')
        if (nLinha == -1):
            print(idiomas._idiomas.mensCliNaoCadastrado)
        else:
            line = arq.readlines()[nLinha]
            placa, nome, sobreNome, cpf, tel, modelo, ano, tipo, dataCadastro = line.split("%", maxsplit=8)
            print(idiomas._idiomas.mensInfoPlaca, placa)
            print(idiomas._idiomas.mensPrimeiroNome, nome)
            print(idiomas._idiomas.mensSobreNome, sobreNome)
            print(idiomas._idiomas.mensCPF, utils.utils.fomataCPF(cpf, "CPF"))
            print(idiomas._idiomas.mensTelefone, utils.utils.fomataTel(tel, "Fixo"))
            print(idiomas._idiomas.mensModeloVeiculo, modelo)
            print(idiomas._idiomas.mensAnoVeiculo, ano)
            print(idiomas._idiomas.mensCliMensalista, tipo.upper())
            print(dataCadastro)

    def retornarDadosCliente(placa, inf): # antes de chamar esse método, garantir que o arquivo exista.
        arq = open(utils._caminhoArqCadClientes+utils._arqCadClientes, 'r')
        linha = int(utils.utils.checkLinhaRegistro(placa, utils._caminhoArqCadClientes, utils._arqCadClientes))
        if not(linha == -1):
            line = arq.readlines()[linha]  # Me tras a linha que o cliente esta
            placa, nome, sobreNome, cpf, tel, modelo, ano, tipo, dataCadastro = line.split("%", maxsplit=8)
        ret = 0
        if inf.__eq__('1'):
            ret = placa
        elif inf.__eq__('2'):
            ret = nome
        elif inf.__eq__('3'):
            ret = sobreNome
        elif inf.__eq__('4'):
            ret = cpf
        elif inf.__eq__('5'):
            ret = tel
        elif inf.__eq__('6'):
            ret = modelo
        elif inf.__eq__('7'):
            ret = ano
        elif inf.__eq__('8'):
            ret = tipo
        else:
            ret = dataCadastro
        return ret

    def verificarCadastradoCliente(placa):
        ret = 0
        if utils.utils.checkLinhaRegistro(placa, utils._caminhoArqCadClientes, utils._arqCadClientes) == -1:  # Verifica se a placa já está no banco de dados
            utils.utils.alertaArquivo(idiomas._idiomas.mensAtencao, idiomas._idiomas.mensCliNaoCadastrado)
            print("         "+ idiomas._idiomas.mensDesejaCadCli)
            print(idiomas._idiomas.mensSim, "             ", idiomas._idiomas.mensNao)
            resp = input()
            if resp == 1:
                _bsnCliente.entradaInfNovoCliente('') # Cadastro cliente na hora se usuário quiser
                ret = _bsnCliente.retornarDadosCliente(placa, '8') # devolvo a placa cacadastrada para função retornar
        else:
            ret = _bsnCliente.retornarDadosCliente(placa, '8')
        return ret

    def excluirCadastroCliente(placa):
        linha = []
        x = utils.utils.checkLinhaRegistro(placa, utils._caminhoArqCadClientes, utils._arqCadClientes)
        if x == -1:
            print(idiomas._idiomas.mensNaoHaComoExcluirCli)
        else:
            arq = open(utils._caminhoArqCadClientes+utils._arqCadClientes, 'r')
            teste = arq.readline()
            while teste != '':
                linha.append(teste)
                teste = arq.readline()
            arq.close()
            arq = open(utils._caminhoArqCadClientes+utils._arqCadClientes, 'w')
            for i in range(len(linha)):
                if i != x:
                    arq.write(linha[i])
            arq.close()
            utils.utils.alertaArquivo(idiomas._idiomas.mensAtencao, idiomas._idiomas.mensExluidoComSucesso)
