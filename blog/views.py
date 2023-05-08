from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def home_view(request):
    all_posts = BlogPost.objects.all().order_by('-created')
    slider_posts = BlogPost.objects.filter(status='slider').order_by('-created')
    per_page = 4
    paginator = Paginator(all_posts, per_page)
    page_number = request.GET.get('page')
    try:
        posts = paginator.get_page(page_number)
    except PageNotAnInteger:
        posts = paginator.page_number(1)
    except:
        posts = paginator.page_number(paginator.num_pages)
    context = {'posts': posts, 'slider_posts':slider_posts,}
    return render(request, 'blog/index.html', context)

def single_post(request, blog_slug):
    post_details = get_object_or_404(BlogPost, slug=blog_slug)
    template_name = 'blog/blog-single.html'
    context = {'post_details':post_details}
    return render(request, template_name, context)


def category_view(request, category_slug):
    all_categories = PostCategory.objects.all()
    categories = get_object_or_404(PostCategory, slug=category_slug)
    cat_posts = BlogPost.objects.filter(category = categories).order_by('-created')
    per_page = 2
    paginator = Paginator(cat_posts, per_page)
    page = request.GET.get('page')
    try:
        posts_cat = paginator.get_page(page)
    except PageNotAnInteger:
        posts_cat = paginator.page(1)
    except:
        posts_cat = paginator.page(paginator.num_pages)
    context = {
        'posts': posts_cat,
        'cat_posts':cat_posts,
        'all_categories':all_categories,
        }
    return render(request, 'blog/category.html', context)

