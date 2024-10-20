from block_2.queryset_methods.models import Order
from django.db.models import Count


def get_top_customer_in_period(begin, end):
    """Возвращает покупателя, который сделал наибольшее количество заказов за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает имя покупателя и количество его заказов за указанный период
    """
    first_q = (Order.objects.filter(date_formation__gte=begin, date_formation__lte=end)
               .values('customer__name', 'customer__id')
               .order_by('date_formation', 'customer__name'))[:1]
    if len(first_q) > 0:
        name = first_q[0]['customer__name']
        response = (Order.objects.filter(date_formation__gte=begin, date_formation__lte=end, customer__name=name)
                    .values('customer__name')
                    .annotate(dcount=Count('customer__name')))
        return response[0]['customer__name'], response[0]['dcount']
    else:
        return None
