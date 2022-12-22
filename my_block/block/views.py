from django.shortcuts import render
from .models import Records, Сounterparties


def records(request):
    records = Records.objects.all()
    context = {
        'records':records,
        'title': 'Список Оплат'
    }
    return render(request, template_name='block/records.html', context=context)


def counterparties_block(request):
    counterparties = Сounterparties.objects.all()
    context = {
        'counterparties': counterparties,
        'title': 'Список контрагентов'
    }
    return render(request, template_name='block/counterparties.html', context=context)
# Create your views here.
