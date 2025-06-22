from django.shortcuts import render
from .models import SquadPowerEntry

def squad_power(request):
    if request.method == 'POST':
        in_game_name = request.POST.get('in_game_name')
        hq_level = request.POST.get('hq_level')
        squad_power_value = request.POST.get('squad_power')

        entry = SquadPowerEntry(
            in_game_name=in_game_name,
            hq_level=hq_level,
            squad_power=squad_power_value
        )
        entry.save()

        return render(request, 'thanks.html')

    return render(request, 'home.html')
