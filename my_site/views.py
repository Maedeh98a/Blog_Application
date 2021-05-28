from django.shortcuts import render, get_object_or_404
from my_site.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView


def list_of_post(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {"posts": posts, 'pages': page}
    return render(request, 'my_site/post_list.html', context)


def post_detail(request, day, month, year, post):
    post = get_object_or_404(Post, slug=post, publish__year=year, publish__month=month, publish__day=day , status='publish')
    return render(request, 'my_site/detail.html', {'post': post})


class PostView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'my_site/post_list.html'

