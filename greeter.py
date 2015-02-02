
from __future__ import division, print_function, unicode_literals, absolute_import

import argparse


def main():
  args = parseArgs()

  print( 'Hello {name}!'.format( name = args.name ) )

def parseArgs():
  parser = argparse.ArgumentParser( description = 'Greeter - An Example Application For Vincit Git Trainings' )

  parser.add_argument(
    'name',
    nargs = '?',
    default = 'World',
  )

  return parser.parse_args()
