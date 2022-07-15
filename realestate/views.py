from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls.base import reverse_lazy
# from django.views.generic import TemplateView
# from django.views.generic.edit import FormView
# from .forms import ContactForm


def contact(request):
  if request.method == "POST":
    sub = "問い合わせがありました"
    message = "件名 : "+request.POST.get('title')+"\n\n氏名 : "+request.POST.get('name')+"\n\nメールアドレス : "+request.POST.get('address')+"\n\n内容 : \n"+request.POST.get('message')
    from_email = "yuhi.kikake@gmail.com"
    recipient_list = [
        "yuhi.kikake@gmail.com"
    ]

    send_mail(sub , message, from_email, recipient_list)
    return render(request, 'realestate/complete.html')
  return render(request, 'realestate/contact.html')


# class contact(LoginRequiredMixin, FormView):
#     template_name = "realestate/contact.html"
#     form_class = ContactForm
#     success_url = reverse_lazy("realestate:pycomplete")

#     def form_valid(self, form):
#         form.send_email(
#             username=self.request.user.username, 
#             email=self.request.user.email
#         )
#         return super().form_valid(form)

# class complete(LoginRequiredMixin, TemplateView):
#     template_name = "realestate/complete.html"



def index(request):
    params = {
        'company': '会社概要',
        'property': '物件一覧',
        'contact': 'お問い合わせ',
        'member': '会員登録',
        'login': 'ログイン',
        'complete':'送信',
    }
    return render(request, 'realestate/index.html', params)


def company(request):
    params = {
        'company': 'INDEX',
    }

    return render(request, 'realestate/company.html', params)

def property(request):
    params = {
        'property': 'INDEX',
    }

    return render(request, 'realestate/property.html', params)


def member(request):
    params = {
        'member': 'INDEX',
    }

    return render(request, 'realestate/member.html', params)

def login(request):
    params = {
        'login': 'INDEX',
    }

    return render(request, 'realestate/login.html', params)

def complete(request):
    params = {
        'complete': 'INDEX',

    }

    return render(request, 'realestate/complete.html', params)