from block_2.queryset_methods.models import OrderItem
from django.db.models import Sum, IntegerField


def get_top_product_by_total_count_in_period(begin, end):
    """Возвращает товар, купленный в наибольшем объеме за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает наименование товара и объем
    """
    response = (OrderItem.objects
                .filter(order__date_formation__gte=begin, order__date_formation__lte=end)
                .select_related('product')
                .values_list('product__name')
                .annotate(sum=Sum('count',
                                  output_field=IntegerField()))
                .order_by('-sum')[:1])
    if len(response) > 0:
        return response[::-1]
    else:
        return []