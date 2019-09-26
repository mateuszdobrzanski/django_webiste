from django.shortcuts import render

# inject fake post on the page
posts = [
    {
        'author': 'John Doe',
        'title': 'John Doe first post',
        'content': '''Hello! It's my first post here!''',
        'date': '11/11/12'
    },
    {
        'author': 'John Doe',
        'title': 'second post',
        'content': 'testtesttesttesttesttesttesttesttesttesttesttesttesttest',
        'date': '12/12/12'
    },
]


def home(request):
    context = {
        'data': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
