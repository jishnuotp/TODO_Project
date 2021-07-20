from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TodoForm
from.models import Task
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task1'

class Taskdetailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'

class Taskupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})


def home(request):
    task = Task.objects.all()
    if request.method=='POST':
        name = request.POST.get('name','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date','')
        task2 = Task(name=name,priority=priority,date=date)
        task2.save()
    return render(request,'home.html',{'task1':task})

def update(request,task_id):
    task = Task.objects.get(id=task_id)
    form = TodoForm(request.POST or None,request.FILES,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form1':form,'task1':task})

def delete(request,id):
    task = Task.objects.get(id=id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')