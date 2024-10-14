from django.shortcuts import render,redirect
from .models import *
from .serializers import *
from django.utils import timezone
from rest_framework.generics import *
from django.views.generic import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views.generic.edit import UpdateView
from django.db.models import Q  # New
from django.contrib.auth.mixins import LoginRequiredMixin
from .filters import *
from itertools import groupby
from operator import attrgetter
from django.db.models import Count
@login_required(login_url='login')
def hokimpaneli(request):
    if request.user.username == 'admin':
        stats = {
            'hammasi': Sorov.objects.count(),
            'bajargan': Hokimiyat.objects.filter(bajarildi=True).count(),
            'bajarilmagan': Hokimiyat.objects.filter(bajarildi=False).count(),
            'muddati_otkan': Hokimiyat.objects.filter(muddat_holati=True).count(),
        }
        return render(request, 'hokim.html', stats)
    return redirect('login')

@login_required(login_url='login')
def hbarchasi(request):
    hammasis = Sorov.objects.all()
    return render(request, 'barcha.html', {'hammasi': hammasis})

@login_required(login_url='login')
def ramat(request):
    return render(request, 'rahmat.html')

@login_required(login_url='login')
def Tbir(request):
    return render_filtered_sorov(request, True, 'tbir.html')

@login_required(login_url='login')
def Tno(request):
    return render_filtered_sorov(request, False, 'tno.html')

def render_filtered_sorov(request, korish_value, template_name):
    af = Sorov.objects.filter(korish=korish_value)
    ac = af.count()
    return render(request, template_name, {'af': af, 'ac': ac})

@login_required(login_url='login')
def br(request):
    br1 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Суд масалалари').count()
    bar1 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Суд масалалари', bajarildi=True).count()

    br2 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Ички ишлар фаолияти').count()
    bar2 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Ички ишлар фаолияти', bajarildi=True).count()

    br3 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Прокуратура фаолияти').count()
    bar3 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Прокуратура фаолияти', bajarildi=True).count()

    br4 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Алимент масаласи').count()
    bar4 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Алимент масаласи', bajarildi=True).count()

    br5 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Суд ижроси').count()
    bar5 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Суд ижроси', bajarildi=True).count()

    br6 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Соғлиқни сақлаш').count()
    bar6 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Соғлиқни сақлаш', bajarildi=True).count()

    br7 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Пенсия ва нафақа').count()
    bar7 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Пенсия ва нафақа', bajarildi=True).count()

    br8 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Мактаб таълими').count()
    bar8 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Мактаб таълими', bajarildi=True).count()

    br9 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Ўй-жой, ер билан таъм').count()
    bar9 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Ўй-жой, ер билан таъм', bajarildi=True).count()

    br10 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Иш билан таъминлаш').count()
    bar10 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Иш билан таъминлаш', bajarildi=True).count()

    br11 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Афв этиш масаласи').count()
    bar11 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Афв этиш масаласи', bajarildi=True).count()

    br12 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Олий таълим масалалари').count()
    bar12 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Олий таълим масалалари', bajarildi=True).count()

    br13 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Кредит олиш').count()
    bar13 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Кредит олиш', bajarildi=True).count()

    br14 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Банк-молия масалалари').count()
    bar14 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Банк-молия масалалари', bajarildi=True).count()

    br15 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Газ, электр, сув, иссиқлик таъминоти').count()
    bar15 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Газ, электр, сув, иссиқлик таъминоти', bajarildi=True).count()

    br16 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Коммунал тўловларни ҳисоблаш').count()
    bar16 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='коммунал тўловларни ҳисоблаш', bajarildi=True).count()

    br17 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Йўл қурилиши').count()
    bar17 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Йўл қурилиши', bajarildi=True).count()

    br18 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Солиқ тўловлари').count()
    bar18 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Солиқ тўловлари', bajarildi=True).count()

    br19 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Транспорт масалалари').count()
    bar19 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Транспорт масалалари', bajarildi=True).count()

    br20 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Қурилиш соҳасидаги масалалар').count()
    bar20 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Қурилиш соҳасидаги масалалар', bajarildi=True).count()

    br21 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Тадбиркорлик ҳуқуқларини бузилиши').count()
    bar21 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Тадбиркорлик ҳуқуқларини бузилиши', bajarildi=True).count()

    br22 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Санʼат, маърифат ва маданият масалалари').count()
    bar22 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Санʼат, маърифат ва маданият масалалари', bajarildi=True).count()

    br23 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Дори-дармон нарх-наволари').count()
    bar23 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Дори-дармон нарх-наволари', bajarildi=True).count()

    br24 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Биринчи эҳтиёж моллари нарх-наволари').count()
    bar24 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Биринчи эҳтиёж моллари нарх-наволари', bajarildi=True).count()

    br25 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Давлат хизмати фаолияти').count()
    bar25 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Давлат хизмати фаолияти', bajarildi=True).count()

    br26 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Моддий ёрдам олиш').count()
    bar26 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Моддий ёрдам олиш', bajarildi=True).count()

    br27 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='бошқа масалалар').count()
    bar27 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Бошқа масалалар', bajarildi=True).count()

    con = {
        'br1':br1,
        'bar1':bar1,
        'br2':br2,
        'bar2':bar2,
        'br3':br3,
        'bar3':bar3,
        'br4':br4,
        'bar4':bar4,
        'br5':br5,
        'bar5':bar5,
        'br6':br6,
        'bar6':bar6,
        'br7':br7,
        'bar7':bar7,
        'br8':br8,
        'bar8':bar8,
        'br9':br9,
        'bar9':bar9,
        'br10':br10,
        'bar10':bar10,
        'br11':br11,
        'bar11':bar11,
        'br12':br12,
        'bar12':bar12,
        'br13':br13,
        'bar13':bar13,
        'br14':br14,
        'bar14':bar14,
        'br15':br15,
        'bar15':bar15,
        'br16':br16,
        'bar16':bar16,
        'br17':br17,
        'bar17':bar17,
        'br18':br18,
        'bar18':bar18,
        'br19':br19,
        'bar19':bar19,
        'br20':br20,
        'bar20':bar20,
        'br21':br21,
        'bar21':bar21,
        'br22':br22,
        'bar22':bar22,
        'br23':br23,
        'bar23':bar23,
        'br24':br24,
        'bar24':bar24,
        'br25':br25,
        'bar25':bar25,
        'br26':br26,
        'bar26':bar26,
        'br27':br27,
        'bar27':bar27,
    }
    return render(request,'br.html',con)
