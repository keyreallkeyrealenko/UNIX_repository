import os
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-l', help='prints the line count', required=False)
parser.add_argument('-c', help='prints the byte count', required=False)
parser.add_argument('-w', help='prints the word count', required=False)

