import os
import time
from EstacaoCentral.Utils.Classes import idiomas
from EstacaoCentral.Utils.Classes import utils

class frmMenu:

    def menuPrincipal(self):
        os.system('cls') # Limpa a tela antes de mostrar qualquer coisa
        # menuPrincipal
        print("                            ####################################################")
        print("                            #                                                  #")
        print("#############################                "+utils.utils.recuperarParametros(5)+"                   #################################")
        print("                            #                                           v  1.0 #")
        print("                            #################################################### \n\n")
        print(utils.utils.recuperarParametros(6), ", " + utils.utils.recuperaDiaHora(''))
        print(idiomas._idiomas.mensCadNovoCliente)
        print(idiomas._idiomas.mensLocalizaCli)
        print(idiomas._idiomas.mensEntradaCli)
        print(idiomas._idiomas.mensConsultaTempo)
        print(idiomas._idiomas.mensBaixaCliente)
        print(idiomas._idiomas.mensAjuda)
        print(idiomas._idiomas.mensConfigs)
        print(idiomas._idiomas.mensTodosCli)
        print(idiomas._idiomas.mensMenuExcluir)
        print(idiomas._idiomas.mensSair+ '\n')
        time.sleep(1)