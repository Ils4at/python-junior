from block_2.queryset_methods.models import OrderItem, ProductCost
from django.db.models import Avg, Sum, OuterRef, Subquery, ExpressionWrapper, DecimalField, F


def get_average_cost_without_product(product, begin, end):
    """Возвращает среднюю стоимость заказов без указанного товара за определенный промежуток времени

    Args:
        product: наименование товара
        begin: начало периода
        end: окончание периода

    Returns: возвращает числовое значение средней стоимости
    """
    res1 = (ProductCost.objects
            .filter(begin__gte=begin, end__lte=end, product=OuterRef("product"))
            .values('product', 'value')
            )
    response = (OrderItem.objects
                .filter(order__date_formation__gte=begin, order__date_formation__lte=end)
                .exclude(product__name=product)
                .select_related('product')
                .select_related('order')
                .annotate(sum1=Sum(ExpressionWrapper(F('count') *
                                                     Subquery(res1.values('value')),
                                                     output_field=DecimalField()
                                                     )
                                   )
                          )
                .aggregate(Avg('sum1')))
    if response['sum1__avg'] is None:
        return 0.00
    else:
        return response['sum1__avg']