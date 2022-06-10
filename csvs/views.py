from django.shortcuts import render
from .forms import CsvModelForm
from .models import  Csv
#from django.http import HttpResponse

# Create your views here.
def upload_file_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
    return render(request, 'csvs/upload.html', {'form': form})