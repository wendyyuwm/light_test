import subprocess
import time
import sys

for i in range(31):
    try:
        script_name = "Color_gamut_xy_TC%s.py" % str(i+1)
        print "\n"*2 + "#" * 10 + "\t" + script_name + "\t" + "#" * 10
        subprocess.check_call("python %s" % script_name)
        time.sleep(5)

    except subprocess.CalledProcessError as e:
        print e
        sys.exit()

