from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic.edit import FormMixin

from django.views.generic import DetailView, ListView

from .forms import ComposeForm
from .models import Thread, ChatMessage


class InboxView(LoginRequiredMixin, ListView):
    template_name = 'chat/inbox.html'
    
    def get_queryset(self):
        return Thread.objects.by_user(self.request.user).order_by('-updated')

class ThreadView(LoginRequiredMixin, FormMixin, DetailView):
    template_name = 'chat/thread.html'
    form_class = ComposeForm

    def get_success_url(self, *args, **kwargs):
        kwargs = {'username': self.kwargs.get("username")}
        return reverse_lazy('chat:thread', kwargs=kwargs)


    def get_queryset(self):
        return Thread.objects.by_user(self.request.user)

    def get_object(self):
        other_username  = self.kwargs.get("username")
        user = self.request.user
        if other_username == user.username:
            raise Http404
        obj, created    = Thread.objects.get_or_new(user, other_username)
        if obj == None:
            raise Http404
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['threads'] = Thread.objects.by_user(self.request.user).order_by('-updated')
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        thread = self.get_object()
        user = self.request.user
        message = form.cleaned_data.get("message")
        thread.updated = timezone.now
        thread.save()
        ChatMessage.objects.create(user=user, thread=thread, message=message)
        return super().form_valid(form)


