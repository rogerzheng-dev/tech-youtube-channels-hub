from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Review
from .forms import ReviewForm
from channels.models import Channel

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.channel = get_object_or_404(Channel, slug=kwargs['slug'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.channel = self.channel
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('channel_detail', kwargs={'slug': self.channel.slug})

class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_form.html'

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.user

    def get_success_url(self):
        return reverse('channel_detail', kwargs={'slug': self.object.channel.slug})

class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = 'reviews/review_confirm_delete.html'

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.user

    def get_success_url(self):
        return reverse_lazy('channel_detail', kwargs={'slug': self.object.channel.slug})