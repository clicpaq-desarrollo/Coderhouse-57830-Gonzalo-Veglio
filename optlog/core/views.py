from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html')
 

def admin_panel(request):
    return render(request, 'core/admin_panel.html')