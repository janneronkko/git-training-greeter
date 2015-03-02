
from __future__ import division, print_function, unicode_literals, absolute_import

from unittest import TestCase

import greeter
try:
  from unittest import mock
except ImportError:
  import mock


class TestGreeter( TestCase ):
  def setUp( self ):
    TestCase.setUp( self )

    self.args = mock.Mock()
    self.args.greeting = mock.sentinel.Greeting
    self.args.names = [ mock.sentinel.Name1, mock.sentinel.Name2 ]

    self.greeter = greeter.Greeter( self.args )
    self.greeter._greet = mock.Mock()

  def testGreeting( self ):
    self.greeter()

    self.assertListEqual(
      self.greeter._greet.call_args_list,
      [
        mock.call( mock.sentinel.Greeting, mock.sentinel.Name1 ),
        mock.call( mock.sentinel.Greeting, mock.sentinel.Name2 ),
      ]
    )

