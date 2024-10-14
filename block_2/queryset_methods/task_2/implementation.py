from block_2.queryset_methods.models import Customer, Order
from django.db.models import Count, Max, Min


def get_top_customer_in_period(begin, end):
    """Возвращает покупателя, который сделал наибольшее количество заказов за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает имя покупателя и количество его заказов за указанный период
    """
    res = Order.objects.all().filter(date_formation__lte=begin, date_formation__gte=end).annotate(Max(Count('customer')))
    res = res.filter(Min('date_formation')).order_by('customer__name')[0]

    if res[0].customer__count >= 0:
        return res[0].customer__name, res[0].customer__count
    else:
        raise None