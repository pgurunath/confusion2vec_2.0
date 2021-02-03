#!/usr/bin/env python

"""Data preperation: Convert Kaldi Sausage to text format compatible for training models"""


import os
import sys
import argparse
import re

__author__ = "Prashanth Gurunath Shivakumar"
__maintainer__ = "Prashanth Gurunath Shivakumar"
__email__ = "pgurunat@usc.edu"

def get_num_lines(fp):
  for lines, _ in enumerate(fp):
    continue
  fp.seek(0)
  return lines+1

def filter_silence(data):
  return [x for x in data if ((not x.startswith("<")) and (not x.startswith("[")) and (not x.startswith("#")))]

def read_data_sausage(ifile, ofile, id2word):
  for n, line in enumerate(ifile):
    uttid = line[:line.find(' ')]
    sau = [x[1:-1].split() for x in re.findall('\[.*?\]', line)]
    wrds = [list(map(id2word.get, x))[::2] for x in sau]
    scrs = [x[1::2] for x in sau]
    ostr = ""
    for c, cs in zip(wrds, scrs):
      ostr += " [ " + " ".join([x+" "+y for x,y in zip(c,cs)]) + " ]"
    ofile.write(ostr.strip() + os.linesep)

def main():
  parser = argparse.ArgumentParser(description='Data preperation: Convert Kaldi Sausage to Confusion2vec text format')
  parser.add_argument("input", nargs='?', type=argparse.FileType("r"), default=sys.stdin, help="Input Kaldi Sausage file")
  parser.add_argument("wordFile", type=argparse.FileType("r"), help="Kaldi words.txt file")
  parser.add_argument("output", nargs='?', type=argparse.FileType("w"), default=sys.stdout, help="Output text file")

  args = parser.parse_args()


  word2id, id2word = {}, {}
  for line in args.wordFile:
    word, id_ = line.strip().split()
    word2id[word] = id_
    id2word[id_] = word

  read_data_sausage(args.input, args.output, id2word)


if __name__ =="__main__":
  main()