def bjr(request):
    br1 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Суд масалалари').count()
    bar1 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Суд масалалари', bajarildi=False).count()

    br2 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Ички ишлар фаолияти').count()
    bar2 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Ички ишлар фаолияти', bajarildi=False).count()

    br3 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Прокуратура фаолияти').count()
    bar3 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Прокуратура фаолияти', bajarildi=False).count()

    br4 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Алимент масаласи').count()
    bar4 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Алимент масаласи', bajarildi=False).count()

    br5 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Суд ижроси').count()
    bar5 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Суд ижроси', bajarildi=False).count()

    br6 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Соғлиқни сақлаш').count()
    bar6 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Соғлиқни сақлаш', bajarildi=False).count()

    br7 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Пенсия ва нафақа').count()
    bar7 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Пенсия ва нафақа', bajarildi=False).count()

    br8 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Мактаб таълими').count()
    bar8 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Мактаб таълими', bajarildi=False).count()

    br9 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Ўй-жой, ер билан таъм').count()
    bar9 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Ўй-жой, ер билан таъм', bajarildi=False).count()

    br10 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Иш билан таъминлаш').count()
    bar10 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Иш билан таъминлаш', bajarildi=False).count()

    br11 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Афв этиш масаласи').count()
    bar11 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Афв этиш масаласи', bajarildi=False).count()

    br12 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Олий таълим масалалари').count()
    bar12 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Олий таълим масалалари', bajarildi=False).count()

    br13 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Кредит олиш').count()
    bar13 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Кредит олиш', bajarildi=False).count()

    br14 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Банк-молия масалалари').count()
    bar14 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Банк-молия масалалари', bajarildi=False).count()

    br15 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Газ, электр, сув, иссиқлик таъминоти').count()
    bar15 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Газ, электр, сув, иссиқлик таъминоти', bajarildi=False).count()

    br16 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Коммунал тўловларни ҳисоблаш').count()
    bar16 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Коммунал тўловларни ҳисоблаш', bajarildi=False).count()

    br17 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Йўл қурилиши').count()
    bar17 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Йўл қурилиши', bajarildi=False).count()

    br18 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Солиқ тўловлари').count()
    bar18 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Солиқ тўловлари', bajarildi=False).count()

    br19 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Транспорт масалалари').count()
    bar19 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Транспорт масалалари', bajarildi=False).count()

    br20 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Қурилиш соҳасидаги масалалар').count()
    bar20 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Қурилиш соҳасидаги масалалар', bajarildi=False).count()

    br21 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Тадбиркорлик ҳуқуқларини бузилиши').count()
    bar21 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Тадбиркорлик ҳуқуқларини бузилиши', bajarildi=False).count()

    br22 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Санʼат, маърифат ва маданият масалалари').count()
    bar22 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Санʼат, маърифат ва маданият масалалари', bajarildi=False).count()

    br23 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Дори-дармон нарх-наволари').count()
    bar23 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Дори-дармон нарх-наволари', bajarildi=False).count()

    br24 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Биринчи эҳтиёж моллари нарх-наволари').count()
    bar24 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Биринчи эҳтиёж моллари нарх-наволари', bajarildi=False).count()

    br25 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Давлат хизмати фаолияти').count()
    bar25 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Давлат хизмати фаолияти', bajarildi=False).count()

    br26 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Моддий ёрдам олиш').count()
    bar26 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Моддий ёрдам олиш', bajarildi=False).count()

    br27 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Бошқа масалалар').count()
    bar27 = Hokimiyat.objects.filter(tel_name__ariza_mazmuni='Бошқа масалалар', bajarildi=False).count()



    con = {
        'br1':br1,
        'bar1':bar1,
        'br2':br2,
        'bar2':bar2,
        'br3':br3,
        'bar3':bar3,
        'br4':br4,
        'bar4':bar4,
        'br5':br5,
        'bar5':bar5,
        'bar6':bar6,
        'br6':br6,
        'br7':br7,
        'bar7':bar7,
        'br8':br8,
        'bar8':bar8,
        'br9':br9,
        'bar9':bar9,
        'br10':br10,
        'bar10':bar10,
        'br11':br11,
        'bar11':bar11,
        'br12':br12,
        'bar12':bar12,
        'br13':br13,
        'bar13':bar13,
        'br14':br14,
        'bar14':bar14,
        'br15':br15,
        'bar15':bar15,
        'br16':br16,
        'bar16':bar16,
        'br17':br17,
        'bar17':bar17,
        'br18':br18,
        'bar18':bar18,
        'br19':br19,
        'bar19':bar19,
        'br20':br20,
        'bar20':bar20,
        'br21':br21,
        'bar21':bar21,
        'br22':br22,
        'bar22':bar22,
        'br23':br23,
        'bar23':bar23,
        'br24':br24,
        'bar24':bar24,
        'br25':br25,
        'bar25':bar25,
        'br26':br26,
        'bar26':bar26,
        'br27':br27,
        'bar27':bar27,
    }
    return render(request,'bjr.html',con)


