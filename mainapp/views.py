import json
import random
import string

from django.shortcuts import render

from .documents import ProductDocument
from .models import Product


def load_json_data():
    with open('data.json', 'r', encoding='utf-8') as f:
        data_list = json.load(f)
        data_list = data_list["products"][:10]
    return data_list


def generate_random_string(length):
    characters = string.ascii_lowercase[:5] + " "
    return ''.join(random.choices(characters, k=length))


def create_model_instances(data_list):
    model_instances = []
    for data in data_list:
        instance = Product(
            name=data.get("name"),
            supplier=data.get("supplier"),
            rating=data.get("reviewRating"),
            text=generate_random_string(100)
        )
        model_instances.append(instance)
    return model_instances


def index(request):
    Product.objects.bulk_create(create_model_instances(load_json_data()))
    return render(request, 'mainapp/create.html')


def elastic(request):
    q = request.GET.get('q')
    context = {}
    if q:
        s = ProductDocument.search().query('match', name=q)
        context['products'] = s
    return render(request, 'target/elastic.html', context)