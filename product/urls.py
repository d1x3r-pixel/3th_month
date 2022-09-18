from django.urls import path
from .views import(
    ProductListApiView,
    ProductCreateApiView,
    ProductDetailApiView,
    ProductUpdateApiView,
    ProductDestroyApiView,
    CategoryListApiView,
    CategoryCreateApiView,
CategoryDetailApiView,
PriceApiView,
LenProduct,
Revenue
)

urlpatterns = [
    path('prod_list/', ProductListApiView.as_view(), name='prod-list'),
    path('prod_create/', ProductCreateApiView.as_view(), name='prod-create'),
    path('cat_list/', CategoryListApiView.as_view(), name='cat-list'),
    path('cat_create/', CategoryCreateApiView.as_view(), name='cat-create'),
    path('price/', PriceApiView.as_view(), name='price'),
    path('len/', LenProduct.as_view(), name='len'),
    path('rev/', Revenue.as_view(), name='rev'),
]