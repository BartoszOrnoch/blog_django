from django.shortcuts import render


posty = [
    {
        'name': 'bartek',
        'surname': 'ornoch',
        'birth': '14.06.1996'
    },
    {
        'name': 'Ian',
        'surname': 'Nepomniatchi',
        'birth': '01.01.1991'
    }

]


def home(request):
    context = {
        'posts': posty
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
