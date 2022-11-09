import sys
import argparse
from platforms_android import firebase, univesal_analytics, appsflyer, gtm
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
    option = ["Firebase", "Universal Analytics", "AppsFlyer", "Google Tag Manager", "Sair"]
    action = ""
    msg = ""
    description = verbose

    while action not in ["0", "1", "2", "3", "4"]:
        clean_screen()
        title("Debug Log - Android")
        if description:
            verbose_custom()
        options(option, msg)

        action = input(str("Opção: ")).strip()
        msg = "\033[31mOpção inválida. Escolha entre 0, 1, 2, 3 ou 4.\033[m"
        
    return action


if __name__ == "__main__":
    args = receive_arguments()
    description = False
    
    if args.verbose:
            description = True

    action = user_choice(description)

    if (len(sys.argv) == 1):
        if action == "0":
            firebase.no_arguments()
        elif action == "1":
            univesal_analytics.no_arguments()
        # opcoes sem filtros
        elif action == "2":
            appsflyer.appsFlyer()
        elif action == "3":
            gtm.main()
        elif action == "4":
            pass
    
    else:
        if action == "0":
            firebase.with_arguments(args)
        elif action == "1":
            univesal_analytics.with_arguments(args)
        # opcoes sem filtros
        elif action == "2":
            appsflyer.appsFlyer()
        elif action == "3":
            gtm.main()
        elif action == "4":
            pass
    
    print("\033[1;32mFinalizado.\033[m")
    sys.exit(0)
