from django.core.management.base import BaseCommand
from pages.models import *
from decimal import Decimal
from datetime import date

class Command(BaseCommand):
    help = 'Charge des données de test dans la base de données'

    def handle(self, *args, **options):
        self.stdout.write('Suppression des données existantes...')
        
        # Supprimer toutes les données existantes
        ProductPrice.objects.all().delete()
        CartProducts.objects.all().delete()
        Product.objects.all().delete()
        ProductType.objects.all().delete()
        Famille.objects.all().delete()
        Cart.objects.all().delete()
        PointOfSale.objects.all().delete()
        Commune.objects.all().delete()
        Moughataa.objects.all().delete()
        Wilaya.objects.all().delete()

        self.stdout.write('Création des types de produits...')
        # Créer un type de produit
        type_alim = ProductType.objects.create(
            code='ALI',
            label='Alimentation',
            description='Produits alimentaires de base'
        )

        self.stdout.write('Création des familles...')
        # Créer des familles
        famille_cereales = Famille.objects.create(nom='Céréales')
        famille_lait = Famille.objects.create(nom='Produits laitiers')
        famille_viande = Famille.objects.create(nom='Viandes')

        self.stdout.write('Création des produits...')
        # Créer des produits
        riz = Product.objects.create(
            code='RIZ001',
            name='Riz',
            description='Riz blanc de qualité supérieure',
            unit_measure='kg',
            product_type=type_alim,
            famille=famille_cereales
        )

        lait = Product.objects.create(
            code='LAI001',
            name='Lait',
            description='Lait entier',
            unit_measure='litre',
            product_type=type_alim,
            famille=famille_lait
        )

        viande = Product.objects.create(
            code='VIA001',
            name='Viande bovine',
            description='Viande de bœuf fraîche',
            unit_measure='kg',
            product_type=type_alim,
            famille=famille_viande
        )

        self.stdout.write('Création de la hiérarchie administrative...')
        # Créer la hiérarchie administrative
        wilaya = Wilaya.objects.create(code='W01', name='Nouakchott')
        moughataa = Moughataa.objects.create(code='M01', label='Tevragh Zeina', wilaya=wilaya)
        commune = Commune.objects.create(code='C01', name='Tevragh Zeina Nord', moughataa=moughataa)

        self.stdout.write('Création des points de vente...')
        # Créer un point de vente
        pos = PointOfSale.objects.create(
            code='MAR001',
            type='Marché',
            gps_lat=18.1091,
            gps_lon=-15.9785,
            commune=commune
        )

        self.stdout.write('Création des prix...')
        # Créer des prix pour chaque produit (6 mois)
        products = [riz, lait, viande]
        base_prices = [Decimal('350'), Decimal('280'), Decimal('1500')]
        increments = [Decimal('10'), Decimal('5'), Decimal('50')]

        for month in range(1, 7):
            start_day = date(2024, month, 1)
            end_day = date(2024, month + 1, 1) if month < 12 else date(2025, 1, 1)
            
            for i, product in enumerate(products):
                ProductPrice.objects.create(
                    valeur=base_prices[i] + (month * increments[i]),
                    date_de_debut=start_day,
                    date_fin=end_day,
                    produit=product,
                    point_de_vente=pos
                )

        self.stdout.write('Création des paniers...')
        # Créer des paniers
        panier_base = Cart.objects.create(
            code='PAN001',
            name='Panier de base',
            description='Panier contenant les produits de première nécessité'
        )

        self.stdout.write('Ajout des produits aux paniers...')
        # Ajouter des produits aux paniers avec leurs poids
        weights = [Decimal('0.3'), Decimal('0.2'), Decimal('0.5')]
        for i, product in enumerate(products):
            CartProducts.objects.create(
                product=product,
                cart=panier_base,
                weight=weights[i],
                date_from=date(2024, 1, 1),
                date_to=date(2024, 12, 31)
            )

        # Afficher les statistiques
        self.stdout.write(self.style.SUCCESS('Données de test insérées avec succès!'))
        self.stdout.write(f'Nombre de produits : {Product.objects.count()}')
        self.stdout.write(f'Nombre de prix : {ProductPrice.objects.count()}')
        self.stdout.write(f'Nombre de paniers : {Cart.objects.count()}')
        self.stdout.write(f'Nombre de produits dans les paniers : {CartProducts.objects.count()}')
