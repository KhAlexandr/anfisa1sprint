from django.shortcuts import get_object_or_404, render

from ice_cream.models import IceCream

ice_cream_catalog = [
    {
        'id': 0,
        'title': 'Классический пломбир',
        'description': 'Настоящее мороженое, для истинных ценителей вкуса. '
                       'Если на столе появляется пломбир — это не надолго.',
    },
    {
        'id': 1,
        'title': 'Мороженое с кузнечиками',
        'description': 'В колумбийском стиле: мороженое '
                       'с добавлением настоящих карамелизованных кузнечиков.',
    },
    {
        'id': 2,
        'title': 'Мороженое со вкусом сыра чеддер',
        'description': 'Вкус настоящего сыра в вафельном стаканчике.',
    },
]


def ice_cream_detail(request, pk):
    template = 'ice_cream/detail.html'
    ice_cream = get_object_or_404(
        IceCream.objects.filter(is_published=True, category__is_published=True),
        pk=pk
    )
    context = {
        'ice_cream': ice_cream,
    }
    return render(request, template, context)


def ice_cream_list(request):
    template = 'ice_cream/list.html'
    ice_cream_list = IceCream.objects.select_related('category').filter(
        is_published=True,
        category__is_published=True
    ).order_by('category')
    context = {'ice_cream_list': ice_cream_list}
    return render(request, template, context)
