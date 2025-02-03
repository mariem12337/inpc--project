from django.db.models import Avg, DecimalField, Sum, F, ExpressionWrapper, Q
from django.db.models.functions import Coalesce, ExtractYear, ExtractMonth
from decimal import Decimal
from .models import Product, ProductPrice, Cart, CartProducts
from datetime import datetime
from dateutil.relativedelta import relativedelta

def calculate_inpc_for_date(date):
    """
    Calcule l'INPC pour une date donnée.
    """
    print(f"Calcul de l'INPC pour la date : {date}")  # Log de débogage
    product_avg_prices = {}
    for product in Product.objects.all():
        avg_price_query = ProductPrice.objects.filter(
            produit=product,
            date_de_debut__lte=date,
            date_fin__gte=date
        )
        print(f"Requête pour le produit {product.name}: {avg_price_query.query}")  # Log de requête
        
        avg_price = avg_price_query.aggregate(
            avg_price=ExpressionWrapper(
                Avg('valeur'),
                output_field=DecimalField(max_digits=10, decimal_places=2)
            )
        )['avg_price']

        print(f"Prix moyen pour {product.name}: {avg_price}")  # Log de prix

        if avg_price is not None:
            product_avg_prices[product.id] = Decimal(str(avg_price))

    if not product_avg_prices:
        print("Aucun prix moyen trouvé")  # Log
        return Decimal('0')  # Aucun prix disponible

    cart_inpc = {}
    for cart in Cart.objects.all():
        total_weighted_price = Decimal('0')
        total_weight = Decimal('0')

        cart_products = CartProducts.objects.filter(
            cart=cart,
            date_from__lte=date,
            date_to__gte=date
        )
        print(f"Produits dans le panier {cart.name}: {list(cart_products.values())}")  # Log des produits du panier

        for cart_product in cart_products:
            product_id = cart_product.product.id
            if product_id in product_avg_prices:
                weight = Decimal(str(cart_product.weight))
                total_weighted_price += product_avg_prices[product_id] * weight
                total_weight += weight

        if total_weight > 0:
            cart_inpc[cart.id] = total_weighted_price / total_weight

    # Retourner la moyenne des INPC de tous les paniers
    if cart_inpc:
        total = sum(Decimal(str(value)) for value in cart_inpc.values())
        count = Decimal(str(len(cart_inpc)))
        result = total / count
        print(f"INPC final : {result}")  # Log du résultat
        return result
    print("Aucun INPC calculé")  # Log
    return Decimal('0')

def calculate_inpc_for_period(year=None, month=None):
    """
    Calcule l'INPC pour une période donnée (année et mois optionnel).
    Retourne les résultats détaillés par produit et le total.
    """
    from django.db.models import Q, Sum, Avg, F, ExpressionWrapper, DecimalField
    from django.db.models.functions import Coalesce

    print(f"Calcul de l'INPC pour l'année {year}, mois {month}")  # Log de débogage
    
    # Construire le filtre de base pour la période
    date_filter = Q()
    if year:
        date_filter &= Q(date_de_debut__year=year)
    if month:
        date_filter &= Q(date_de_debut__month=month)

    # 1. Calculer les prix moyens par produit pour la période
    product_prices = (
        ProductPrice.objects
        .filter(date_filter)
        .values('produit', 'produit__name', 'produit__code')
        .annotate(
            avg_price=ExpressionWrapper(
                Avg('valeur'),
                output_field=DecimalField(max_digits=10, decimal_places=2)
            )
        )
    )
    
    # Affichage détaillé des prix
    print("Prix des produits pour la période :")
    for price in product_prices:
        print(f"Produit: {price['produit__name']}, Code: {price['produit__code']}, Prix moyen: {price['avg_price']}")

    # 2. Calculer l'INPC par produit avec pondération
    products_data = []
    total_weighted_sum = Decimal('0')
    total_weight = Decimal('0')

    for product_price in product_prices:
        # Récupérer les pondérations du produit dans tous les paniers
        # Modification importante : utiliser une requête plus explicite
        product_weights = CartProducts.objects.filter(
            product_id=product_price['produit'],
            date_from__lte=datetime(year, month, 1) if year and month else F('date_from'),
            date_to__gte=datetime(year, month, 1) if year and month else F('date_to')
        ).aggregate(
            total_weight=Coalesce(
                Sum('weight'),
                Decimal('0'),
                output_field=DecimalField(max_digits=10, decimal_places=4)
            )
        )
        
        # Affichage détaillé des poids
        print(f"Poids pour {product_price['produit__name']}: {product_weights}")

        weight = product_weights['total_weight']
        if weight > 0:
            avg_price = Decimal(str(product_price['avg_price']))
            weighted_price = avg_price * weight
            inpc = weighted_price / weight

            total_weighted_sum += weighted_price
            total_weight += weight
            
            products_data.append({
                'product_code': product_price['produit__code'],
                'product_name': product_price['produit__name'],
                'avg_price': avg_price,
                'weight': weight,
                'inpc': inpc
            })

    # Calculer l'INPC total
    total_inpc = Decimal('0')
    if total_weight > 0:
        total_inpc = total_weighted_sum / total_weight

    print(f"Somme pondérée totale : {total_weighted_sum}")
    print(f"Poids total : {total_weight}")
    print(f"INPC total : {total_inpc}")

    return {
        'products': products_data,
        'total': total_inpc,
        'total_weight': total_weight,
        'period': {
            'year': year,
            'month': month
        }
    }


def get_inpc_evolution(start_year=2024, end_year=2024):
    """
    Récupère l'évolution de l'INPC pour l'année 2024 uniquement.
    Retourne les données formatées pour Chart.js.
    """
    labels = []
    values = []
    products_data = {}

    print(f"🔍 Calcul de l'évolution de l'INPC pour {start_year}")

    for month in range(1, 13):  # Boucle uniquement sur 2024
        try:
            result = calculate_inpc_for_period(start_year, month)

            # Vérifier si l'INPC est valide (> 0)
            if result['total'] > 0:
                month_name = datetime(start_year, month, 1).strftime('%B %Y')
                labels.append(month_name)
                values.append(float(result['total']))

                # Stocker les valeurs des produits
                for product in result['products']:
                    product_name = product['product_name']
                    if product_name not in products_data:
                        products_data[product_name] = []
                    products_data[product_name].append(float(product['inpc']))
            else:
                print(f"⚠️ Peu de données pour {month}/{start_year}, INPC non ajouté")

        except Exception as e:
            print(f"❌ Erreur pour {month}/{start_year}: {e}")

    print(f"📊 Labels (Mois disponibles) : {labels}")
    print(f"📈 Valeurs INPC Global : {values}")
    print(f"📊 Valeurs INPC par produit : {products_data}")

    return {
        'labels': labels,
        'values': values,
        'products': products_data
    }
