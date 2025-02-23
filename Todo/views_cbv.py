from django.views.generic import TemplateView

class IndexPageView(TemplateView):
    template_name = 'index.html'
    extra_context = { 'title': "Aplicació To-Do" }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
