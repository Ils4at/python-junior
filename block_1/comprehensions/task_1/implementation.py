def flatten_list(matrix: list) -> list:
    """
    Преобразует матрицу (список списков) в линейный список.

    Args:
         matrix: список, элементами которого являются списки

    Returns:
        линейный список
    """
    return [i for item in matrix for i in item]
