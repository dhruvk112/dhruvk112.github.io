from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from . import models
from Users.forms import TransferForm
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')

class UserListView(ListView):
    context_object_name = 'users'
    model = models.Users

class UserDetailView(DetailView):
    context_object_name = 'user_detail'
    model = models.Users
    template_name = 'Users/user_detail.html'

class TransactionListView(ListView):
    context_object_name = 'transactions'
    model = models.Transfers

class UserTransferView(CreateView):
    form_class = TransferForm
    model = models.Transfers
    
    def get_initial(self,**kwargs):
        person = get_object_or_404(models.Users,pk=self.kwargs.get('pk'))
        self.initial.update({
            'person1': person.name,
            'amount': 0
        })
        
        return super(UserTransferView, self).get_initial()

    
        

        

    

    
    


