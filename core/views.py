from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from core.forms import WordForm
from core.models import Dictionary, Word


class HomeView(TemplateView):
    template_name = 'core/home.html'


class DictionariesView(ListView):
    template_name = 'core/dictionaries.html'
    context_object_name = 'dictionaries'
    paginate_by = 10

    def get_queryset(self):
        return Dictionary.objects.filter(owner=self.request.user)


class DictionaryView(DetailView):
    model = Dictionary
    template_name = 'core/dictionary.html'
    context_object_name = 'dictionary'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = WordForm()
        return context


def add_word(request):
    if request.method == 'POST':
        form = WordForm(request.POST)
        dictionary = Dictionary.objects.get(pk=request.POST.get('dictonary'))
        if form.is_valid():
            word = form.save(commit=False)
            word.dictionary = dictionary
            word.save()
            return redirect('dictionary', pk=dictionary.pk)


def delete_word(request, pk):
    word = Word.objects.get(pk=pk)
    word.delete()
    return redirect('dictionary', pk=word.dictionary.pk)
