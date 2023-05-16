from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
from django.views.generic import FormView
class cdv_forms(FormView):
    template_name='cdv_forms.html'
    form_class=schoolform
    def form_valid(self,form):
        form.save()
        return HttpResponse('data inserted successfully.....')
