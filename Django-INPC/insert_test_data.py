from django.core.management.base import BaseCommand
from pages.models import ProductType, Famille, Product, Wilaya, Moughataa, Commune, PointOfSale, ProductPrice, Cart, CartProducts
from decimal import Decimal
from datetime import date

def run():
    # Types de produits
    types = [
        ProductType.objects.create(code='ALI', label='Alimentation', description='Produits alimentaires de base'),
        ProductType.objects.create(code='HYG', label='Hygiène', description='Produits d''hygiène et de soins'),
        ProductType.objects.create(code='HAB', label='Habillement', description='Vêtements et accessoires')
    ]

    # Familles
    familles = [
        Famille.objects.create(nom='Céréales'),
        Famille.objects.create(nom='Produits laitiers'),
        Famille.objects.create(nom='Viandes'),
        Famille.objects.create(nom='Légumes'),
        Famille.objects.create(nom='Fruits')
    ]

    # Produits
    products = [
        Product.objects.create(code='RIZ001', name='Riz', description='Riz blanc de qualité supérieure', 
                             unit_measure='kg', product_type=types[0], famille=familles[0]),
        Product.objects.create(code='LAI001', name='Lait', description='Lait entier', 
                             unit_measure='litre', product_type=types[0], famille=familles[1]),
        Product.objects.create(code='VIA001', name='Viande bovine', description='Viande de bœuf fraîche', 
                             unit_measure='kg', product_type=types[0], famille=familles[2])
    ]

    # Wilaya, Moughataa, Commune
    wilaya = Wilaya.objects.create(code='W01', name='Nouakchott')
    moughataa = Moughataa.objects.create(code='M01', label='Tevragh Zeina', wilaya=wilaya)
    commune = Commune.objects.create(code='C01', name='Tevragh Zeina Nord', moughataa=moughataa)

    # Points de vente
    pos = PointOfSale.objects.create(code='MAR001', type='Marché', gps_lat=18.1091, 
                                   gps_lon=-15.9785, commune=commune)

    # Prix des produits (6 mois de données)
    for month in range(1, 7):
        start_day = date(2024, month, 1)
        end_day = date(2024, month + 1, 1) if month < 12 else date(2025, 1, 1)
        
        # Prix croissants pour simuler l'inflation
        ProductPrice.objects.create(
            valeur=Decimal('350') + (month * Decimal('10')),
            date_de_debut=start_day,
            date_fin=end_day,
            produit=products[0],
            point_de_vente=pos
        )
        
        ProductPrice.objects.create(
            valeur=Decimal('280') + (month * Decimal('5')),
            date_de_debut=start_day,
            date_fin=end_day,
            produit=products[1],
            point_de_vente=pos
        )
        
        ProductPrice.objects.create(
            valeur=Decimal('1500') + (month * Decimal('50')),
            date_de_debut=start_day,
            date_fin=end_day,
            produit=products[2],
            point_de_vente=pos
        )

    # Paniers
    carts = [
        Cart.objects.create(code='PAN001', name='Panier de base', 
                          description='Panier contenant les produits de première nécessité'),
        Cart.objects.create(code='PAN002', name='Panier familial', 
                          description='Panier adapté aux besoins d''une famille')
    ]

    # Produits dans les paniers
    weights = [Decimal('0.3'), Decimal('0.2'), Decimal('0.5')]
    for cart in carts:
        for i, product in enumerate(products):
            CartProducts.objects.create(
                product=product,
                cart=cart,
                weight=weights[i],
                date_from=date(2024, 1, 1),
                date_to=date(2024, 12, 31)
            )

if __name__ == '__main__':
    run()
