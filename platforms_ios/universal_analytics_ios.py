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
        proc = subprocess.Popen("xcrun simctl spawn booted log stream --level=debug", shell=True, stdout=subprocess.PIPE)

    except:
        print(f"Ops. Houve algum erro. Verifique também se o xcrun está disponível na sua máquina.")
        sys.exit(1)
    else:
        return proc

def no_arguments():
    """Exibe os logs das tags de eventos e screenview no terminal. Ou seja, os eventos que estão sendo registrados. 
    """
    proc = enable_verbose_logging()
    
    re_hit_saved = re.compile(r"GoogleAnalytics.*Saved\ hit")
    re_event = re.compile(r"parameters\ =.*\ event")
    re_screenview = re.compile(r"screenview")
    new_event = re.compile(r"\d\d:\d\d:\d\d.\d\d.*0x")
    continue_log = False
    event_log = ""

    for line in io.TextIOWrapper(proc.stdout, encoding="utf-8"):
        if continue_log == True and not new_event.search(line, re.IGNORECASE):
            event_log += line

        elif re_hit_saved.search(line, re.IGNORECASE) and continue_log == False:
            event_log += line
            continue_log = True
        
        else:
            if re_hit_saved.search(event_log, re.IGNORECASE):
                event_log = re.sub(r"0x.*Saved\ hit", r"Google Analytics - Saved hit", event_log)
                single_line_record = re.sub("\n", r"", event_log)
                continue_log = False
                
                if re_event.search(single_line_record, re.IGNORECASE):
                    print(f"\033[1;33m{event_log}\033[m")

                elif re_screenview.search(single_line_record, re.IGNORECASE):
                    print(f"\033[1;34m{event_log}\033[m")
                else:
                    pass
                event_log = ""
            else:
                pass


def with_arguments(args: argparse.Namespace):
    """Filtra os logs detalhados com base nos argumentos passados pelo usuário.

    Args:
        args (argparse.Namespace): Argumentos passados pelo usuário na chamada para execução do script.
    """
    if args.term1 == None and args.term2 == None: # caso exista somente -v
        no_arguments()

    elif args.term1 != None and args.term2 != None:
        proc = enable_verbose_logging()

        re_hit_saved = re.compile(r"GoogleAnalytics.*Saved\ hit")
        re_terms = re.compile(rf"{args.term1}|{args.term2}")
        continue_log = False
        new_event = re.compile(r"\d\d:\d\d:\d\d.\d\d.*0x")
        event_log = ""

        for line in io.TextIOWrapper(proc.stdout, encoding="utf-8"):
            if continue_log == True and not new_event.search(line, re.IGNORECASE):
                event_log += line

            elif re_hit_saved.search(line, re.IGNORECASE) and continue_log == False:
                event_log += line
                continue_log = True

            else:
                if re_hit_saved.search(event_log, re.IGNORECASE):
                    event_log = re.sub(r"0x.*Saved\ hit", r"Google Analytics - Saved hit", event_log)

                    continue_log = False
                    
                    check_terms = list(set(re_terms.findall(event_log, re.IGNORECASE)))
            
                    if len(check_terms) == 2:
                        check_terms.sort() # sort - ordem alfabetica

                        event_log = re.sub(f"{check_terms[0]}", f"\033[1;32;40m{check_terms[0]}\033[m", event_log)
                        event_log = re.sub(f"{check_terms[1]}", f"\033[1;34;40m{check_terms[1]}\033[m", event_log)
                        print(event_log)
                        
                    event_log = ""
    
    elif args.term1 != None or args.term2 != None:
        proc = enable_verbose_logging()
        term = args.term1 if args.term1 != None else args.term2
        re_terms = re.compile(rf"{term}")

        re_hit_saved = re.compile(r"GoogleAnalytics.*Saved\ hit")
        continue_log = False
        new_event = re.compile(r"\d\d:\d\d:\d\d.\d\d.*0x")
        event_log = ""

        for line in io.TextIOWrapper(proc.stdout, encoding="utf-8"):
            if continue_log == True and not new_event.search(line, re.IGNORECASE):
                event_log += line

            elif re_hit_saved.search(line, re.IGNORECASE) and continue_log == False:
                event_log += line
                continue_log = True
            
            else:
                if re_hit_saved.search(event_log, re.IGNORECASE):
                    event_log = re.sub(r"0x.*Saved\ hit", r"Google Analytics - Saved hit", event_log)

                    continue_log = False                
                    match = re_terms.search(event_log, re.IGNORECASE)
                    if match:
                        #event_log = re.sub(r', ', r'\n', line)
                        event_log = re.sub(match.group(), f"\033[1;32;40m{match.group()}\033[m", event_log)
                        print(event_log)

                    event_log = ""


if __name__ == "__main__":
    no_arguments()