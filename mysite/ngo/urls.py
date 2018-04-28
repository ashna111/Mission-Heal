from django.urls import path
from . import views

app_name='ngo'

urlpatterns = [
    path('', views.IndexView.as_view() , name='index'),
    path('<int:pk>/',views.DetailView.as_view(),name='detail'),

    path('ngo/add/',views.NgoCreate.as_view(),name='ngo-add'),

    path('<int:pk>/delete/',views.NgoDelete.as_view(),name='ngo-delete'),

    path('signup',views.UserFormView.as_view(),name='user-sign-up')
]
