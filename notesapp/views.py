from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,DeleteView,UpdateView,DetailView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache


from .models import Notes
from .forms import *



class NotesListView(LoginRequiredMixin,ListView):
    model = Notes
    template_name = "notes_list.html"
    context_object_name = "notes"

    def get_queryset(self):
        query = self.request.GET.get("search")
        user = self.request.user
        if query:
            return Notes.objects.filter(user = user, title__icontains = query)
        users_note = Notes.objects.filter(user=user)
        return users_note


class NotesCreateView(LoginRequiredMixin,CreateView):
    model = Notes
    form_class = NotesCreateForm
    template_name = "notes_creation_update.html"
    success_url = reverse_lazy("notes-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
    
class NotesUpdateView(LoginRequiredMixin,UpdateView):
    model = Notes
    form_class = NotesCreateForm 
    template_name = "notes_creation_update.html"
    success_url= reverse_lazy("notes-list")

class NotesDeleteView(LoginRequiredMixin,DeleteView):
    model = Notes
    template_name = "notes_delete.html"
    context_object_name = "notes"
    success_url = reverse_lazy("notes-list")

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['note_to_delete'] = self.get_object()
        context['notes'] = Notes.objects.filter(user = self.request.user)

        return context
    

class UserCreateView(View):
    template_name="auth/register.html"


    def get(self,request):
        user_form = UserCreateForm()
        profile_form = ProfileForm()

        return render(request,self.template_name,{"user_form":user_form,"profile_form":profile_form})
    def post(self,request):
        user_form = UserCreateForm(request.POST)
        profile_form = ProfileForm(request.POST,request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)  ## prepare a copy ,not to save
            profile.user = user
            profile.save()
            # messages.success(request, "Account created successfully! You can now log in.")
            login(request,user=user)
            return redirect("notes-list")
        return render(
            request, 
            self.template_name, 
            {"user_form": user_form, "profile_form": profile_form}
        )
    

class UserUpdateView(LoginRequiredMixin,UpdateView):
    template_name="auth/update.html"

    def get(self,request):
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

        return render(request,self.template_name,{"user_form":user_form,"profile_form":profile_form})
    def post(self,request):
        user_form = UserUpdateForm(request.POST , instance=request.user)
        profile_form = ProfileForm(request.POST,request.FILES , instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            temp_profile = profile_form.save(commit=False)  ## prepare a copy ,not to save
            temp_profile.user = user
            temp_profile.save()
            # messages.success(request, "Account created successfully! You can now log in.")
            return redirect("notes-list")
        return render(
            request, 
            self.template_name, 
            {"user_form": user_form, "profile_form": profile_form}
        )
    