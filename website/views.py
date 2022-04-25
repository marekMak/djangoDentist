from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def pricing(request):
    return render(request, 'pricing.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['message-name']
        email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            name,
            message,
            email,
            ['marek1.zubor@gmail.com'],
            fail_silently=False
        )

        return render(request, 'contact.html',{'name':name})

    else:
        return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def blogDetails(request):
    return render(request, 'blog-details.html')