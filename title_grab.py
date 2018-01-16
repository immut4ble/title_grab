# packet
# Grabs the title of a given webpage.
import sys
import subprocess

def grab_title():
    output = subprocess.check_output(['curl -L', sys.argv[1]], shell=True)
    opening_title = output.find("<title>")
    closing_title = output.find("</title>")
    title = output[opening_title+7:closing_title]
    title = title.strip()
    print(title)

if len(sys.argv) != 2:
    print("useage: title_grab ip-address")
else:
    grab_title()
