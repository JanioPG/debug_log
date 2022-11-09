import io
import re
import subprocess
import json

def convert_object(txt):
    return txt.replace(',', ',\n')

def print_gtm_event(line):
    """re_caputre_event_category = re.compile(r'vtp_eventCategory=.*?, ')
    re_caputre_event_action = re.compile(r'vtp_eventAction=.*?, ') 
    re_caputre_event_label = re.compile(r'vtp_eventLabel=.*?, ')  
    re_capture_ua = re.compile(r'vtp_gaSettings=.*?, ')

    category = re_caputre_event_category.search(line)
    action = re_caputre_event_action.search(line)
    label = re_caputre_event_label.search(line)
    ua = re_capture_ua.search(line)"""

    print('\x1b[93m' + '\x1b[1m' + line)

def print_gtm_screenview(line):
    print('\x1b[94m' + '\x1b[1m' + line)

def main():
    subprocess.run("adb shell setprop log.tag.GoogleTagManager VERBOSE ".split(" "))

    proc = subprocess.Popen("adb logcat -v time -s GoogleTagManager".split(" "), stdout=subprocess.PIPE)

    re_firing_tag = re.compile(r'Executing firing')
    re_caputre_screenview = re.compile(r"vtp_trackType=TRACK_SCREENVIEW")
    re_capture_event = re.compile(r"vtp_trackType=TRACK_EVENT")

    for line in io.TextIOWrapper(proc.stdout, encoding="utf-8"):
        if re_firing_tag.search(line):
            if re_caputre_screenview.search(line):
                print_gtm_screenview(line.replace(r", ", "\n"))
            elif re_capture_event.search(line):
                print_gtm_event(line.replace(r", ", "\n"))
            else:
                print(line)


if __name__ == "__main__":
    main()