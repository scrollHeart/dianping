from django.shortcuts import render
from models import MerchantItem
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.paginator import Paginator
import json
def index(request):
    return HttpResponse('index')


def listAll(request):
    result = MerchantItem.objects.all()[0:3]
    result = serializers.serialize('json', result)
    result = [x['fields'] for x in json.loads(result)]
    result = json.dumps(result)
    return HttpResponse(result, content_type="application/json")


def listPage(request, page=1, count=20):
    result = MerchantItem.objects.all()
    p = Paginator(result, int(count))
    result = p.page(int(page))
    result = serializers.serialize('json', result)
    result = [x['fields'] for x in json.loads(result)]
    result = json.dumps({
        'page': int(page),
        'totalPage': p.num_pages,
        'data': result,
    })
    return HttpResponse(result, content_type="application/json")