import os

class _parametro:

    __caminho1 = "C:/Users\Ramilson\Dropbox\Sistemas de Informação\Programação\Trabalho\projetoParking\EstacaoCentral\Arquivos/configuracao"
    __caminho2 = "C:/Users\Ramilson\Dropbox\Sistemas de Informação\Programação\Trabalho\projetoParking\EstacaoCentral\Arquivos/regEntSaida"
    __caminho3 = "C:/Users\Ramilson\Dropbox\Sistemas de Informação\Programação\Trabalho\projetoParking\EstacaoCentral\Arquivos/help"
    __caminho4 = "C:/Users\Ramilson\Dropbox\Sistemas de Informação\Programação\Trabalho\projetoParking\EstacaoCentral\Arquivos/clientes"

    caminhos = [__caminho1, __caminho2, __caminho3, __caminho4] # Crio uma lista com todos os caminhos que vou usar.

    for i in caminhos: # Testo para ver se a pasta de cada arquivo está criada, do contrário, eu crio.
        if not os.path.exists(i):
            os.makedirs(i)

    _caminhoArqConfig = "C:/Users\Ramilson\Dropbox\Sistemas de Informação\Programação\Trabalho\projetoParking\EstacaoCentral\Arquivos/configuracao"
    _caminhoArqRegEntSai = "C:/Users\Ramilson\Dropbox\Sistemas de Informação\Programação\Trabalho\projetoParking\EstacaoCentral\Arquivos/regEntSaida"
    _caminhoArqMenuAjuda = "C:/Users\Ramilson\Dropbox\Sistemas de Informação\Programação\Trabalho\projetoParking\EstacaoCentral\Arquivos/help"
    _caminhoArqCadClientes = "C:/Users\Ramilson\Dropbox\Sistemas de Informação\Programação\Trabalho\projetoParking\EstacaoCentral\Arquivos/clientes"
    _arqConfig = "/configs"+".txt"
    _arqCadClientes = "/cadastroClientes"+".txt"
    _arqRegEntSai = "/registroEntradaSaida"+".txt"
    _arqMenuAjuda = "/menuAjuda"+".txt"
    _arqIdiomaEng = "/eng"+".txt"
    _arqIdiomaPtbr = "/ptbr"+".txt"
    _arqIdiomaEsp = "/esp"+".txt"
