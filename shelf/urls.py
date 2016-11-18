from django.conf.urls import url
from .views import AuthorListView, AuthorDetailView, BookListView, PublisherListView

urlpatterns = [
        url(r'authors/$', AuthorListView.as_view(), name='author-list'),
        url(r'authors/(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='author-detail'),
        url(r'books/$', BookListView.as_view(), name='book-list'),
        url(r'publisher/$', PublisherListView.as_view(), name='publisher-list'),
        ]

