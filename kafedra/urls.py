from django.urls import path
from . import views


urlpatterns = [
    path('te-ach-er-s/', views.kafedrateachersview, name='teachers'),
    path('gr-an-ts/', views.kafedragrantview, name='grants'),
    path('si-nc-e/', views.kafedrasinceview, name='sinces'),
    path('li-f-es/', views.kafedralifesview, name='lifes'),
    path('inter-nati-o-nals/', views.kafedrinternatinalsview, name='international'),
    path('cul-tu-ra-ls/', views.kafedraculturalview, name='culturals'),
    path('up-da-te-te-ac-he-r/', views.kafedrupdatesview, name='updates'),
    path('teacher-single/<slug:teacher>/', views.teachersdetailview, name="teacher_detail"),
    path('teachers-search/', views.teacherssearchview, name="teachers_search"),
    path('since-single/<slug:since>/', views.sincedetailview, name="since_detail"),
    path('life-single/<slug:life>/', views.lifedetailview, name="life_detail"),
    path('grant-single/<slug:grant>/', views.grantdetailview, name="grant_detail"),
    path('international-single/<slug:international>/', views.internationaldetailview, name="international_detail"),
    path('teacher-update-single/<slug:teacher_update>/', views.teachersupdatedetailview, name="teacher_update_detail"),
    path('cultural-single/<slug:cultural>/', views.culturaldetailview, name="cultural_detail"),
    path('since-search/', views.sincesearchview, name="since_search"),
    path('life-search/', views.lifesearchview, name="life_search"),
    path('cultural-search/', views.culturalsearchview, name="cultural_search"),
    path('international-search/', views.internationalsearchview, name="international_search"),
    path('grant-search/', views.grantsearchview, name="grant_search"),
    path('teacher-update-search/', views.teacherupdatesearchview, name="teacher_update_search"),
]