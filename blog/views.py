import datetime
from django.db.models import Q
from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm


def post_list(request):
    qs = Post.objects.all()

    query = request.GET.get('query', '')
    if query:
        condition = Q(title__icontains=query) | Q(content__icontains=query)
        qs = qs.filter(condition)

    date_list = []
    for i in range(365):
        date = datetime.datetime(2017, 1, 1) + datetime.timedelta(days=i)
        date_list.append(date)

    return render(request, 'blog/post_list.html', {
        'post_list': qs,
        'query': query,
        'date_list': date_list,
    })


def post_detail(request, pk):
    # pk = "100"  # /blog/100/
    # post = Post.objects.get(id=pk)
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post': post,
    })


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
    # if request.method == 'GET':
        form = PostForm()

    return render(request, 'blog/post_form.html', {
        'form': form,
    })

# from django.views.generic import CreateView
# post_new = CreateView.as_view(model=Post, form_class=PostForm, success_url='/weblog/')
# post_new = CreateView.as_view(model=Post, form_class=PostForm)  # get_absolute_url을 활용


def post_edit(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        # if request.method == 'GET':
        form = PostForm(instance=post)

    return render(request, 'blog/post_form.html', {
        'form': form,
    })


def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:post_list')
    return render(request, 'blog/post_confirm_delete.html', {
        'post': post,
    })

