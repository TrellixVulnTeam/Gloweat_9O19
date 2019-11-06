from rest_framework import viewsets
from apps.productos.models import productos
from apps.productos.serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    model = productos
    queryset = productos.objects.all()
    serializer_class = ProductoSerializer