import random
from django.http import JsonResponse


def generate_code(request):
    code = random.randint(1000, 9999)
    return JsonResponse({"code": code})
