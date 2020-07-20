#!/usr/bin/python3
import argparse
from effects import effects

parser = argparse.ArgumentParser()
parser.add_argument('-e','--effect',help='effect to run',action="store")
arg = parser.parse_args()

worker = effects()
loop = getattr(worker,str(arg.effect))
while True:
    loop()
