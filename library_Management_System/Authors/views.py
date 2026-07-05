from django.shortcuts import render, get_object_or_404
from .models import Author

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', {'authors': authors})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'author_detail.html', {'author': author})