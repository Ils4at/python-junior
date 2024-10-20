from block_2.queryset_methods.models import OrderItem, ProductCost
from django.db.models import Sum
from django.db.models import OuterRef, Subquery, ExpressionWrapper, DecimalField, F


def get_top_order_by_sum_in_period(begin, end):
    """Возвращает заказ, который имеют наибольшую сумму за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает номер заказа и его сумму
    """
    res1 = (ProductCost.objects
            .filter(begin__gte=begin, end__lte=end, product=OuterRef("product"))
            .values('product', 'value')
            )
    response = (OrderItem.objects
                .filter(order__date_formation__gte=begin, order__date_formation__lte=end)
                .select_related('order')
                .values('order__number')
                .annotate(sum=Sum(ExpressionWrapper(F('count') *
                                                    Subquery(res1.values('value')),
                                                    output_field=DecimalField()
                                                    )
                                  )
                          )
                .order_by('-order__number')[:1]
                )
    if len(response) > 0:
        return response[0]['order__number'], response[0]['sum']
    else:
        return None