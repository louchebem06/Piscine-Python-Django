from django.shortcuts import render
from .forms import FileForm
from .models import File

# Create your views here.
def home(request):
    context = dict()
    files = File.objects.all()
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = FileForm()
    context['form'] = form
    context['files'] = files
    return render(request, 'ex/home.html', context)