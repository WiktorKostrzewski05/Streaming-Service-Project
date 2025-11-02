from django.views.generic import ListView
from django.db.models import Q
from mediaApp.models import Content, Genre


class SearchResultsListView(ListView):
    model = Content
    context_object_name = 'content_list'
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        content = Content.objects.filter(
            Q(con_title__icontains=query) | 
            Q(con_description__icontains=query))
        return content
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context