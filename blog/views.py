from datetime import date
from django.shortcuts import render

posts = [
    {
        "slug": "knitting-fun",
        "image": "knitting.jpg",
        "author": "Hannah",
        "date": date(2023, 5, 19),
        "Title": "Knitting",
        "exerpt": "There's nothing like the satisfaction you get when knitting anywhere and I wasn't even prepared for what happened when I knitted my last piece!",
        "content": "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Suscipit doloremque vel culpa! Error excepturi perspiciatis maxime provident quasi voluptas qui debitis dolorem cum. Amet voluptas adipisci nam, eligendi minima officiis!",
    }
]

# Create your views here.


def starting_page(request):
    return render(request, "blog/index.html")


def posts(request):
    return render(request, "blog/all-posts.html")


def post_detail(request, slug):
    return render(request, "blog/post-detail.html")
