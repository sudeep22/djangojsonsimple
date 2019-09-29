# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json, yaml, ast

from django.views.generic.edit import FormView
from django.http import HttpResponse

# internal imports
from .forms import IndexForm


class IndexView(FormView):
    """
        Render Basic template to show form for JSON and YAML creation
    """
    form_class = IndexForm
    template_name = 'index.html'
    data = None

    def form_valid(self, form):
        """If the form is valid, return YAML/JSON file."""

        self.data = form.cleaned_data
        json_data = json.dumps(self.data)
        if self.data['export_type'] == 'json':
            return HttpResponse(json_data, content_type='application/json')
        else:
            data = ast.literal_eval(json_data)
            return HttpResponse(yaml.dump(data), content_type='application/yaml')
