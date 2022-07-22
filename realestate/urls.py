from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('company', views.company, name='会社概要'),
    path('property', views.PropertyView.as_view(), name='物件一覧'),
    path('contact', views.contact, name='お問い合わせ'),
    path('member', views.member, name='会員登録'),
    path('login', views.login, name='ログイン'),
    path('complete',views.complete, name='送信'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
]
