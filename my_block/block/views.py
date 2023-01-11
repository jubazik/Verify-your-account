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
        'title': 'Список оплат',
        'counterparties': counterparties

    }
    return render(request, template_name='block/records.html', context=context)


def get_record_id(request, record_id):  # Вывод оплат по id
    record = Records.objects.filter(name_id=record_id)
    counterparties = Сounterparties.objects.all()
    counterpart = Сounterparties.objects.get(pk=record_id)
    return render(request, 'block/record_id.html',
                  {'record': record, 'counterparties': counterparties, 'caunterpart': counterpart, 'title': 'Список оплат'})



def counter(request):  # Вывод всех конрагентов
    counter = Сounterparties.objects.all()
    category = Category.objects.all()
    context = {
        'category': category,
        'counter': counter,
        'title': 'Список Контрагентов'
    }
    return render(request, template_name='block/count.html', context=context)


def counterparties_category(request, category_id):  # Вывод контрагенты по id
    counterparties = Сounterparties.objects.filter(category_id=category_id)
    category = Category.objects.all()
    counter = Сounterparties.objects.get(pk=category_id)

    return render(request, 'block/counterparties.html',
                  {'counterparties': counterparties, 'category': category, 'counter': counter,
                   'title': 'Список Контрагентов'})
# Create your views here.

