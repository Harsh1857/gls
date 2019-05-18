# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory
from .views import Home

# Create your tests here.

class TestHomeGlsPage(TestCase):
    def  setUp(self):
        self.factory = RequestFactory()

    def test_gls_home_page_lending(self):
        request = self.factory.get('/')
        response = Home.as_view()(request)
        self.assertEqual(response.status_code, 200)
