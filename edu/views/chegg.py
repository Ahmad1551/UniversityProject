from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View


class CheggView(View):
    initial = {'key': 'value'}
    template_name = 'chegg_view.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)
