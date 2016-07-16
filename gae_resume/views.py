from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

import models
import json


@csrf_exempt
def home(request):
    template = loader.get_template('gae_resume/index.html')
    context = {
        'title': 'GAE - Resume',
        'count': models.get_kudos(),
        'author': 'Yash Raj Singh',
        'why': '',
        'who': '',
        'primary_color_hex': '#FFF',
        'company': '',
        'company_url': 'http://yashrajsingh.net/',
        'work_desc': '',
    }
    return HttpResponse(template.render(context, request))


@csrf_exempt
def kudos(request):
    data = json.loads(request.body)
    # print data
    value = data['count']
    if value in [1]:
        models.add_kudos()

    return JsonResponse({'count': models.get_kudos()})
