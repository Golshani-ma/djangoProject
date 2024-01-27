from django.shortcuts import render
from website.forms import NameForm, ContactForm, NewsletterForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages


# Create your views here.


def home_view(request):
    return render(request, 'website/index.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # form.cleaned_data['name'] = 'ناشناس'
            form.instance.name = 'ناشناس '
            form.save()
            messages.success(request,'اطلاعات شما با موفقیت ثبت شد.')
        else:
            messages.error(request, 'متاسفانه خطایی پیش آمده. مجددا امتحان کنید.')

    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})


def modify_field_value(value):
    # Perform any modifications to the field value here
    # For example, you can change the value, format it, etc.
    modified_value = 'UNKNOWN'  # Example: Convert to uppercase
    return modified_value


def about_view(request):
    return render(request, 'website/about.html')


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')


def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('OK')
        else:
            return HttpResponse('Error')

    form = ContactForm()
    return render(request, 'test.html', {'form': form})
