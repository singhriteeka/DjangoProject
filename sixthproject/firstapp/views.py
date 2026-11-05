from django.shortcuts import render

# Create your views here.
def index_view(request):
    student_data = [{
        'name':'riteeka',
        'id':1008,
        'mail':'riteeka@gmail.com',
    },{
        'name':'riteeka1',
        'id':1080,
        'mail':'riteekasingh@gmail.com',
    },{
        'name':'riteeka2',
        'id':1088,
        'mail':'singhriteeka@gmail.com',
    }]
    return render(request,'index.html',{
        'name':'riteekasingh',
        'id':1008,
        'marks':[10,20,30],
        'add':{
            'at':'pbc',
            'pod':'xyz',
            'pin':751013
        },
        'student_data':student_data
    })

from django.http import HttpResponse
def add(r,first,second):
    return render(r,'add.html',{
        'first':first,
        'second':second
    })