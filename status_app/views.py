
from django.shortcuts import render, redirect, get_object_or_404
from .models import Website
from django.http import JsonResponse
import requests
from .forms import WebsiteForm

def status_page(request):
    websites = Website.objects.all()
    return render(request, 'status_page.html', {'websites': websites})

def check_status(request):
    url = request.GET.get('url', '')
    try:
        response = requests.head(url, timeout=5)
        if response.status_code == 200:
            status = 'Online'
        else:
            status = 'Offline'
    except requests.ConnectionError:
        status = 'Offline'

    return JsonResponse({'status': status})

def add_website(request):
    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('status_page')  # Weiterleitung zur Statusseite nach dem Hinzufügen
    else:
        form = WebsiteForm()

    return render(request, 'add_website.html', {'form': form})

def delete_website(request, website_id):
    website = get_object_or_404(Website, pk=website_id)
    website.delete()
    return redirect('status_page')