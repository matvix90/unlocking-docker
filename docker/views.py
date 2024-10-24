from django.views.generic import TemplateView, ListView
from .models import Tag

class Home(ListView):
    template_name = "templates/index.html"
    model = Tag
    context_object_name = "tags"
    