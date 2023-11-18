from django.shortcuts import get_object_or_404, render

from .models import RelicWeapon


def relic_weapon(request, relic_name):
    relic_weapon = get_object_or_404(
        RelicWeapon,
        weapon_name=relic_name
    )
    context = {'relic_weapon': relic_weapon}
    return render(request, 'relic_weapon.html', context)


def index(request):
    relic_weapons = RelicWeapon.objects.all()
    context = {'relic_weapons': relic_weapons}
    return render(request, 'index.html', context)
