from django.shortcuts import render


def handler404view(request, *args, **argv):
    response = render(request, 'error_pages/404.html')
    response.status_code = 404
    return response


def handler500view(request, *args, **argv):
    response = render(request, 'error_pages/500.html')
    response.status_code = 500
    return response
