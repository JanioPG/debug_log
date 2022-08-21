import io
import re
import subprocess
import json

#subprocess.run("adb shell setprop log.tag.FA VERBOSE".split(" "))
subprocess.run("adb shell setprop log.tag.FA-SVC VERBOSE".split(" "))
proc = subprocess.Popen("adb logcat -v time -s FA FA-SVC".split(" "), stdout=subprocess.PIPE)

re_capture_bundle = re.compile(r'Logging event:')
e_screenview = re.compile(r'name=screen_view')
e_auto = re.compile(r'origin=auto')




for line in io.TextIOWrapper(proc.stdout, encoding="utf-8"):

    if re_capture_bundle.search(line):
        line = re.sub(r', ', r',', line)
        line = re.sub(r',', r'\n', line)
        line = re.sub(r'items=\[Bundle', r'items=[\nBundle', line)
        line = re.sub(r'}\]', r'\n}]', line)

        if e_screenview.search(line) and not e_auto.search(line):
            print(f"\033[1;34m{line}\033[m")

        elif e_auto.search(line):
            print(f"\033[1;90m{line}\033[m")
        else:
            print(f"\033[1;33m{line}\033[m")
