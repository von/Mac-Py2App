#!/usr/bin/env python
import subprocess
subprocess.Popen(["/Applications/Firefox.app/Contents/MacOS/firefox",
                  # Default is where remote stuff should go
                  "-no-remote",
                  "-P",
                  "Development"],
                 shell=False)
