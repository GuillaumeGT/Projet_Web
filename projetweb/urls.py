"""projetweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accueil, name='accueil'),
    path('signup/', views.signupJoueur, name='signup'),
    path('signin/', auth_views.LoginView.as_view(template_name='signin_joueur.html',redirect_field_name='accueil'), name='signin'),
    path('logout/', views.logoutJoueur, name='logout'),
    path('account/', views.moncompteJoueur, name='account'),
    path('account/update', views.updateJoueur, name='update_joueur'),
    path('friend/dashboard/', views.dashboardAmis, name='dashboard_amis'),
    path('friend/sendto/', views.demandeAmis, name='create_amis'),
    path('friend/search/', views.rechercheAmis, name='search_amis'),
    path('friend/accept/', views.accepteAmis, name='accept_amis'),
    path('friend/delete/', views.supprimerAmis, name='delete_amis'),
    path('rencontre/organiser/', views.createRencontre, name='create_rencontre'),#Reste url : /list/delete
    path('rencontre/read/<int:idRencontre>', views.readRencontre, name='read_rencontre'),
    path('rencontre/update/<int:idRencontre>', views.updateRencontre, name='update_rencontre'),
    #path('rencontre/delete/<int:idRencontre>', views.deleteRencontre, name='delete_rencontre'),
    #path('rencontre/list/', views.listRencontre, name='list_rencontre'),
    path('stade/creation/', views.createStade, name='create_stade'),
    path('stade/read/<int:idStade>', views.readStade, name='read_stade'),
    path('stade/update/<int:idStade>', views.updateStade, name='update_stade'),
    path('stade/delete/<int:idStade>', views.deleteStade, name='delete_stade'),
    path('stade/list/', views.listStade, name='list_stade'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