@login_required(login_url='login')
def at(request):
    ir1 = Sorov.objects.filter(ariza_mazmuni='Суд масалалари').count()
    ir2 = Sorov.objects.filter(ariza_mazmuni='Ички ишлар фаолияти').count()
    ir3 = Sorov.objects.filter(ariza_mazmuni='Прокуратура фаолияти').count()
    ir4 = Sorov.objects.filter(ariza_mazmuni='Алимент масаласи').count()
    ir5 = Sorov.objects.filter(ariza_mazmuni='Суд ижроси').count()
    ir6 = Sorov.objects.filter(ariza_mazmuni='Соғлиқни сақлаш').count()
    ir7 = Sorov.objects.filter(ariza_mazmuni='Пенсия ва нафақа').count()
    ir8 = Sorov.objects.filter(ariza_mazmuni='Мактаб таълими').count()
    ir9 = Sorov.objects.filter(ariza_mazmuni='Ўй-жой, ер билан таъм').count()
    ir10 = Sorov.objects.filter(ariza_mazmuni='Иш билан таъминлаш').count()
    ir11 = Sorov.objects.filter(ariza_mazmuni='Афв этиш масаласи').count()
    ir12 = Sorov.objects.filter(ariza_mazmuni='Олий таълим масалалари').count()
    ir13 = Sorov.objects.filter(ariza_mazmuni='Кредит олиш').count()
    ir14 = Sorov.objects.filter(ariza_mazmuni='Банк-молия масалалари').count()
    ir15 = Sorov.objects.filter(ariza_mazmuni='Газ, электр, сув, иссиқлик таъминоти').count()
    ir16 = Sorov.objects.filter(ariza_mazmuni='Коммунал тўловларни ҳисоблаш').count()
    ir17 = Sorov.objects.filter(ariza_mazmuni='Йўл қурилиши').count()
    ir18 = Sorov.objects.filter(ariza_mazmuni='Солиқ тўловлари').count()
    ir19 = Sorov.objects.filter(ariza_mazmuni='Транспорт масалалари').count()
    ir20 = Sorov.objects.filter(ariza_mazmuni='Қурилиш соҳасидаги масалалар').count()
    ir21 = Sorov.objects.filter(ariza_mazmuni='Тадбиркорлик ҳуқуқларини бузилиши').count()
    ir22 = Sorov.objects.filter(ariza_mazmuni='Санʼат, маърифат ва маданият масалалари').count()
    ir23 = Sorov.objects.filter(ariza_mazmuni='Дори-дармон нарх-наволари').count()
    ir24 = Sorov.objects.filter(ariza_mazmuni='Биринчи эҳтиёж моллари нарх-наволари').count()
    ir25 = Sorov.objects.filter(ariza_mazmuni='Давлат хизмати фаолияти').count()
    ir26 = Sorov.objects.filter(ariza_mazmuni='Моддий ёрдам олиш').count()
    ir27 = Sorov.objects.filter(ariza_mazmuni='Бошқа масалалар').count()

    con = {
    'ir1':ir1,
    'ir2':ir2,
    'ir3':ir3,
    'ir4':ir4,
    'ir5':ir5,
    'ir6':ir6,
    'ir7':ir7,
    'ir8':ir8,
    'ir9':ir9,
    'ir10':ir10,
    'ir11':ir11,
    'ir12':ir12,
    'ir13':ir13,
    'ir14':ir14,
    'ir15':ir15,
    'ir16':ir16,
    'ir17':ir17,
    'ir18':ir18,
    'ir19':ir19,
    'ir20':ir20,
    'ir21':ir21,
    'ir22':ir22,
    'ir23':ir23,
    'ir24':ir24,
    'ir25':ir25,
    'ir26':ir26,
    'ir27':ir27,
    }
    return render(request,'t.html',con)
