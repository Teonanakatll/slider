from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from slider_app.forms import MicromodalForm
from slider_app.models import LogoAndContacts, Soc, SliderItem



def home(request):
    info = LogoAndContacts.objects.latest('id')
    soc_accs = Soc.objects.all()
    slider_items = SliderItem.objects.all()
    form = MicromodalForm
    return render(request, 'slider_app/index.html', {'form': form, 'info': info, 'soc_accs': soc_accs, 'slider_items': slider_items})

class MessageView(CreateView):
    form_class = MicromodalForm
    template_name = 'slider_app/index.html'
    success_url = reverse_lazy('home')
