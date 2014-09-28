#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import TestCase
import views

class EchoTestCase(TestCase):
    def setUp(self):
        pass

    def test_echo_happy_path(self):
        result = views.echo("John")
        self.assertTrue("Hello John! The time is " in result) 
        self.assertEquals(len(result), 51)
