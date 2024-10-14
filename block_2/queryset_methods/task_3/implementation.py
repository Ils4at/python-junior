from block_2.queryset_methods.models import OrderItem
from django.db.models import Count, Max, Min


def get_top_order_by_sum_in_period(begin, end):
    """Возвращает заказ, который имеют наибольшую сумму за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает номер заказа и его сумму
    """
    res = OrderItem.objects.all().filter(product__date_formation__lte=begin, product__date_formation__gte=begin).Max('count').order_by('-order__number')[0]
    return res[0].order__number, res[0].count
