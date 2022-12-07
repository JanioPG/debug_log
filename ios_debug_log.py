import sys
import argparse
from platforms_ios import firebase_ios, universal_analytics_ios
from interface import title, options, clean_screen, verbose_custom


def receive_arguments():
    """Recebe e trata os argumentos passados na chamada para execução do script.

    Returns:
        [argparse.Namespace]: todos os argumentos
    """
    parser = argparse.ArgumentParser(description="Ative o registro detalhado e veja imediatamente o envio dos eventos. Use argumentos para filtrar.")
    parser.add_argument("-t1", "--term1", type=str, help="Primeiro termo de pesquisa.")
    parser.add_argument("-t2", "--term2", type=str, help="Segundo termo de pesquisa.")
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")

    return parser.parse_args()


def user_choice(verbose: bool):
    """Obtém a plataforma/analytics de escolha do usuário.

    Args:
        verbose (bool): Determina se a descrição do programa será exibida para o usuário no menu de escolha da plataforma.

    Returns:
        action (str): Indíce da plataforma escolhida pelo usuário.
    """
    option = ["Firebase", "Universal Analytics", "Sair"] #, "AppsFlyer", "Google Tag Manager", "Sair"]
    action = ""
    msg = ""
    description = verbose

    while action not in ["0", "1", "2"]:
        clean_screen()
        title("Debug Log - iOS")
        if description:
            verbose_custom()
        options(option, msg)

        action = input(str("Opção: ")).strip()
        msg = "\033[31mOpção inválida. Escolha entre 0, 1 ou 2.\033[m"
        
    return action


if __name__ == "__main__":
    args = receive_arguments()
    # por enquanto nao tem filtro
    description = False
    
    if args.verbose:
            description = True

    action = user_choice(description)

    if (len(sys.argv) == 1):
        if action == "0":
            firebase_ios.no_arguments()
        elif action == "1":
            universal_analytics_ios.no_arguments()
        elif action == "2":
            pass
        
        # Incluir AppsFlyer e GTM
    
    else:
        if action == "0":
            firebase_ios.with_arguments(args)
        elif action == "1":
            universal_analytics_ios.with_arguments(args)
        elif action == "2":
            pass

        # incluir AppsFlyer e GTM
    
    print("\033[1;32mFinalizado.\033[m")
    sys.exit(0)
