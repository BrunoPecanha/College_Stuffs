import time
import os
from EstacaoCentral.Utils.Classes import bsnValidacaoInicial
from EstacaoCentral.Menu.Form import frmMenu
from EstacaoCentral.Utils.Classes import utils as utilitarios
from EstacaoCentral.Utils.Classes import idiomas
from EstacaoCentral.Cliente.Classes import bsnCliente as cliente

class _menuPrincipal:

    def _menus(self):
        frmMenu.frmMenu.menuPrincipal('')
        print(idiomas._idiomas.mensOp)
        ret = input()

        while not(ret.__eq__('1')) and not(ret.__eq__('2')) and not(ret.__eq__('3')) and not(ret.__eq__('4')) and not(ret.__eq__('5')) and not(ret.__eq__('6')) and not(ret.__eq__('7')) and not(ret.__eq__('8')) and not(ret.__eq__('9')):
            os.system('cls')
            frmMenu.frmMenu.menuPrincipal('')
            print(idiomas._idiomas.mensOpValida)
            time.sleep(1)  # Estava carregando a mensagem "Operação" antes do cabeçalho. Com isso, ele aguarda 1 seg antes do comando de baixo
            print(idiomas._idiomas.mensOp)
            ret = input()
        else:
            if ret.__eq__('1'):
                cliente._bsnCliente.entradaInfNovoCliente('')
                _menuPrincipal.refazerOuMenuInicial('1')
            elif ret.__eq__('2'):
                cliente._bsnCliente.recuperaCadastro(utilitarios.utils.checkLinhaRegistro(cliente._bsnCliente.recuperaPlaca('').upper(), utilitarios._caminhoArqCadClientes, utilitarios._arqCadClientes))
                _menuPrincipal.refazerOuMenuInicial('2')
            elif ret.__eq__('3'):
                cliente._bsnCliente.entrada('')
                _menuPrincipal.refazerOuMenuInicial('3')
            elif ret.__eq__('4'):
                float
                _menuPrincipal.refazerOuMenuInicial('4')
            elif ret.__eq__('5'):
                float
                _menuPrincipal.refazerOuMenuInicial('5')
            elif ret.__eq__("6"):
                utilitarios.utils.mostraInstrucoes('')
                _menuPrincipal.refazerOuMenuInicial('6')
            elif ret.__eq__("7"):
                bsnValidacaoInicial._bsnValidacaoInicial.parametrizarConfiguracao('')
                _menuPrincipal.refazerOuMenuInicial('7')
                utilitarios.utils.recuperarParametros('')
            elif ret.__eq__('8'):
                float
                _menuPrincipal.refazerOuMenuInicial('8')
            else:
                if (utilitarios.utils.finalizarApp('')):
                    exit()
                else:
                    _menuPrincipal._menus('')
    def refazerOuMenuInicial(menu):
        print(idiomas._idiomas.mensRefazUltOp, end='                                             ')
        print(idiomas._idiomas.mensVoltMenuPrinc)
        ret = input()
        if ret.__eq__("2"):
            _menuPrincipal._menus('')
        else:
            if menu.__eq__("1"):
                cliente._bsnCliente.entradaInfNovoCliente('')
            elif menu.__eq__("2"):
                cliente._bsnCliente.recuperaCadastro(
                    utilitarios.utils.checkLinhaRegistro(cliente._bsnCliente.recuperaPlaca('').upper(),
                                                         utilitarios._caminhoArqCadClientes,
                                                         utilitarios._arqCadClientes))
                _menuPrincipal.refazerOuMenuInicial('')
            elif menu.__eq__("3"):
                cliente._bsnCliente.entrada('')
                _menuPrincipal.refazerOuMenuInicial('')
            elif menu.__eq__("4"):
                float
            elif menu.__eq__("5"):
                float
            elif menu.__eq__("6"):
                utilitarios.utils.mostraInstrucoes('')
                _menuPrincipal.refazerOuMenuInicial('')
            elif menu.__eq__("7"):
                float