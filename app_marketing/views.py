from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView


from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.shortcuts import render,redirect



from .models import Person, Task, User

#REGISTRO DE USUARIO
class UserSignup(FormView):
    template_name = 'app_marketing/signup.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(UserSignup, self).form_valid(form)
    

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('personlist')
        return super(UserSignup, self).get(*args, **kwargs)

# LOGUEO DE USUARIO
class UserLogin(LoginView):
    template_name = 'app_marketing/signin.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('personlist')
    
# CREAR USUARIO
class PersonCreate(LoginRequiredMixin,View):

    def get(self,request):
        return render(request,'app_marketing/person_create_form.html')

    def post(self,request):
        user = User.objects.get(username=request.user)
        my_name = request.POST.get('name')
        user.person_set.create(name=my_name)
        my_object = user.person_set.get(name=my_name).id
        return redirect('persondetail',my_object)

# VER LISTADO DE CLIENTES
class PersonList(LoginRequiredMixin,View):
    def get(self,request):
        account = User.objects.get(username=request.user)
        context = {'person_list':account}
        return render(request,'app_marketing/home.html',context)

# VER SERVICIOS ADQUIRIDOS POR CLIENTE

class PersonDetail(LoginRequiredMixin,DetailView):
    model = Person
    context_object_name = 'person'
    template_name = 'app_marketing/person_detail.html'

    def get(self,*args,**kwargs):
        return super(PersonDetail, self).get(*args,**kwargs)
    
    def post(self,*args,**kwargs):
        return super(PersonDetail, self).get(*args,**kwargs)

    def dispatch(self,request,pk,*args,**kwargs):
        peep = self.model.objects.get(id=pk)
        if self.request.POST.get('save'):
            for task in peep.task_set.all():
                if request.POST.get(f't{task.id}') == 'clicked':
                    task.is_complete = True
                else:
                    task.is_complete = False
                task.save()

        elif self.request.POST.get('add_item'):
            new = request.POST.get('new_item')
            peep.task_set.create(task=new, is_complete=False)

        elif request.POST.get('delete_this'):
            task_index = request.POST.get('delete_this')
            peep.task_set.get(id=task_index).delete()

        return super(PersonDetail, self).dispatch(request,*args,**kwargs)

# ACTUALIZACION DE CLIENTES
class PersonUpdate(LoginRequiredMixin,UpdateView):
    model = Person
    fields = ['name']
    template_name = 'app_marketing/person_update_form.html'
    success_url = reverse_lazy('personlist')

# BORRAR CLIENTES
class PersonDelete(LoginRequiredMixin,DeleteView):
    model = Person
    success_url = reverse_lazy('personlist')
    template_name = 'app_marketing/person_confirm_delete.html'


