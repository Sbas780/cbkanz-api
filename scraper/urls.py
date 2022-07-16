from django.urls import path
from .views import VendorsView, ProductsView, ApiOverview, ProductsByTypeView, \
    ProductsByPkView, ProductByVendorPkView


urlpatterns = [
    path('', ApiOverview.as_view(), name=""),
    path('vendors/', VendorsView.as_view(), name="vendors-view"),
    path('products/', ProductsView.as_view(), name='products-view'),
    path('collection/type/<str:type>', ProductsByTypeView.as_view()),
    path('collection/id/<int:pk>', ProductsByPkView.as_view()),
    path('collection/vendor/<int:pk>', ProductByVendorPkView.as_view()),


]