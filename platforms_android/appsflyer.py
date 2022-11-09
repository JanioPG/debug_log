import io
import re
import subprocess
import json

def convert_object(txt):
    return txt.replace(',', ',\n')

def appsFlyer():
    subprocess.run("adb shell setprop log.tag.FA VERBOSE".split(" "))
    subprocess.run("adb shell setprop log.tag.FA-SVC VERBOSE".split(" "))
    proc = subprocess.Popen("adb logcat | grep appsflyer".split(" "), stdout=subprocess.PIPE)

    re_capture_bundle = re.compile(r'.*data:.*')

    for line in io.TextIOWrapper(proc.stdout, encoding="utf-8"):

        if re_capture_bundle.search(line):
            txt = re_capture_bundle.search(line)
            print(txt.group(0) + '\n')

if __name__ == "__main__":
    appsFlyer()