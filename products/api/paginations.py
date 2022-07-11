from rest_framework.pagination import LimitOffsetPagination

class ProductListPagination(LimitOffsetPagination):
    default_limit=4
    max_limit=7