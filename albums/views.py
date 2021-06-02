from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView
from .models import Photography, Albums, Photo,  AlbumsDiv
from .forms import EmailAlbumForm


# Create your views here.


class PhotagraphyView:


    def get_photography_all(self):
        """Выводим список фотосъёмок"""
        return Photography.objects.filter(published=True).order_by('pk')




def albums_list(request, photography_slug=None):
    """Список товаров"""
    photography = None
    photographies = Photography.objects.filter(published=True)
    albums = Albums.objects.filter(published=True)
    if photography_slug:
        photography = get_object_or_404(Photography, slug=photography_slug)
        albums = albums.filter(photography=photography)
    return render(request, 'albums/albums_list.html', {'photography': photography,
                                                       'photographies': photographies,
                                                       'albums': albums})



def album_detail(request, id, slug):
    """Страница альбома"""
    album = get_object_or_404(Albums, id=id, slug=slug, published=True)
    albums_div = AlbumsDiv.objects.filter(album=album)
    return render(request, 'albums/albums_detail.html', {'album': album,
                                                        'albums_div': albums_div})


class PhotographyDetailView(PhotagraphyView, ListView):
    """Выводим список фотосъёмок"""
    model = Photography
    template_name = 'albums/albums_list.html'
    queryset = Photography.objects.filter(published=True).order_by('pk')


class AlbumDetailView(PhotagraphyView, DetailView):
    """Вывод страница с альбомом"""
    model = Albums
    slug_field = 'slug'
    queryset = Albums.objects.filter(published=True)


def album_share(request, albums_id):
    """Отправка электронного письма с рекоммендацие к просмотру альбома"""
    album = get_object_or_404(Albums, id=albums_id)
    sent = False
    if request.method == 'POST':
        form = EmailAlbumForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            album_url = request.build_absolute_uri(album.get_absolute_url())
            subject = f'{cd["name"]}  порекоммендовал(а) Вам этот альбом к просмотру "{album.name}"'
            message = f'Для просмотра альбома "{album.name}" перейдите по сыылке\n\n{album_url}. \nКомментарий: {cd["comments"]}.'
            send_mail(subject, message, 'arsavit@gmail.com', [cd['email_to']])
            sent = True
        else:
            pass
    else:
        form = EmailAlbumForm()
    return render(request, 'albums/album_share.html', {'album': album,
                                                       'form': form,
                                                       'sent': sent})
