from block_2.queryset_methods.models import Customer, Order


def get_order_count_by_customer(name):
    """Возвращает количества заказов по имени покупателя

    Args:
        name: имя покупателя

    Returns: число заказов (не может быть отрицательным, но может быть нулевым)
    """
    response = Order.objects.all().filter(customer__name=name).count()
    return response