def user_ariza(request,name):
    ariza = Sorov.objects.filter(fish=name,korish=False)
    con = {
        'ariza':ariza
    }
    return render(request,'user_ariza.html',con)


class CreateBlog(CreateView):
    model = Hokimiyat
    template_name = 'blog_new.html'
    fields = ('__all__')

@login_required(login_url='login')
def hokimiyatPanel(request):
    if request.user.is_authenticated:
        if request.user.type == 'Tashkilot':
            tashkilotlar = Tashkilotlar.objects.all()  # Barcha tashkilotlarni olish
            tashkilot_id = request.GET.get('tashkilot', '')  # Tanlangan tashkilot ID'sini olish

            if tashkilot_id:
                hok = Hokimiyat.objects.filter(tashkilot__id=request.user.tashkilot, bajarildi=False)  # Tanlangan tashkilotni filtr qilish
            else:
                hok = Hokimiyat.objects.filter(bajarildi=False)  # Agar tanlanmasa, barcha tashkilotlarni ko'rsatish

            ariza = Sorov.objects.all()
            return render(request, 'hp2.html', {
                'hok': hok,
                'ariza': ariza,
                'tashkilotlar': tashkilotlar,
                'tashkilot_id': tashkilot_id,  # Tanlangan tashkilot ID'sini shablonda foydalanish uchun yuborish
            })
        else:
            hammasi = Sorov.objects.all().count()
            bajargan = Hokimiyat.objects.filter(bajarildi=True).count()
            bajarilmagan = Hokimiyat.objects.filter(bajarildi=False).count()
            muddati_otkan = Hokimiyat.objects.filter(muddat_holati=True).count()
            ariza = Sorov.objects.filter(korish=False)
            ac = Sorov.objects.filter(korish=False).count()
            af = Sorov.objects.filter(korish=True).count()

            # Grouping arizalar by 'fish' and counting the number of submissions
            grouped_arizalar = []
            ariza = ariza.order_by('fish')  # Ensure the queryset is ordered by 'fish' for groupby to work correctly
            for key, group in groupby(ariza, key=attrgetter('fish')):
                group_list = list(group)
                first_element = group_list[0]
                submission_count = len(group_list)  # Count the number of submissions for this 'fish'
                grouped_arizalar.append({
                    'ariza': first_element,
                    'submission_count': submission_count
                })

            return render(request, 'hp.html', {
                'hammasi': hammasi,
                'bajargan': bajargan,
                'bajarilmagan': bajarilmagan,
                'muddati_otkan': muddati_otkan,
                'grouped_arizalar': grouped_arizalar,
                'ac': ac,
                'af': af,
            })

    else:
        return redirect('login')
