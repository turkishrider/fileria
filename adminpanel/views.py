from django.shortcuts import render, render_to_response, redirect
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.contrib import messages
from django.utils.translation import ugettext as _
from .forms import New_Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, User


@login_required()
def home(request):
    blog_list = Post.objects.filter(which_user=request.user)
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')

    try:
        post_count = paginator.page(page)

    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        post_count = paginator.page(1)

    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        post_count = paginator.page(paginator.num_pages)

    return render_to_response("admin-panel/all-blogs.html",
                              {"blogs": blog_list,
                               "request": request,
                               "post_count": post_count,
                               "read_more": 1})