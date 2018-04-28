from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Ngo
from django.urls import reverse_lazy
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login
from django.views.generic import View 
from .forms import UserForm

class IndexView(generic.ListView):
    template_name='ngo/index.html'
    context_object_name='all_ngos'

    def get_queryset(self):
        return Ngo.objects.all()

class DetailView(generic.DetailView):
    model=Ngo
    template_name='ngo/detail.html'

class NgoCreate(CreateView):
    model=Ngo
    fields=['ngo_name','ngo_logo','ngo_loc','ngo_relieftype']

class NgoDelete(DeleteView):
    model=Ngo
    success_url=reverse_lazy('ngo:index')

class UserFormView(View):
    form_class=UserForm
    template_name='ngo/registration.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():

            user=form.save(commit=False)

            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #return user object if correct
            user=authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('ngo:index')

        return render(request,self.template_name,{'form':form})        



