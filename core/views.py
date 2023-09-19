from django.views.generic import TemplateView

from datetime import date

class IndexView(TemplateView):
    template_name = 'index.html'
