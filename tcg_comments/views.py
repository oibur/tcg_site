from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Comment
from .forms import CommentForm

@login_required
def comments(request):
    """Show all comments."""
    comments = Comment.objects.order_by('date_added')
    context = {'comments': comments}
    return render(request, 'tcg_comments/comments.html', context)

@login_required
def new_comment(request):
    """Add a new comment."""
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = CommentForm()
    else:
        #POST data submitted; process data.
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tcg_comments:comments'))

    context = {'form': form}
    return render(request, 'tcg_comments/new_comment.html', context)