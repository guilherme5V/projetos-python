from colorama import Fore, Back, Style, init

# Inicializa o colorama
init(autoreset=True)

# Funções para aplicar cores no texto
def preto(texto):
    return f"{Fore.BLACK}{texto}"

def vermelho(texto):
    return f"{Fore.RED}{texto}"

def verde(texto):
    return f"{Fore.GREEN}{texto}"

def amarelo(texto):
    return f"{Fore.YELLOW}{texto}"

def azul(texto):
    return f"{Fore.BLUE}{texto}"

def magenta(texto):
    return f"{Fore.MAGENTA}{texto}"

def ciano(texto):
    return f"{Fore.CYAN}{texto}"

def branco(texto):
    return f"{Fore.WHITE}{texto}"

# Funções para aplicar cores fortes no texto
def preto_forte(texto):
    return f"{Fore.LIGHTBLACK_EX}{texto}"

def vermelho_forte(texto):
    return f"{Fore.LIGHTRED_EX}{texto}"

def verde_forte(texto):
    return f"{Fore.LIGHTGREEN_EX}{texto}"

def amarelo_forte(texto):
    return f"{Fore.LIGHTYELLOW_EX}{texto}"

def azul_forte(texto):
    return f"{Fore.LIGHTBLUE_EX}{texto}"

def magenta_forte(texto):
    return f"{Fore.LIGHTMAGENTA_EX}{texto}"

def ciano_forte(texto):
    return f"{Fore.LIGHTCYAN_EX}{texto}"

def branco_forte(texto):
    return f"{Fore.LIGHTWHITE_EX}{texto}"

# Funções para aplicar cores de fundo no texto
def fundo_preto(texto):
    return f"{Back.BLACK}{texto}"

def fundo_vermelho(texto):
    return f"{Back.RED}{texto}"

def fundo_verde(texto):
    return f"{Back.GREEN}{texto}"

def fundo_amarelo(texto):
    return f"{Back.YELLOW}{texto}"

def fundo_azul(texto):
    return f"{Back.BLUE}{texto}"

def fundo_magenta(texto):
    return f"{Back.MAGENTA}{texto}"

def fundo_ciano(texto):
    return f"{Back.CYAN}{texto}"

def fundo_branco(texto):
    return f"{Back.WHITE}{texto}"

# Funções para aplicar cores fortes de fundo no texto
def fundo_preto_forte(texto):
    return f"{Back.LIGHTBLACK_EX}{texto}"

def fundo_vermelho_forte(texto):
    return f"{Back.LIGHTRED_EX}{texto}"

def fundo_verde_forte(texto):
    return f"{Back.LIGHTGREEN_EX}{texto}"

def fundo_amarelo_forte(texto):
    return f"{Back.LIGHTYELLOW_EX}{texto}"

def fundo_azul_forte(texto):
    return f"{Back.LIGHTBLUE_EX}{texto}"

def fundo_magenta_forte(texto):
    return f"{Back.LIGHTMAGENTA_EX}{texto}"

def fundo_ciano_forte(texto):
    return f"{Back.LIGHTCYAN_EX}{texto}"

def fundo_branco_forte(texto):
    return f"{Back.LIGHTWHITE_EX}{texto}"

# Funções para aplicar estilos no texto
def negrito(texto):
    return f"{Style.BRIGHT}{texto}"

def normal(texto):
    return f"{Style.NORMAL}{texto}"

def fraco(texto):
    return f"{Style.DIM}{texto}"
