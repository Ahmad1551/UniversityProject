import json
import random

import requests
from django.shortcuts import render
from django.views import View

from edu.models import Bot, Subscription


class CheggView(View):
    initial = {'key': 'value'}
    template_name = 'chegg_view.html'
    api_url = ['https://Chegg.muhammadahmad6.repl.co']

    def get(self, request, *args, **kwargs):
        subscription = Subscription.objects.filter(user_id=request.user.id, plan__bot_id=1).first()
        bots = Bot.objects.all()
        return render(request, self.template_name, {'subscription': subscription, 'bots': bots})

    def post(self, request, *args, **kwargs):
        que_url = request.POST.get('chegg-search')
        subscription = Subscription.objects.filter(user_id=request.user.id, plan__bot_id=1).first()
        bots = Bot.objects.all()
        chegg_solution_api = requests.post(f'{random.choice(self.api_url)}/v1/grab-sol', headers={
            'content-type': 'application/json'}, data=json.dumps({'url': que_url})).json()
        return render(request, self.template_name, {'unlock': chegg_solution_api, 'subscription': subscription, 'bots': bots})
