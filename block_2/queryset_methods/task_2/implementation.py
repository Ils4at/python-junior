from block_2.queryset_methods.models import Order
from django.db.models import Count


def get_top_customer_in_period(begin, end):
    """Возвращает покупателя, который сделал наибольшее количество заказов за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает имя покупателя и количество его заказов за указанный период
    """
    s = Order.objects.filter(date_formation__gte=begin, date_formation__lte=end).values('customer__name').order_by('-date_formation').order_by('customer__name').annotate(dcount=Count('customer__name'))[:1]
    print(len(s), 'dsddsds')
    if len(s) > 0:
        return s[0]['customer__name'], s[0]['dcount']
    else:
        return None
