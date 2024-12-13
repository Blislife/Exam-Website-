from django.shortcuts import render
from .models import testDate
from .forms import whenTestForm

# Create your views here.
def createTestObject(request):
    if request.method == 'POST':
        form = whenTestForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = whenTestForm()
    return render(request, 'select/select.html', {'form': form})