from django.shortcuts import render

from .models import *


def top(request):
    return render(request, 'top.html', {})

def about(request):
    return render(request, 'about.html', {})

def premium(request):
    return render(request, 'premium.html', {})

def contact(request):
    return render(request, 'contact.html', {})


def pref(request):
    hokkaido_cities = Hokkaido.objects
    aomori_cities = Aomori.objects
    iwate_cities = Iwate.objects
    akita_cities = Akita.objects
    miyagi_cities = Miyagi.objects
    yamagata_cities = Yamagata.objects
    fukushima_cities = Fukushima.objects
    niigata_cities = Niigata.objects
    tochigi_cities = Tochigi.objects
    ibaraki_cities = Ibaraki.objects
    saitama_cities = Saitama.objects
    chiba_cities = Chiba.objects
    tokyo_cities = Tokyo.objects
    kanagawa_cities = Kanagawa.objects
    shizuoka_cities = Shizuoka.objects
    yamanashi_cities = Yamanashi.objects
    gunma_cities = Gunma.objects
    nagano_cities = Nagano.objects
    gifu_cities = Gifu.objects
    ishikawa_cities = Ishikawa.objects
    aichi_cities = Aichi.objects
    toyama_cities = Toyama.objects
    fukui_cities = Fukui.objects
    mie_cities = Mie.objects
    shiga_cities = Shiga.objects
    kyoto_cities = Kyoto.objects
    osaka_cities = Osaka.objects
    nara_cities = Nara.objects
    wakayama_cities = Wakayama.objects
    hyogo_cities = Hyogo.objects
    tottori_cities = Tottori.objects
    okayama_cities = Okayama.objects
    hiroshima_cities = Hiroshima.objects
    shimane_cities = Shimane.objects
    yamaguchi_cities = Yamaguchi.objects
    tokushima_cities = Tokushima.objects
    kochi_cities = Kochi.objects
    ehime_cities = Ehime.objects
    kagawa_cities = Kagawa.objects
    saga_cities = Saga.objects
    nagasaki_cities = Nagasaki.objects
    fukuoka_cities = Fukuoka.objects
    oita_cities = Oita.objects
    kumamoto_cities = Kumamoto.objects
    miyazaki_cities = Miyazaki.objects
    kagoshima_cities = Kagoshima.objects
    okinawa_cities = Okinawa.objects
    return render(request, 'home.html', {'miyagi_cities':miyagi_cities, 'chiba_cities':chiba_cities, 'kagoshima_cities':kagoshima_cities, 'hokkaido_cities':hokkaido_cities,'aomori_cities':aomori_cities, 'iwate_cities':iwate_cities, 'akita_cities':akita_cities,'yamagata_cities':yamagata_cities,'fukushima_cities':fukushima_cities,'niigata_cities':niigata_cities,'tochigi_cities':tochigi_cities,'ibaraki_cities':ibaraki_cities,'saitama_cities':saitama_cities,'tokyo_cities':tokyo_cities,'kanagawa_cities':kanagawa_cities,'shizuoka_cities':shizuoka_cities,'yamanashi_cities':yamanashi_cities,'gunma_cities':gunma_cities,'nagano_cities':nagano_cities,'gifu_cities':gifu_cities,'ishikawa_cities':ishikawa_cities,'aichi_cities':aichi_cities,'toyama_cities':toyama_cities,'fukui_cities':fukui_cities,'mie_cities':mie_cities,'shiga_cities':shiga_cities,'kyoto_cities':kyoto_cities,'osaka_cities':osaka_cities,'nara_cities':nara_cities,'wakayama_cities':wakayama_cities,'hyogo_cities':hyogo_cities,'tottori_cities':tottori_cities,'okayama_cities':okayama_cities,'hiroshima_cities':hiroshima_cities,'shimane_cities':shimane_cities,'yamaguchi_cities':yamaguchi_cities,'tokushima_cities':tokushima_cities,'kochi_cities':kochi_cities,'ehime_cities':ehime_cities,'kagawa_cities':kagawa_cities,'saga_cities':saga_cities,'nagasaki_cities':nagasaki_cities,'fukuoka_cities':fukuoka_cities,'oita_cities':oita_cities,'kumamoto_cities':kumamoto_cities,'miyazaki_cities':miyazaki_cities,'okinawa_cities':okinawa_cities}) 

