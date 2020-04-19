from django.urls import path
from wallet.views import EntryListView, EntryCreateView, EntryUpdateView, EntryDeleteView, sample
# from . import views

urlpatterns = [
    path("", EntryListView.as_view(), name="wallet-home"),
    path("add", EntryCreateView.as_view(), name="wallet-addentry"),
    path("edit/<int:pk>", EntryUpdateView.as_view(), name="wallet-editentry"),
    path("delete/<int:pk>", EntryDeleteView.as_view(), name="wallet-deleteentry"),
    # path("", views.home, name="wallet-home"),
    # path("add", views.add, name="wallet-addentry"),
    # path("edit", views.edit, name="wallet-editentry"),
    path("sample", sample, name="wallet-sample")
]