@login_required(login_url='login')
def barcha(request,at):
    ariza = Sorov.objects.filter(ariza_mazmuni=at)
    ac = ariza.count()
    return render(request,'barcha.html',{'ariza':ariza,'ac':ac})
@login_required(login_url='login')
def bajarilgan(request,at):
    ft = HokimiyatFilter()
    ariza = HokimiyatFilter(request.GET,Hokimiyat.objects.filter(tel_name__ariza_mazmuni=at,bajarildi=True))
    ac = HokimiyatFilter(request.GET,Hokimiyat.objects.filter(tel_name__ariza_mazmuni=at,bajarildi=True))
    return render(request,'bajarilgan.html',{'ariza':ariza.qs,'ft':ft,'ac':ac.qs.count()})
@login_required(login_url='login')
def muddat(request):
    arizal = Hokimiyat.objects.filter(muddat_holati=False)
    ariza = Hokimiyat.objects.filter(muddat_holati=True)
    return render(request,'md.html',{'ariza':ariza,'arizal':arizal,'ac':ariza.count()})
@login_required(login_url='login')
def bj(request,at):
    ft = HokimiyatFilter()
    ariza = HokimiyatFilter(request.GET,Hokimiyat.objects.filter(tel_name__ariza_mazmuni=at,bajarildi=False))
    return render(request,'bj.html',{'ariza':ariza.qs,'ft':ft,'ac':ariza.qs.count()})
@login_required(login_url='login')
def tash(request):
    if request.user.username == 'tash1':
        ariza = Hokimiyat.objects.filter(tashkilot='t1')
    elif request.user.username == 'tash2':
        ariza = Hokimiyat.objects.filter(tashkilot='t1')
@login_required(login_url='login')
def delete(request,id):
    Sorov.objects.filter(id=id).update(korish=True)
    return redirect('hp')
@login_required(login_url='login')
def mudot(request,id):
    Hokimiyat.objects.filter(id=id).update(muddat_holati=True)
    return redirect('hp')

@login_required(login_url='login')
def updatebajar(request,pk):
    Hokimiyat.objects.filter(id=pk).update(bajarildi=True)
    return redirect('hp')

@login_required(login_url='login')
def sorovid(request, id):
    sorovid = Sorov.objects.get(id=id)
    form = DweetForm()
    hokimiyat_list = []

    if sorovid.korish == True:
        # Hokimiyat obyektlarini olish
        hokimiyat_list = Hokimiyat.objects.filter(tel_name=sorovid)

    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.tel_name = sorovid
            dweet.save()
            sorovid.korish = True
            sorovid.save()

    return render(request, 'sorovid.html', {
        'ariza': sorovid,
        'form': form,
        'hokimiyat_list': hokimiyat_list
    })


