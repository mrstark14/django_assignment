from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template import loader

from .models import TodoList
from .models import TodoItem

# Create your views here.

#->before template
# def index(request):
#     todolists = TodoList.objects.all()
#     list_items=TodoItem.objects.all()

#     output=', '.join(item.title for item in list_items) 
#     return HttpResponse(output)

# after template
def index(request):
    todolists = TodoList.objects.all()
    items = TodoItem.objects.all()
    template = loader.get_template('todo/index.html')
    context = {
        'todolists': todolists,
        'todoitems': items,
    }

    return HttpResponse(template.render(context,request)) #this or->
    #return render(request, 'todo/index.html',context)


def detail(request,list_id):
    try:
        todolist=TodoList.objects.get(id=list_id)
    except:
        raise Http404("This List Does not exist")
    items_list=TodoItem.objects.filter(todo_list=todolist)
    context={
        'todolist':todolist,
        'items_list':items_list
    }
    return render(request, 'todo/detail.html',context)


def createlist(request):
    if request.method == "GET":
        return render(request, 'todo/createlist.html')

    name = request.POST["name"]
    TodoList.objects.create(list_name=name)
    lists = TodoList.objects.all()
    context = {
        'todolists': lists,
    }
    return render(request, 'todo/index.html', context)


def createitem(request):
    if request.method == "GET":
        todolists = TodoList.objects.all()
        items = TodoItem.objects.all()
        context = {
        'todolists': todolists,
        'todoitems': items,
        }
        return render(request, 'todo/createitem.html', context)
    title_name=request.POST['title']
    duedate=request.POST['due_date']
    list_id=int(request.POST['list_id'])
    check=request.POST['checked']
    t=TodoList.objects.get(id = list_id)
    if check=="yes":
        TodoItem.objects.create(title=title_name,checked=True,due_date=duedate,todo_list=t)
    else:
        TodoItem.objects.create(title=title_name,checked=False,due_date=duedate,todo_list=t)
    lists = TodoList.objects.all()
    context = {
        'todolists':lists,
    }
    return render(request, 'todo/index.html', context)
def deletelist(request, list_id):
    try:
        todolist=TodoList.objects.get(id=list_id)
    except:
        raise Http404("This List Does not exist")
    todolist.delete()
    todolists = TodoList.objects.all()
    items = TodoItem.objects.all()
    template = loader.get_template('todo/index.html')
    context = {
        'todolists': todolists,
        'todoitems': items,
    }
    return HttpResponse(template.render(context,request))    
def deleteitem(request, list_id, item_id):
    try:
        todoitem=TodoItem.objects.get(id=item_id)
    except:
        raise Http404("This Item Does not exist")
    todoitem.delete()
    try:
        todolist=TodoList.objects.get(id=list_id)
    except:
        raise Http404("This List Does not exist")
    items_list=TodoItem.objects.filter(todo_list=todolist)
    context={
        'todolist':todolist,
        'items_list':items_list
    }
    return render(request, 'todo/detail.html',context)
def updatelist(request, list_id):
    try:
        todolist=TodoList.objects.get(id=list_id)
    except:
        raise Http404("This List Does not exist")
    context={
        'todolist':todolist,
    }
    if request.method == "GET":
        return render(request, 'todo/updatelist.html', context)
    name = request.POST["name"]
    todolist.list_name=name
    todolist.save()
    todolists = TodoList.objects.all()
    items = TodoItem.objects.all()
    template = loader.get_template('todo/index.html')
    context = {
        'todolists': todolists,
        'todoitems': items,
    }
    return HttpResponse(template.render(context,request)) 

def updateitem(request, item_id, List_id):
    try:
        todoitem = TodoItem.objects.get(id = item_id)
    except:
        raise Http404("This item does not exist")
    try:
        Todolist = TodoList.objects.get(id = List_id)
    except:
        raise Http404("This List does not exist")
    if request.method == "GET":
        todolists = TodoList.objects.all()
        context={
            'todoitem':todoitem,
            'todolists':todolists,
            'Todolist': Todolist,
        }
        return render(request, 'todo/updateitem.html', context)
    title_name=request.POST['title']
    duedate=request.POST['due_date']
    list_id=int(request.POST['list_id'])
    check=request.POST['checked']
    t=TodoList.objects.get(id = list_id)
    if check == "yes":
        todoitem.title = title_name
        todoitem.save()
        todoitem.due_date = duedate
        todoitem.save()
        todoitem.checked = True
        todoitem.save()
        todoitem.todo_list = t
        todoitem.save()
    else:
        todoitem.title = title_name
        todoitem.save()
        todoitem.due_date = duedate
        todoitem.save()
        todoitem.checked = False
        todoitem.save()
        todoitem.todo_list = t
        todoitem.save()
    items_list=TodoItem.objects.filter(todo_list=Todolist)
    context={
        'todolist':Todolist,
        'items_list':items_list
    }
    return render(request, 'todo/detail.html',context)