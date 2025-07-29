from django.views.generic import ListView
from .models import Cheese
from .forms import AddCheeseForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

class CheeseDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Cheese
    template_name = "cheeses/cheese_detail.html"

    def test_func(self):
        return self.get_object().added_by == self.request.user

class CheeseListView(ListView):
    model = Cheese
    template_name = "cheeses/cheese_list.html"
    paginate_by = 5

    def get_queryset(self):
        return Cheese.objects.all().order_by('-created_at')


class CheeseCreateView(LoginRequiredMixin ,SuccessMessageMixin ,CreateView):
    model = Cheese
    form_class = AddCheeseForm
    template_name = "cheeses/cheese_form.html"
    success_message = "¡Queso «%(name)s» creado con éxito!"

    def get_initial(self):
        return {
            "description": "Escribe aquí una descripción breve del queso…",
            "country": "CO",
        }

    def handle_no_permission(self):
        messages.warning(self.request, "Debes iniciar sesión para agregar un queso.")
        return super().handle_no_permission()

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)

class CheeseUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Cheese
    form_class = AddCheeseForm
    template_name = "cheeses/cheese_form.html"
    success_message = "¡Queso «%(name)s» actualizado correctamente!"

    def handle_no_permission(self):
        messages.warning(self.request, "No tienes permiso para editar este queso.")
        return super().handle_no_permission()

    def test_func(self):
        return self.get_object().added_by == self.request.user

class CheeseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Cheese
    template_name = "cheeses/cheese_confirm_delete.html"
    success_url = reverse_lazy("cheese_list")

    def handle_no_permission(self):
        messages.warning(self.request, "No tienes permiso para eliminar este queso.")
        return super().handle_no_permission()

    def test_func(self):
        return self.get_object().added_by == self.request.user

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(request, f"¡Queso «{obj.name}» eliminado!")
        return super().delete(request, *args, **kwargs)
    
class CheeseAddCustomView(LoginRequiredMixin, CreateView):
    model         = Cheese
    form_class    = AddCheeseForm
    template_name = "cheeses/cheese_add_custom.html"
    success_url   = reverse_lazy("cheese_list")

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)