def for_all_pages(request):
    # Ariza mazmuni ro'yxati
    ariza_mazmuni_list = [
       'Суд масалалари', 'Ички ишлар фаолияти', 'Прокуратура фаолияти',
        'Алимент масаласи', 'Суд ижроси', 'Соғлиқни сақлаш',
        'Пенсия ва нафақа', 'Мактаб таълими', 'Ўй-жой, ер билан таъм',
        'Иш билан таъминлаш', 'Афв этиш масаласи', 'Олий таълим масалалари',
        'Кредит олиш', 'Банк-молия масалалари',
        'Газ, электр, сув, иссиқлик таъминоти',
        'Коммунал тўловларни ҳисоблаш', 'Йўл қурилиши',
        'Солиқ тўловлари', 'Транспорт масалалари',
        'Қурилиш соҳасидаги масалалар',
        'Тадбиркорлик ҳуқуқларини бузилиши',
        'Санʼат, маърифат ва маданият масалалари',
        'Дори-дармон нарх-наволари',
        'Биринчи эҳтиёж моллари нарх-наволари',
        'Давлат хизмати фаолияти',
        'Моддий ёрдам олиш', 'Бошқа масалалар'
    ]

    # Hisoblangan natijalarni saqlash uchun lug'at
    con = {}

    # Har bir ariza mazmuni uchun hisoblash
    for index, ariza_mazmuni in enumerate(ariza_mazmuni_list, start=1):
        count = Sorov.objects.filter(ariza_mazmuni=ariza_mazmuni, korish=False).count()
        con[f'i{index}'] = count  # i1, i2, i3... tarzida kalitlar yaratish

    # Natijalarni qaytarish
    return con



class Change(LoginRequiredMixin,UpdateView):
    model = Hokimiyat
    template_name = 'bajar.html'
    fields = ['bajarildi']
# @login_required(login_url='login')
# def filter_ariza_tur1(request):
#     if request.method == "POST":
#         form = DweetForm1(request.POST)
#         if form.is_valid():
#             dweet = form.save(commit=False)
#             dweet.user = request.user
#             dweet.save()

#     form = DweetForm1()
#     hokimiyat = Hokimiyat.objects.all()
#     ariza = Sorov.objects.filter(ariza_mazmuni='суд  масалалари',korish=False)
#     return render(request,'hp_az/hp_az1.html',{'ariza':ariza,"form": form,'hokimiyat':hokimiyat})
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def filter_ariza_tur1(request):
    if request.method == "POST":
        form = DweetForm1(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)

            # Tanlangan arizalarni olish
            selected_arizalar = request.POST.getlist('selected_arizalar')

            if not selected_arizalar:
                return JsonResponse({'success': False, 'message': 'Tanlangan arizalar yo\'q.'})

            arizalar = Sorov.objects.filter(id__in=selected_arizalar)
            if not arizalar.exists():
                return JsonResponse({'success': False, 'message': 'Tanlangan arizalar topilmadi.'})

            # Orinbosar va Tashkilot ob'ektlarini olish
            orinbosari = get_object_or_404(Orinbosar, id=dweet.orinbosar.id)
            tashkiloti = get_object_or_404(Tashkilotlar, id=dweet.tashkilot.id)

            response_data = []

            for ariza in arizalar:
                # Hokimiyat modeliga saqlaymiz
                hokimiyat_instance = Hokimiyat.objects.create(
                    tel_name=ariza,
                    orinbosar=orinbosari,
                    tashkilot=tashkiloti
                )

                # Ariza `korish` maydonini True ga yangilaymiz
                ariza.korish = True
                ariza.save()

                # Qaytish uchun ma'lumotlarni yig'ish
                response_data.append({
                    'tel_name': hokimiyat_instance.tel_name.id,
                    'orinbosar': hokimiyat_instance.orinbosar.id,
                    'tashkilot': hokimiyat_instance.tashkilot.id
                })



    else:
        form = DweetForm1()

    arizaturi = request.GET.get('arizatur', None)
    # Faqat 'Суд масалалари' arizalarini ko'rsatamiz
    tashkilotlar = Tashkilotlar.objects.all()
    orinbosarlar = Orinbosar.objects.all()
    arizas = Sorov.objects.filter(ariza_mazmuni=arizaturi, korish=False)

    return render(request, 'hp_az/hp_az1.html', {
        'ariza': arizas,
        'form': form,
        'tashkilotlar': tashkilotlar,
        'orinbosarlar': orinbosarlar,
    })


@login_required(login_url='login')
def fuwr(request):
    return render(request,'uls.html')
@login_required(login_url='login')
def searching(request):
    query = request.GET.get("q")
    object_list = Sorov.objects.filter(
            Q(fish__icontains=query)
        )
    return render(request,'searching.html',{'ariza':object_list})