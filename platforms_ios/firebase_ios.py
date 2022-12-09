import io
import re
import subprocess
import sys
import argparse

def enable_verbose_logging():
    try:
        proc = subprocess.Popen("xcrun simctl spawn booted log stream --level=debug", shell=True, stdout=subprocess.PIPE)

    except:
        print(f"Ops. Houve algum erro.")
        sys.exit(1)
    else:
        return proc


def no_arguments():
    """Exibe os logs das tags de eventos e screenview no terminal. Ou seja, os eventos que estão sendo registrados. 
    """
    proc = enable_verbose_logging()
    
    re_capture_bundle = re.compile(r"Logging\ event")
    e_screenview = re.compile(r'name.*screen_view')
    e_auto = re.compile(r'origin.*auto')
    new_event = re.compile(r"\d\d:\d\d:\d\d.\d\d.*0x")
    continue_log = False
    event_log = ""

    for line in io.TextIOWrapper(proc.stdout, encoding="utf-8"):
        if continue_log == True and not new_event.search(line, re.IGNORECASE):
            event_log += line

        elif re_capture_bundle.search(line, re.IGNORECASE) and continue_log == False:
            event_log += line
            continue_log = True
        
        else:
            if re_capture_bundle.search(event_log, re.IGNORECASE):
                continue_log = False
                event_log = re.sub(r"0x.*event:\ ", r"", event_log)
                if e_screenview.search(event_log) and not e_auto.search(event_log):
                    print(f"\033[1;34m{event_log}\033[m")

                elif e_auto.search(event_log):
                    print(f"\033[1;90m{event_log}\033[m")

                else:
                    print(f"\033[1;33m{event_log}\033[m")
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
        re_terms = re.compile(rf"{args.term1}|{args.term2}")
        re_capture_bundle = re.compile(r"Logging\ event")
        new_event = re.compile(r"\d\d:\d\d:\d\d.\d\d.*0x")
        continue_log = False
        event_log = ""        

        for line in io.TextIOWrapper(proc.stdout, encoding="utf-8"):
            if continue_log == True and not new_event.search(line, re.IGNORECASE):
                event_log += line
            
            elif re_capture_bundle.search(line, re.IGNORECASE) and continue_log == False:
                event_log += line
                continue_log = True

            else:
                if re_capture_bundle.search(event_log, re.IGNORECASE):
                    continue_log = False
                    event_log = re.sub(r"0x.*event:\ ", r"", event_log)
                    
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

        re_capture_bundle = re.compile(r"Logging\ event")
        new_event = re.compile(r"\d\d:\d\d:\d\d.\d\d.*0x")
        continue_log = False
        event_log = ""      
        
        for line in io.TextIOWrapper(proc.stdout, encoding="utf-8"):
            if continue_log == True and not new_event.search(line, re.IGNORECASE):
                event_log += line
            
            elif re_capture_bundle.search(line, re.IGNORECASE) and continue_log == False:
                event_log += line
                continue_log = True
            else:
                if re_capture_bundle.search(event_log, re.IGNORECASE):
                    continue_log = False
                    event_log = re.sub(r"0x.*event:\ ", r"", event_log)

                    match = re_terms.search(event_log, re.IGNORECASE)         
                    if match:
                        event_log = re.sub(match.group(), f"\033[1;32;40m{match.group()}\033[m", event_log)
                        print(event_log)
                    event_log = ""

if __name__ == "__main__":
    no_arguments()