import io
import re
import subprocess
import sys
import argparse


def enable_verbose_logging():
    """Ativa o modo log detalhado.

    Returns:
        Popen: Instances of the Popen class 
    """
    try:
        #subprocess.run("adb shell setprop log.tag.FA VERBOSE".split(" "))
        subprocess.run("adb shell setprop log.tag.FA-SVC VERBOSE".split(" "))
        proc = subprocess.Popen("adb logcat -v time -s FA FA-SVC".split(" "), stdout=subprocess.PIPE)
    except:
        print(f"Ops. Houve algum erro. Verifique se o adb está instalado.")
        sys.exit(1)
    else:
        return proc


def no_arguments():
    """Exibe os logs das tags de eventos e screenview no terminal. Ou seja, os eventos que estão sendo registrados. 
    """
    proc = enable_verbose_logging()

    re_capture_bundle = re.compile(r"Logging\ event:")
    e_screenview = re.compile(r'name=screen_view')
    e_auto = re.compile(r'origin=auto')

    for line in io.TextIOWrapper(proc.stdout, encoding="utf-8"):

        if re_capture_bundle.search(line, re.IGNORECASE):
            line = re.sub(r"\w+\[\{", r"Bundle[{\n", line)
            line = re.sub(r"\}\]", r"\n}]", line)
            line = re.sub(r", |,", r"\n", line)

            if e_screenview.search(line) and not e_auto.search(line):
                print(f"\033[1;34m{line}\033[m")

            elif e_auto.search(line):
                print(f"\033[1;90m{line}\033[m")
            else:
                print(f"\033[1;33m{line}\033[m")


def with_arguments(args: argparse.Namespace):
    """Filtra os logs detalhados com base nos argumentos passados pelo usuário.

    Args:
        args (argparse.Namespace): Argumentos passados pelo usuário na chamada para execução do script.
    """
    if args.term1 == None and args.term2 == None: # caso exista somente -v
        no_arguments()

    elif args.term1 != None and args.term2 != None:
        proc = enable_verbose_logging()
        re_terms = re.compile(rf"{args.term1}|{args.term2}")

        for line in io.TextIOWrapper(proc.stdout, encoding="utf-8"):
            check_terms = list(set(re_terms.findall(line, re.IGNORECASE)))
            
            if len(check_terms) == 2:
                check_terms.sort() # sort - ordem alfabetica
                line = re.sub(r', |,', r'\n', line)
                line = re.sub(f"{check_terms[0]}", f"\033[1;32m{check_terms[0]}\033[m", line)
                line = re.sub(f"{check_terms[1]}", f"\033[1;34m{check_terms[1]}\033[m", line)
                print(line)

    elif args.term1 != None or args.term2 != None:
        proc = enable_verbose_logging()
        term = args.term1 if args.term1 != None else args.term2
        re_terms = re.compile(rf"{term}")
        
        for line in io.TextIOWrapper(proc.stdout, encoding="utf-8"):
            match =re_terms.search(line, re.IGNORECASE)         
            if match:
                line = re.sub(r', |,', r'\n', line)
                line = re.sub(match.group(), f"\033[1;32m{match.group()}\033[m", line)
                print(line)