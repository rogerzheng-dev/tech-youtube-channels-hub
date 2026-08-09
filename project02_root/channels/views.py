from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Channel
from .forms import ChannelForm
from django.contrib.auth.mixins import LoginRequiredMixin

class ChannelListView(ListView):
    model = Channel
    template_name = 'channels/channel_list.html'
    context_object_name = 'channels'

    def get_queryset(self):
        queryset = Channel.objects.all()
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(name__icontains=query)

        return queryset

class ChannelDetailView(DetailView):
    model = Channel
    template_name = 'channels/channel_detail.html'
    context_object_name = 'channel'

class ChannelCreateView(LoginRequiredMixin, CreateView):
    model = Channel
    form_class = ChannelForm
    template_name = 'channels/channel_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ChannelUpdateView(UpdateView):
    model = Channel
    form_class = ChannelForm
    template_name = 'channels/channel_form.html'

class ChannelDeleteView(DeleteView):
    model = Channel
    template_name = 'channels/channel_confirm_delete.html'
    success_url = reverse_lazy('channel_list')