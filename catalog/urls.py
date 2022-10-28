from django.urls import path

from catalog.views import index, \
    BookListView, \
    BookDetailView, \
    AuthorListView, \
    AuthorDetailView, \
    AuthorCreateView, \
    LiteraryFormatListView, \
    LiteraryFormatCreateView, \
    LiteraryFormatUpdateView, \
    LiteraryFormatDeleteView, \
    BookUpdateView, \
    BookCreateView

urlpatterns = [
    path("", index, name="index"),
    # path("test-sessions/", test_session_view, name="test-session"),
    path("literary-formats/",
         LiteraryFormatListView.as_view(),
         name="literary-format-list"),
    path("literary-formats/create/",
         LiteraryFormatCreateView.as_view(),
         name="literary-format-create"),
    path("literary-formats/<int:pk>/update/",
         LiteraryFormatUpdateView.as_view(),
         name="literary-format-update"),
    path("literary-formats/<int:pk>/delete/",
         LiteraryFormatDeleteView.as_view(),
         name="literary-format-delete"),
    path("books/", BookListView.as_view(), name="book-list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("books/create/",
         BookCreateView.as_view(),
         name="book-create"),
    path("books/<int:pk>/update/",
         BookUpdateView.as_view(),
         name="book-update"),
    path("authors/", AuthorListView.as_view(), name="author-list"),
    path("authors/<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),
    path("authors/create/", AuthorCreateView.as_view(), name="author-create"),
]

app_name = "catalog"
