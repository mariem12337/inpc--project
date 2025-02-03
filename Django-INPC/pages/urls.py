from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Authentification
    path('connexion/', views.connexion, name='connexion'),
    path('accueil/', login_required(views.accueil), name='accueil'),
    path('', login_required(views.home), name='home'),

    # Gestion des Wilayas
    path('wilayas/', login_required(views.gestion_wilayas), name='gestion_wilayas'),

    # Gestion des Moughataas
    path('moughataas/', login_required(views.gestion_moughataas), name='gestion_moughataas'),

    # Gestion des Communes
    path('communes/', login_required(views.gestion_communes), name='gestion_communes'),

    # Gestion des Produits
    path('produits/', login_required(views.gestion_produits), name='gestion_produits'),
    # Suppression de produit
    path('produits/delete/<int:product_id>/', login_required(views.delete_product), name='delete_product'),

    # Gestion des Types de Produits
    path('product_types/', login_required(views.gestion_product_types), name='gestion_product_types'),

    # Gestion des Points de Vente
    path('points_de_vente/', login_required(views.gestion_points_de_vente), name='gestion_points_de_vente'),

    # Gestion des Prix des Produits
    path('product_prices/', login_required(views.gestion_product_prices), name='gestion_product_prices'),

    # Gestion des Paniers
    path('paniers/', login_required(views.gestion_paniers), name='gestion_paniers'),

    # Gestion des Produits dans les Paniers
    path('cart_products/', login_required(views.gestion_cart_products), name='gestion_cart_products'),

    # Gestion des Familles
    path('familles/', login_required(views.gestion_familles), name='gestion_familles'),

    # Import/Export
    path('import/', login_required(views.import_data), name='import_data'),
    path('export/', login_required(views.export_data), name='export_data'),
    
    # Calcul INPC
    path('calculate_inpc/', login_required(views.calculate_inpc), name='calculate_inpc'),
]
