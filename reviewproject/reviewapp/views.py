from django.shortcuts import render,redirect
from django.http import HttpResponse

from . import models


def index(request):
    return HttpResponse('this is first page')

def fl(request):
    # return HttpResponse('this is test for fl')
    data = models.FLtester.objects.all()
    return render(request, 'fl_data.html', {'data_list':data})

# Create your views here.
# def write_in(request):
#     if request.method == 'GET':
#         return render(request, 'write.html')
def show(request):
    data = models.Manager.objects.all()
    return render(request, 'show_UI.html', {'data_list':data})

def table_cmd(request):
    data = models.Addnewtablefromcmd.objects.all()
    return render(request, 'show_table_from_cmd.html', {'data_list':data})

def fldata(request):
    return HttpResponse('this is test for Fl_data')
    # data = models.FLtester.objects.all()
    # return render(request, 'fl_data.html', {'data_list':data})


def write(request):
    if request.method == "GET":
        return render(request, 'write.html')

    elif request.method == "POST":
        id = request.POST.get('id')
        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')

        models.Manager.objects.create(id=id, name=name, date=date, time=time)
        # return render(request, 'write.html')
        return redirect('/show')
