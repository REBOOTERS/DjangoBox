from django.urls import path

from . import views, views2

app_name = 'polls'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results', views.results, name='results'),
    # path('<int:question_id>/vote', views.vote, name='vote')

    path('', views2.IndexView.as_view(), name='index'),
    path('<int:pk>/', views2.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views2.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views2.vote, name='vote')
]
