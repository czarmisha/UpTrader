from django.shortcuts import render


def my_view(request):
    context = {'foo': 'bar'}
    return render(request, 'base.html', context)

def test_view(request):
    context = {'foo': 'bar'}
    return render(request, 'menu/test.html', context)
