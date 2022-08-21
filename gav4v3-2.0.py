import io
import re
import subprocess
import sys

#https://github.com/shiena/ansicolor/blob/master/README.md

subprocess.run("adb shell setprop log.tag.GAv4-SVC DEBUG".split(" "))
proc = subprocess.Popen("adb logcat -s GAv4-SVC".split(" "), stdout=subprocess.PIPE)

re_hit_delivery = re.compile(r'Hit saved to database.')
re_event = re.compile(r't=event')
re_screenview = re.compile(r't=screenview')
#re_hit_saved = re.compile(r'Hit saved to database.')

if (len(sys.argv) == 1): # se nenhum argumento e passado ao executar o script
    for line in io.TextIOWrapper(proc.stdout, encoding="utf-8"):
        if re_hit_delivery.search(line):
            line = re.sub(r', ', r'\n', line)
            if re_event.search(line):
                print(f"\033[1;33m{line}\033[m")
            elif re_screenview.search(line):
                print(f"\033[1;34m{line}\033[m")
            else:
                pass

else:
    search_term = " ".join(sys.argv[1:])
    re_search_term = re.compile(search_term.lower())

    for line in io.TextIOWrapper(proc.stdout, encoding="utf-8"):
        if re_search_term.search(line.lower()):
            line = re.sub(r', ', r'\n', line)
            line = re.sub(search_term, f"\033[1;33m{search_term}\033[m", line)
            print(line)