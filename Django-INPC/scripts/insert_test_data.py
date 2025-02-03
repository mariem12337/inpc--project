import os
import django
import random
from datetime import datetime, timedelta
from decimal import Decimal

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inpc.settings')
django.setup()

from pages.models import Product, ProductPrice, Cart, CartProducts

def create_test_data():
    # 1. Créer des produits de test
    products = [
        {'name': 'Pain', 'code': 'PAIN001', 'description': 'Pain de base'},
        {'name': 'Lait', 'code': 'LAIT001', 'description': 'Lait entier'},
        {'name': 'Riz', 'code': 'RIZ001', 'description': 'Riz blanc'},
        {'name': 'Huile', 'code': 'HUIL001', 'description': 'Huile végétale'},
        {'name': 'Sucre', 'code': 'SUCR001', 'description': 'Sucre blanc'},
    ]

    created_products = []
    for product_data in products:
        product, created = Product.objects.get_or_create(
            code=product_data['code'],
            defaults={
                'name': product_data['name'],
                'description': product_data['description']
            }
        )
        created_products.append(product)
        print(f"Produit {'créé' if created else 'existant'}: {product.name}")

    # 2. Créer des paniers de test
    carts = [
        {'name': 'Panier de base', 'description': 'Produits de première nécessité'},
        {'name': 'Panier familial', 'description': 'Produits pour une famille'},
    ]

    created_carts = []
    for cart_data in carts:
        cart, created = Cart.objects.get_or_create(
            name=cart_data['name'],
            defaults={'description': cart_data['description']}
        )
        created_carts.append(cart)
        print(f"Panier {'créé' if created else 'existant'}: {cart.name}")

    # 3. Ajouter des produits aux paniers avec des pondérations
    weights = [0.3, 0.25, 0.2, 0.15, 0.1]  # Total = 1
    for cart in created_carts:
        for product, weight in zip(created_products, weights):
            cart_product, created = CartProducts.objects.get_or_create(
                cart=cart,
                product=product,
                defaults={
                    'weight': weight,
                    'date_from': datetime(2023, 1, 1),
                    'date_to': datetime(2025, 12, 31)
                }
            )
            print(f"Produit {product.name} {'ajouté au' if created else 'déjà dans le'} panier {cart.name}")

    # 4. Créer des prix pour chaque produit sur plusieurs mois
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 12, 31)
    base_prices = {
        'PAIN001': 100,  # Prix de base en unités monétaires
        'LAIT001': 150,
        'RIZ001': 200,
        'HUIL001': 300,
        'SUCR001': 120,
    }

    for product in created_products:
        current_date = start_date
        base_price = base_prices[product.code]
        
        while current_date <= end_date:
            # Simuler une variation de prix de ±10%
            variation = random.uniform(-0.1, 0.1)
            price = base_price * (1 + variation)
            
            # Créer le prix pour ce mois
            price_obj, created = ProductPrice.objects.get_or_create(
                produit=product,
                date_de_debut=current_date,
                defaults={
                    'date_fin': current_date + timedelta(days=30),
                    'valeur': Decimal(str(round(price, 2)))
                }
            )
            
            if created:
                print(f"Prix créé pour {product.name}: {price_obj.valeur} (date: {current_date.strftime('%Y-%m')})")
            
            # Passer au mois suivant
            current_date = (current_date.replace(day=1) + timedelta(days=32)).replace(day=1)
            
            # Augmenter légèrement le prix de base pour simuler l'inflation
            base_price *= 1.002

if __name__ == '__main__':
    create_test_data()
