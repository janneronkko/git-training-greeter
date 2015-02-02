
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
    self.args.randomGreetin = False

    self.greeter = greeter.Greeter( self.args )
    self.greeter._greet = mock.Mock()

  def testGreeting( self ):
    self.greeter()

    self.greeter._greet.assert_called_once_with( mock.sentinel.Greeting, mock.sentinel.Name )

  def testRandomGreeting( self ):
    self.args.randomGreetin = True
    self.greeter()

    args, kwargs = self.greeter._greet.call_args

    greeting, name = args

    self.assertTrue( len( kwargs ) == 0 )
    self.assertNotEqual( greeting, mock.sentinel.Greeting )
    self.assertEqual( name, mock.sentinel.Name )

  def testRandomGreetingGeneration( self ):
    calls = 10
    self.args.randomGreetin = True
    prevGreeting = self.greeter._greeting()
    while calls > 0:
      import time
      time.sleep( 0.11 ) # Need to sleep more than 0.1 seconds to make sure enough time has passed so that the random greeting is changed
      greeting = self.greeter._greeting()
      self.assertNotEqual( prevGreeting, greeting )
      prevGreeting = greeting
      calls -= 1

