from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import UserProfile
from .forms import UserChangeCustomForm, UserProfileForm

class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'usuarios/user_list.html'
    context_object_name = 'users'

class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserChangeCustomForm
    template_name = 'usuarios/user_form.html'
    success_url = reverse_lazy('usuarios:user_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        
        UserProfile.objects.create(user=self.object)
        return response

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserChangeCustomForm
    template_name = 'usuarios/user_form.html'
    success_url = reverse_lazy('usuarios:user_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_form'] = UserProfileForm(instance=self.object.userprofile)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        profile_form = UserProfileForm(request.POST, request.FILES, instance=self.object.userprofile)
        if form.is_valid() and profile_form.is_valid():
            return self.form_valid(form, profile_form)
        else:
            return self.form_invalid(form, profile_form)

    def form_valid(self, form, profile_form):
        response = super().form_valid(form)
        profile_form.save()
        return response

    def form_invalid(self, form, profile_form):
        context = self.get_context_data()
        context['profile_form'] = profile_form
        return self.render_to_response(context)

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('usuarios:user_list')
