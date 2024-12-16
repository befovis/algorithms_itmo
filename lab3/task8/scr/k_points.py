def get_k_closest_points(points, k):
    """
    Сортирует все точки по расстоянию от начала координат и возвращает k ближайших.
    """
    points.sort(key=lambda point: point[0] ** 2 + point[1] ** 2)
    closest_points = points[:k]
    closest_points.sort()

    return closest_points
