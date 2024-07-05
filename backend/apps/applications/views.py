from django.shortcuts import render, get_object_or_404, redirect
from .models import Application

def application_list(request):
    applications = Application.objects.all()
    return render(request, 'applications/application_list.html', {'applications': applications})

def application_detail(request, pk):
    application = get_object_or_404(Application, pk=pk)
    return render(request, 'applications/application_detail.html', {'application': application})

def approve_application(request, pk):
    application = get_object_or_404(Application, pk=pk)
    application.status = 'approved'
    application.save()
    return redirect('application_detail', pk=pk)

def reject_application(request, pk):
    application = get_object_or_404(Application, pk=pk)
    application.status = 'rejected'
    application.save()
    return redirect('application_detail', pk=pk)
