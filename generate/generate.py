import os
import sys
from random import choice

CHARSET = 'abcdefghijklmnopqrstuvwxyz'
NAMELEN = 8
DEPTH = 3
SPF = 25  # subfolders per folder
TPF = 1600  # targets per folder
PROJECT = 'bazel-1M'


def randname():
  return ''.join(
    (choice(CHARSET) for i in range(NAMELEN))
  )

def makeBUILD(prefix):
  with open(f'{prefix}BUILD', 'w') as f:
    for i in range(TPF):
      f.write(f'java_library(name = "{randname()}")\n')

def create(depth, prefix):
  if depth == 1:
    makeBUILD(prefix)
  elif depth > 1:
    for i in range(SPF):
      dirname = f'{prefix}{randname()}'
      os.mkdir(dirname)
      create(depth - 1, f'{dirname}/')


if not os.path.exists(f'./{PROJECT}'):
  os.mkdir(PROJECT)
  create(DEPTH, f'{PROJECT}/')
  with open(f'{PROJECT}/WORKSPACE', 'w') as fp:
    pass
  print(f'Generated {TPF * SPF ** (DEPTH - 1)} targets')
else:
  print('This already exists.')
