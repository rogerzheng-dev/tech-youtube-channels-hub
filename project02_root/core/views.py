from django.shortcuts import render
from .forms import ContactForm

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    submitted = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            submitted = True
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {
        'form': form,
        'submitted': submitted,
    })