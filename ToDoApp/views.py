from django.shortcuts import render,redirect
from .models import Tasks
from .forms import TaskForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime,date
# Create your views here.


def inputtask(request):
	frm = TaskForm()
	return render(request,'input.html',{'form':frm})
	#return render(request,'input.html')



@csrf_exempt
def savetask(request):
	a=request.POST.get("title")
	b=request.POST.get("date")
	c=request.POST.get("time")

	obj = Tasks(title=a,date=b,time=c)
	obj.save()
	messages.success(request,"\N{grinning face}  "+"New Task \""+obj.title+"\" added.")
	return redirect('/show/')

def showtask(request):
	obj= Tasks.objects.order_by('date','time')

	for i in obj:
		if (i.date)<date.today():
			i.expired=True
			i.save()

		elif (i.date)==date.today() and (i.time)<datetime.now().time():
			i.expired=True
			i.save()
		else:
			i.expired=False
			i.save()

	return render(request,'index.html',{'Data':obj})

@csrf_exempt
def delete(request,id):
	obj = Tasks.objects.get(id=id)
	
	if request.method=="POST":
		msg="\N{pensive face}"+"Task \""+obj.title+"\" deleted."
		obj.delete()
		messages.warning(request,msg)
		return redirect('/show/')

	return render(request,'delete.html',{'obj':obj})


@csrf_exempt
def update(request,id):
	obj = Tasks.objects.get(id=id)
	form = TaskForm(instance = obj)

	if request.method=="POST":
		obj.title=request.POST.get("title")
		obj.date=request.POST.get("date")
		obj.time=request.POST.get("time")
		obj.complete=False
		
		obj.save()
		messages.info(request,"\N{winking face} "+"Task \""+obj.title+"\" updated successfully.")
		return redirect('/show/')

	return render(request,'update.html',{'frm':form,'obj':obj})


@csrf_exempt
def deleteall(request):
	obj = Tasks.objects.all()
	
	if request.method=="POST":
		obj.delete()
		messages.warning(request,"All the Tasks have been deleted.")
		return redirect('/show/')

	return render(request,'remove.html',{'obj':obj})


@csrf_exempt
def complete(request,a,id):
	obj = Tasks.objects.get(id=id)
	
	if request.method=="POST":
		if a==obj.title:
			obj.complete=True
			msg="\N{grinning face}  "+"Task \""+obj.title+"\" Completed."
			messages.success(request,msg)
		else:
			obj.complete=False
			msg="\N{pensive face}  "+"Task \""+obj.title+"\" NOT completed yet."
			messages.warning(request,msg)
		obj.save()
		
		return redirect('/show/')





	

