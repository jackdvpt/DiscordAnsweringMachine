#!/usr/bin/python
from subprocess import Popen
import sys

while True:
    p = Popen("python3 ring.py", shell=True)
    p.wait()
