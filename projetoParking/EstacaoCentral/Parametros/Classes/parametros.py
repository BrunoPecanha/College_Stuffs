import json
import os
from EstacaoCentral.Parametros.Forms import frmParametros
from EstacaoCentral.Utils.Classes import utils

class _parametro:

    __caminho1 = "C:/Users\Bruno Peçanha\Desktop\projetoParking\EstacaoCentral\Arquivos/configuracao"
    __caminho2 = "C:/Users\Bruno Peçanha\Desktop\projetoParking\EstacaoCentral\Arquivos/regEntSaida"
    __caminho3 = "C:/Users\Bruno Peçanha\Desktop\projetoParking\EstacaoCentral\Arquivos/help"
    __caminho4 = "C:/Users\Bruno Peçanha\Desktop\projetoParking\EstacaoCentral\Arquivos/clientes"

    caminhos = [__caminho1, __caminho2, __caminho3, __caminho4] # Crio uma lista com todos os caminhos que vou usar.

    for i in caminhos: # Testo para ver se a pasta de cada arquivo está criada, do contrário, eu crio.
        if not os.path.exists(i):
            os.makedirs(i)

    _caminhoArqConfig = "C:/Users\Bruno Peçanha\Desktop\projetoParking\EstacaoCentral\Arquivos/configuracao"
    _caminhoArqRegEntSai = "C:/Users\Bruno Peçanha\Desktop\projetoParking\EstacaoCentral\Arquivos/regEntSaida"
    _caminhoArqMenuAjuda = "C:/Users\Bruno Peçanha\Desktop\projetoParking\EstacaoCentral\Arquivos/help"
    _caminhoArqCadClientes = "C:/Users\Bruno Peçanha\Desktop\projetoParking\EstacaoCentral\Arquivos/clientes"
    _arqConfig = "/configs"+".txt"
    _arqCadClientes = "/cadastroClientes"+".txt"
    _arqRegEntSai = "/registroEntradaSaida"+".txt"
    _arqMenuAjuda = "/menuAjuda"+".txt"
    _arqIdiomaEng = "/eng"+".txt"
    _arqIdiomaPtbr = "/ptbr"+".txt"
    _arqIdiomaEsp = "/esp"+".txt"