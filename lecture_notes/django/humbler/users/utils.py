
from blog.models import BlogPost


def add_likes(user, liked_blogs):
    for id in liked_blogs:
        blog = BlogPost.objects.get(id=id)
        blog.likes.add(user)
    return liked_blogs
