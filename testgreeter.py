
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
    self.args.name = mock.sentinel.Name

    self.greeter = greeter.Greeter( self.args )
    self.greeter._greet = mock.Mock()

  def testGreeting( self ):
    self.greeter()

    self.greeter._greet.assert_called_once_with( mock.sentinel.Greeting, mock.sentinel.Name )

