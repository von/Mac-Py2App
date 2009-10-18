#!/usr/bin/env python
import os
os.spawnl(os.P_NOWAIT,
          "/usr/bin/ssh",
          "ssh",
          "pkirack15.ncsa.uiuc.edu",
          "/usr/bin/vmware")
