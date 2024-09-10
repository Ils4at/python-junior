def convert_temperature(value, to_scale):
    """Конвертирует температуру в нужную системы счисления

    Args:
        value: значение температуры
        to_scale: система счисления, в которую нужно конвертировать значение

    Returns: значение как результат конвертации
    """
    if to_scale == 'F':
        value = (value * 1.8000) + 32.00
        return value
    elif to_scale == 'C':
        value = (value - 32)/1.800
        return value
    else:
        return value
#raise NotImplementedError
