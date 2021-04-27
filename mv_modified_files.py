#!/usr/bin/env python

from git import Repo
import os
from shutil import copyfile, move
import sys

def main(destdir):
    repo = Repo('.')
    out = repo.git.status()
    lines = out.split('\n')
    modified_files = []
    for li in lines:
        li = li.strip()
        if li.startswith('modified:'):
            fi = li.replace('modified:','').strip()
            modified_files.append(fi)
    for fi in modified_files:
        nfi = fi.replace('linux-0.11/oslab/linux-0.11/', '')
        basename = os.path.basename(nfi)
        dirname = os.path.dirname(nfi)
        os.makedirs(os.path.join(destdir, dirname), exist_ok=True)
        copyfile(fi, os.path.join(destdir, nfi))

    prefix = 'linux-0.11/oslab/linux-0.11'
    for fi in repo.untracked_files:
        if fi.startswith(prefix):
            move(fi, os.path.join(destdir, os.path.basename(fi)))


if __name__ == "__main__":
    # destdir = '/home/yan/git/linuxstudy/linux-0.11/3-processTrack'
    
    if len(sys.argv) >= 2:
        main(sys.argv[1])
    else:
        print('Usage: %s destdir' % sys.argv[0])
        