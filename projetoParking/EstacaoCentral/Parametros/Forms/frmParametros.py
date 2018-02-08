import os
import time

class _frmParametros(object):

    def cabecalhoAjuda(self):
        os.system('cls')
        # informacoesDeUso
        print("                           ####################################################")
        print("                           #                                                  #")
        print("############################                 Instrucoes de Uso                 ############################")
        print("                           #                                           v  1.0 #")
        print("                           #################################################### \n\n")
        #endInformacoesDeUso
        time.sleep(1)

    def cabecalhoConfig(self):
        os.system('cls')
        # informacoesClientes
        print('                           ####################################################')
        print('                           #                                                  #')
        print('#############################                   Configuracoes                 ###########################')
        print('                           #                                           v  1.0 #')
        print('                           #################################################### \n\n')
        #print(config.configuracao.recuperaConfig(3) + cabecalhos.recuperaDiaHora(''))
        # endCadastroCliente
        time.sleep(1)