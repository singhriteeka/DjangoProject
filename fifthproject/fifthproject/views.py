from django.shortcuts import render

def home_view(request) :
    return render(request, 'home.html',context ={
        'name':'riteeka singh',
        'id':1008,
        'course':'BscITM',
        'college':'lit',
        'age':19,
        'marks':[22,33,44,55]
    })