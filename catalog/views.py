from typing import Any
from django.shortcuts import render
from .models import Book, Genre, Author, BookInstance
from django.views import generic
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_maintenance = BookInstance.objects.filter(status__exact='m').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_maintenance,
        'num_authors': num_authors,
    }
    return render(request, 'index.html', context=context)
class BookListView(generic.ListView):
    """
    The generic view will query the database to get all records for the specified model (Book)
    then render a template located at 
    /django-locallibrary-tutorial/catalog/templates/catalog/book_list.html (which we will create below).

    Within the template you can access the list of books with the template variable named object_list 
    OR book_list (i.e. generically "<the model name>_list").
    """
    
    model = Book
    
    """Overide method in class base view """    
    # def get_queryset(self):
    #     # Get 5 book containing the title war
    #     return Book.objects.filter(title__icontains='war')[:5]
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        # Call the base implementation first to get the context
        context = super().get_context_data(**kwargs)
        
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context
    
class BookDetailView(generic.DetailView):
    model = Book
    
    def book_detail_view(request, primary_key):
        book = get_object_or_404(Book, pk=primary_key)
        return render(request, 'catalog/book_detail.html', context={'book': book})