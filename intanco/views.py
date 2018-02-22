from django.shortcuts import render_to_response, render
from django.core.context_processors import csrf
from adminpanel.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def post(request, post_id):
    root_post = Post.objects.get(id=post_id)

    return render(request, "home/single-post.html",
                              {'post': root_post,
                               'request': request})