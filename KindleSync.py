#!/usr/bin/env python
"""Sync PDFs on my Kindle with a local folder.

This serves as a long usage message.
"""
import glob
from optparse import OptionParser
import os
import os.path
import shutil
import sys

# Places to look for KindleRoot
PossibleKindleRoots = [
    "/Volumes/Kindle"
    ]

# Local path to sync from
LocalPath = os.path.expanduser("~/Desktop/ToRead")

def main(argv=None):
    # Do argv default this way, as doing it in the functional
    # declaration sets it at compile time.
    if argv is None:
        argv = sys.argv
    parser = OptionParser(
        usage="%prog [<options>] <some arg>", # printed with -h/--help
        version="%prog 1.0" # automatically generates --version
        )
    parser.add_option("-q", "--quiet", action="store_true", dest="quiet",
                      help="run quietly", default=False)
    (options, args) = parser.parse_args()
    if not os.path.exists(LocalPath):
        print "Local directory %s does not exist."
        sys.exit(1)
    # Find KindleRoot to use (use first if multiple found)
    KindleRoots = filter(lambda path: os.path.exists(path),
                         PossibleKindleRoots,)
    if len(KindleRoots) == 0:
        print "No Kindle found"
        sys.exit(0)
    KindleRoot = KindleRoots[0]
    print "Kindle Root is %s" % KindleRoot
    print "Local path is %s" % LocalPath
    KindleSyncPath = os.path.join(KindleRoot, "documents", "sync")
    KindleFiles = os.listdir(KindleSyncPath)
    LocalSyncPath = os.path.join(LocalPath, "sync")
    if not os.path.exists(LocalSyncPath):
        print "Local sync directory %s does not exist." % LocalSyncPath
        sys.exit(1)
    LocalSyncedFiles = os.listdir(LocalSyncPath)
    # First, deleted any files that have been deleted on Kindle
    DeletedOnKindle = filter(lambda file: not os.path.exists(os.path.join(KindleSyncPath, file)),
                             LocalSyncedFiles)
    for file in DeletedOnKindle:
        print "Deleting %s form local system" % file
        os.unlink(LocalSyncPath)
    # Ok, now copy over any new files
    ToBeAddedFiles = glob.glob(os.path.join(LocalPath, "*.pdf"))
    for file in ToBeAddedFiles:
        print "Adding %s to Kindle" % file
        shutil.copy(file, os.path.join(KindleSyncPath, os.path.basename(file)))
        shutil.move(file, os.path.join(LocalSyncPath, os.path.basename(file)))
    sys.exit(0)

if __name__ == "__main__":
    sys.exit(main())



