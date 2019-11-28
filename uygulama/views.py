from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponsePermanentRedirect, redirect
from uygulama.models import uygulama
from uygulama.forms import UygulamaForm
from django.contrib import messages

def uygulama_index(request):
    uygulamalar= uygulama.objects.all()
    return render(request,'uygulama/index.html', {'uygulamalar': uygulamalar})

def uygulama_detail(request, id):
    Uygulama = get_object_or_404(uygulama, id=id)
    context = {
        'uygulama': Uygulama,
    }
    if request.GET.get('Next') == 'Kişi Listesine Dön':
        return redirect('uygulama:index')
    return render(request, 'uygulama/detail.html',context)
def uygulama_create(request):
    if request.method=="POST":
        form = UygulamaForm (request.POST)
        if form.is_valid():
            Uygulama =form.save()
            messages.success(request, 'Kişi kaydı başarılı bir şekilde oluşturulmuştur.')
            return HttpResponsePermanentRedirect(Uygulama.get_absolute_url())
    else:
        form = UygulamaForm()
    context = {
        'form': form,
    }
    return render(request, 'uygulama/form.html', context)
def uygulama_update(request, id):
    Uygulama = get_object_or_404(uygulama, id=id)
    form = UygulamaForm(request.POST or None, instance=Uygulama)
    if form.is_valid():
        form.save()
        messages.success (request, 'Kişi güncellemesi başarılı bir şekilde gerçekleştirilmiştir', extra_tags='mesaj-basarili')
        return HttpResponsePermanentRedirect(Uygulama.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'uygulama/form.html', context)
def uygulama_delete(request, id):
    Uygulama = get_object_or_404(uygulama, id=id)
    Uygulama.delete()

    return redirect('uygulama:index')