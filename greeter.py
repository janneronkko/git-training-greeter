#! /usr/bin/env python

from __future__ import division, print_function, unicode_literals, absolute_import

import argparse


def main():
  args = parseArgs()

  greeter = Greeter( args )

  greeter()

def parseArgs():
  parser = argparse.ArgumentParser( description = 'Greeter - An Example Application For Vincit Git Trainings' )

  parser.add_argument(
    '-g',
    '--greeting',
    default = 'Hi',
  )

  parser.add_argument(
    'names',
    metavar = 'names',
    nargs = '*',
    default = [ 'World' ],
  )

  return parser.parse_args()

class Greeter( object ):
  def __init__( self, args ):
    object.__init__( self )

    self.args = args

  def __call__( self ):
    for name in self._names():
      self._greet( self._greeting(), name )

  def _greet( self, greeting, name ):
    print( '{greeting} {name}!'.format( greeting = greeting, name = name ) )

  def _greeting( self ):
    return self.args.greeting

  def _names( self ):
    return self.args.names

if __name__ == '__main__':
  main()

