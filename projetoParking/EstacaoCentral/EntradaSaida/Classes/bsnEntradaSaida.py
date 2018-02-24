import time
import datetime
from EstacaoCentral.Cliente.Classes import bsnCliente as _bsnCliente
from EstacaoCentral.Cliente.Forms import frmCliente as formCabecalho
from EstacaoCentral.EntradaSaida.Form import frmEntradaSaida
from EstacaoCentral.Utils.Classes import utils
from EstacaoCentral.Utils.Classes import idiomas
from EstacaoCentral.Conta.Classes import bsnConta

class entradaSaida:

    def entrada(self):
        formCabecalho._frmCliente.cabecalhoEntradaCliente('')  # Escreve o cabeçalho do menu

        utils.utils.verificarArq(utils._caminhoArqRegEntSai, utils._arqRegEntSai)
        placa = _bsnCliente._bsnCliente.recuperaPlaca('')
        if utils.utils.checkLinhaRegistro(placa, utils._caminhoArqRegEntSai, utils._arqRegEntSai) != -1:
            utils.utils.alertaArquivo(idiomas._idiomas.mensAtencao, idiomas._idiomas.mensCarroJaNoEstacionamento)
        elif (_bsnCliente._bsnCliente.verificarCadastradoCliente(placa.upper()) == 0):  # Se o usuário não quis cadastrar, ele retorna 0
             tipoCostumer = 'N'  # Mas dá entrada assim mesmo como Não Mensalista
        else:
             tipoCostumer = _bsnCliente._bsnCliente.verificarCadastradoCliente(placa.upper())  # Do contrário ele devolve a placa

             dadosEntrada = []
             dadosEntrada.append(placa.upper() + '@')
             dadosEntrada.append(time.strftime("%d-%m-%Y") + '@')
             dadosEntrada.append(time.strftime("%H:%M") + '@')
             dadosEntrada.append(str(tipoCostumer) + "\n")
             arq = open(utils._caminhoArqRegEntSai + utils._arqRegEntSai, 'a')
             arq.writelines(dadosEntrada)
             arq.close()
             print(idiomas._idiomas.mensCliIncluidoComSucesso + utils.utils.recuperaDiaHora(''))

    def baixaCliente(placa):
        linha = []
        x = utils.utils.checkLinhaRegistro(placa, utils._caminhoArqRegEntSai, utils._arqRegEntSai)
        if x == -1:
            print(idiomas._idiomas.mensNaoHaComoExcluirCli)
        else:
            bsnConta.conta.totalAPagar(placa)
            arq = open(utils._caminhoArqRegEntSai + utils._arqRegEntSai, 'r')
            teste = arq.readline()
            while teste != '':
                linha.append(teste)
                teste = arq.readline()
            arq.close()
            arq = open(utils._caminhoArqRegEntSai + utils._arqRegEntSai, 'w')
            for i in range(len(linha)):
                if i != x:
                    arq.write(linha[i])
            arq.close()

    def iniciaBaixaCliente(self):
        frmEntradaSaida._frmEntradaSaida.cabecalhoEntradaSaidaliente('')
        print(idiomas._idiomas.mensPlaca)
        ret = input().upper()
        entradaSaida.baixaCliente(ret)

    def calculaDiferencaTempo(dataEntrada, dataSaida, tempoEntrada, tempoSaida):
        dataEntrada, mesEntrada, anoEntrada  = dataEntrada.split("-", maxsplit=2)
        dataSaida, mesSaida, anoSaida = dataSaida.split("-", maxsplit=2)
        horaEntrada, minutosEntrada = tempoEntrada.split(":", maxsplit=1)
        horaSaida, minutosSaida = tempoSaida.split(":", maxsplit=1)

        qtdDias = int(dataSaida)-int(dataEntrada)

        if qtdDias > 0: # Regra se o carro ficou mais de um dia
            return (str(qtdDias)+"@"+horaSaida+"@"+minutosSaida)

        elif (int(horaSaida) > int(horaEntrada)): # Regra se o carro ficou mais de uma hora
            horas = int(horaSaida) - int(horaEntrada)
            minutos = minutosSaida
            return (str(qtdDias)+"@"+str(horas)+"@"+str(minutos))
        else:  # Regra se o carro ficou alguns minutos, ou seja, a fração de hora
            return str(qtdDias)+"@"+str(int(horaSaida)-int(horaEntrada))+"@"+str((int(minutosSaida)-int(minutosEntrada)))

    def retornaTempoNoEstacionamento(placa):
        #frmEntradaSaida._frmEntradaSaida.cabecalhoConsultaTempoCliente('')
        arq = open(utils._caminhoArqRegEntSai + utils._arqRegEntSai, 'r')
        ret = utils.utils.checkLinhaRegistro(placa, utils._caminhoArqRegEntSai, utils._arqRegEntSai)
        if ret != -1:
            linha = arq.readlines()[ret]
            placa, data, horaEntrada, mensalista = linha.split("@", maxsplit=3)
            horaSaida = datetime.datetime.now().strftime('%H:%M')

            tempoUsado = entradaSaida.calculaDiferencaTempo(data, time.strftime("%d-%m-%Y"), horaEntrada, horaSaida)
            dias, horas, min = tempoUsado.split("@", maxsplit=2)
            #saidaTempo = str("Tempo Decorrido: " + "\n" + "Dias: "+ dias + "\n" + "Horas: " + horas + "\n" + "Minutos: " + min)
            #utils.utils.alertaArquivo(idiomas._idiomas.mensAtencao, saidaTempo)
            return (tempoUsado+"@"+mensalista)
        else:
            utils.utils.alertaArquivo(idiomas._idiomas.mensAtencao,  idiomas._idiomas.mensCliNaoCadastrado)
            return -1

    def TempoClienteNoEstacionamento(placa):

        arq = open(utils._caminhoArqRegEntSai + utils._arqRegEntSai, 'r')
        i = utils.utils.checkLinhaRegistro(placa, utils._caminhoArqRegEntSai, utils._arqRegEntSai)
        if i != -1:
            linha = arq.readlines()[i]
            placa, data, hora, mensalista = linha.split("@", maxsplit=3)
            horas, minutos = hora.split(":")
            horas_em_minutos = int(horas) * 60
            hora_de_entrada_em_minutos = horas_em_minutos + int(minutos)

            h = datetime.datetime.now()
            hora_atual, minuto_atual = int(h.strftime('%H')), int(h.strftime('%M'))
            hora_atual_em_minutos = (int(h.strftime('%H')) * 60) + int(h.strftime('%M'))
            HrsCliente = hora_atual_em_minutos - hora_de_entrada_em_minutos
            minutos_em_horas = HrsCliente // 60
            minutos_restantes = HrsCliente % 60

            tempoTotal = str(idiomas._idiomas.mensTempoNoEstacionamento+str(minutos_em_horas)+'H:'+str(minutos_restantes)+'min')
            Carro = idiomas._idiomas.mensInfoPlaca+placa

            utils.utils.alertaArquivo(idiomas._idiomas.mensAtencao, Carro+ '\n' +tempoTotal)

        else:
            print(idiomas._idiomas.mensInfoPlaca)

    def mostraTodosClientes(self):
        arq = open(utils._caminhoArqRegEntSai + utils._arqRegEntSai, 'r')
        teste = arq.readlines()
        print("  ----   " + idiomas._idiomas.mensCliNoEstacionamento + "   ---")
        for i in teste:
            placa, data, horaEntrada, mensalista = i.split("@", maxsplit=3)
            print(idiomas._idiomas.mensPlaca, placa)
            print(idiomas._idiomas.mensCliEntrouAs, horaEntrada)
        arq.close()
