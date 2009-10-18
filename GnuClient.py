#!/usr/bin/env python
import sys
import subprocess

cmdArgs = [
    "/Applications/Emacs.app/Contents/MacOS/bin/emacsclient",
    "emacsclient",
    "-n",
    "-e"
    ]

# First argument is the name of this script, so we ignore that.
if len(sys.argv) > 1:
    file = sys.argv.pop(1)
    lisp="(find-file-other-frame \"%s\")" % file
else:
    lisp="(new-frame)"
cmdArgs.append(lisp)

subprocess.Popen(cmdArgs,
                 shell=False)
