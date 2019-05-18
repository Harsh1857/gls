# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import json

from django.views.generic.base import TemplateView


class Home(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        file_path = os.path.join(os.path.dirname(__file__), 'guide.json')
        
        # Read data from json file into dict format. 
        with open(file_path, 'r') as f:
            data = json.load(f)
        context["steps"] = data["steps"]
                
        return context


