from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    # success_url = '/'

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return redirect('main:home')