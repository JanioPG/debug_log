import io
import re
import subprocess
import sys
import argparse
from platforms import firebase


def receive_arguments():
    """Recebe e trata os argumentos passados na chamada para execução do script.

    Returns:
        [argparse.Namespace]: todos os argumentos
    """
    parser = argparse.ArgumentParser(description="Quando dois ou um termo de pesquisa é passado, você pode buscá-los separados ou combinados.")
    parser.add_argument("-t1", "--term1", type=str, help="Primeiro termo de pesquisa.")
    parser.add_argument("-t2", "--term2", type=str, help="Segundo termo de pesquisa.")
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")

    return parser.parse_args()


def user_choice(list: list):
    print("Escolha a plataforma:")
    for i, item in enumerate(list):
        print(f"[{i}] - {item}")
    option = input(str("Option: "))
    return option


if __name__ == "__main__":

    option = ["Firebase", "Universal", "AppsFlyer", "Sair"]
    
    if (len(sys.argv) == 1):
        if user_choice(option) == "1":
            firebase.no_arguments()
    
    else:
        args = receive_arguments()
        if args.verbose:
            print("""Use este script para observar o disparo/acionamento das tags de eventos e screenviews, ajudando você a verificar imediatamente se os eventos estão sendo enviados.\nO script apenas habilita o registro detalhado permitindo verificar se os eventos estão sendo registrados corretamente pelo SDK. Isso inclui eventos registrados manual e automaticamente.""")
        
        if user_choice(option) == "1":
            firebase.with_arguments(args)
    
    print("Saindo")
    sys.exit(0)
