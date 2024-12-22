from django.shortcuts import render, get_object_or_404
from .models import Post
from .utils import binary_search, bubble_sort


def post_list(request):
    sort_by = request.GET.get('sort', 'id')
    search_query = request.GET.get('search', '')

    # if search_query:
    #     posts = Post.objects.all().order_by('title')
    #     titles = [post.title for post in posts]
    #     s_index = binary_search(titles, search_query)
    #     if s_index != -1:
    #         s_posts = posts[s_index]
    #         posts = [s_posts]
    #     else:
    #         posts = []
    # elif sort_by == 'id':
    #     bubble_sort(posts_list, key=lambda post: post.title.lower())
    #     posts = Post.objects.all().order_by('id')
    # elif sort_by == 'title':
    #     posts = Post.objects.all().order_by('title')
    # else:
    #     posts = Post.objects.all()

    if search_query:
        posts = Post.objects.all().order_by('title')
        titles = [post.title for post in posts]
        s_index = binary_search(titles, search_query)
        if s_index != -1:
            s_posts = posts[s_index]
            posts = [s_posts]
        else:
            posts = []
    else:
        posts = Post.objects.all()

    posts_list = list(posts)

    if sort_by == 'id':
        bubble_sort(posts_list, key=lambda post: post.id)
        #posts = Post.objects.all().order_by('id')
    elif sort_by == 'title':
        bubble_sort(posts_list, key=lambda post: post.title.lower())
        #posts = Post.objects.all().order_by('title')

    return render(request, 'posts/post_list.html', {'posts': posts_list, 'sort_by': sort_by, 'search_query': search_query})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})

