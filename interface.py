import os


def title(txt: str):
    print("\033[1;34m-\033[1m" * 35, end="\n\033[1;32m")
    print(f"{txt}".center(35), end="\033[m\n")
    print("\033[1;34m-\033[m" * 35)

def options(options: list, msg: str = ""):
    print("Escolha a plataforma:")
    for i, item in enumerate(options):
        print(f"[{i}] - {item}")
    print(msg)
    
def clean_screen():
    os.system("cls" if os.name == "nt" else "clear")


def verbose_custom():
    text = "Use este script para observar o dis\nparo/acionamento das tags de evento\ns e screenviews, ajudando você a ve\nrificar imediatamente se os eventos\n estão sendo enviados. O script ape\nnas habilita o registro detalhado p\nermitindo verificar se os eventos e\nstão sendo registrados corretamente\n pelo SDK. Isso inclui eventos regi\nstrados manual e automaticamente.\n"
    print(text)

if __name__ == "__main__":
    title("Debug Log")