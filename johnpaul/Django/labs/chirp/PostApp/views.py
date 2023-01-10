from django.shortcuts import render
from django.contrib.auth.decorators import login_required




posts = [{
    'author': 'Mike64',
    'title': 'My first blog post',
    'date_posted': 'January 2, 2023',
    'content': 'Lorem ipsum'
},
    {
    'author': 'Testuser01',
    'title': 'New Year resolutions loading',
    'date_posted': 'January 1, 2023'
}
]


# Home
@login_required
def post_home(request):
    context = {
        'posts': posts
    }
    return render(request, 'PostApp/post_home.html', context)



# Create
def post_create(request):
    return render(request, 'PostApp/post_create.html')



# Detail
def post_detail(request):
    return render(request, 'PostApp/post_detail.html')



# Update


# Delete


