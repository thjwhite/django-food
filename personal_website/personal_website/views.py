from django.shortcuts import render

from blog.models import BlogEntry


def main(request):
    latest_blog_list = BlogEntry.objects.order_by('-date_published')[:5]
    context = {
        'latest_blog_list': latest_blog_list
    }
    return render(request, 'personal_website/base_blog.html', context)
