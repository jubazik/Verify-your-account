from django.shortcuts import render
from .models import Records, Сounterparties, Blog, Category


# def blog_all(request):
#     blog = Blog.objects.all()
#     context = {
#         'blog': blog,
#         'title': 'Этот мой блог'
#     }
#     return render(request, template_name='block/blog.html', context=context)
#

def records(request):  # Вывод всех оплат
    records = Records.objects.all()
    counterparties = Сounterparties.objects.all()
    context = {
        'records': records,
        'title': 'Список Оплат',
        'counterparties': counterparties

    }
    return render(request, template_name='block/records.html', context=context)


def get_record_id(request, record_id):  # Вывод оплат по id
    record = Records.objects.filter(name_id=record_id)
    counterparties = Сounterparties.objects.all()
    counterpart = Сounterparties.objects.get(pk=record_id)
    return render(request, 'block/record_id.html',
                  {'record': record, 'counterparties': counterparties, 'caunterpart': counterpart})


def counter(request):  # Вывод всех конрагентов
    counter = Сounterparties.objects.all()
    context = {
        'counter': counter,
    }
    return render(request, template_name='block/count.html', context=context)


def counterparties_category(request, coun_id):  # Вывод контрагенты по id
    counterparties = Сounterparties.objects.filter(ctegory_id=coun_id)
    category = Category.objects.all()
    counter = Сounterparties.objects.get(pk=coun_id)
    context = {
        'counterparties': counterparties,
        'title': 'Список контрагентов',
        'category': category,
        'counter': counter
    }
    return render(request, template_name='block/counterparties.html', context=context)
# Create your views here.

# def counter_id(request):
#     category = Category.objects.all()
#     context = {
#         'title' : 'Список Контрагентов',
#         'category' : category
#     }
#     return render(request, template_name='block/counterparties.html', context=context)
