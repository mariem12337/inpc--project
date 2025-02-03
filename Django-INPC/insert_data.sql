-- Nettoyage dans l'ordre inverse des dépendances
DELETE FROM pages_cartproducts;
DELETE FROM pages_productprice;
DELETE FROM pages_product;
DELETE FROM pages_pointofsale;
DELETE FROM pages_commune;
DELETE FROM pages_moughataa;
DELETE FROM pages_wilaya;
DELETE FROM pages_producttype;
DELETE FROM pages_famille;
DELETE FROM pages_cart;

-- 1. Tables indépendantes
-- Wilaya
INSERT INTO pages_wilaya (id, code, name) VALUES 
(1, 'W01', 'Nouakchott');

-- ProductType
INSERT INTO pages_producttype (id, code, label, description) VALUES 
(1, 'ALI', 'Alimentation', 'Produits alimentaires de base');

-- Famille
INSERT INTO pages_famille (id, nom, description) VALUES 
(1, 'Céréales', 'Produits céréaliers'),
(2, 'Produits laitiers', 'Produits laitiers et dérivés'),
(3, 'Viandes', 'Viandes et produits carnés');

-- Cart
INSERT INTO pages_cart (id, code, name, description) VALUES 
(1, 'PAN001', 'Panier de base', 'Panier contenant les produits de première nécessité');

-- 2. Dépend de Wilaya
INSERT INTO pages_moughataa (id, code, label, wilaya_id) VALUES 
(1, 'M01', 'Tevragh Zeina', 1);

-- 3. Dépend de Moughataa
INSERT INTO pages_commune (id, code, name, moughataa_id) VALUES 
(1, 'C01', 'Tevragh Zeina Nord', 1);

-- 4. Dépend de Commune
INSERT INTO pages_pointofsale (id, code, type, gps_lat, gps_lon, commune_id) VALUES 
(1, 'MAR001', 'Marché', 18.1091, -15.9785, 1);

-- 5. Dépend de ProductType et Famille
INSERT INTO pages_product (id, code, name, description, unit_measure, product_type_id, famille_id) VALUES 
(1, 'RIZ001', 'Riz', 'Riz blanc de qualité supérieure', 'kg', 1, 1),
(2, 'LAI001', 'Lait', 'Lait entier', 'litre', 1, 2),
(3, 'VIA001', 'Viande bovine', 'Viande de bœuf fraîche', 'kg', 1, 3);

-- 6. Dépend de Product et PointOfSale
-- Prix des produits (6 mois)
-- Riz (commence à 350, +10 par mois)
INSERT INTO pages_productprice (id, valeur, date_de_debut, date_fin, produit_id, point_de_vente_id) VALUES 
(1, 350.00, '2024-01-01', '2024-01-31', 1, 1),
(2, 360.00, '2024-02-01', '2024-02-29', 1, 1),
(3, 370.00, '2024-03-01', '2024-03-31', 1, 1),
(4, 380.00, '2024-04-01', '2024-04-30', 1, 1),
(5, 390.00, '2024-05-01', '2024-05-31', 1, 1),
(6, 400.00, '2024-06-01', '2024-06-30', 1, 1);

-- Lait (commence à 280, +5 par mois)
INSERT INTO pages_productprice (id, valeur, date_de_debut, date_fin, produit_id, point_de_vente_id) VALUES 
(7, 280.00, '2024-01-01', '2024-01-31', 2, 1),
(8, 285.00, '2024-02-01', '2024-02-29', 2, 1),
(9, 290.00, '2024-03-01', '2024-03-31', 2, 1),
(10, 295.00, '2024-04-01', '2024-04-30', 2, 1),
(11, 300.00, '2024-05-01', '2024-05-31', 2, 1),
(12, 305.00, '2024-06-01', '2024-06-30', 2, 1);

-- Viande (commence à 1500, +50 par mois)
INSERT INTO pages_productprice (id, valeur, date_de_debut, date_fin, produit_id, point_de_vente_id) VALUES 
(13, 1500.00, '2024-01-01', '2024-01-31', 3, 1),
(14, 1550.00, '2024-02-01', '2024-02-29', 3, 1),
(15, 1600.00, '2024-03-01', '2024-03-31', 3, 1),
(16, 1650.00, '2024-04-01', '2024-04-30', 3, 1),
(17, 1700.00, '2024-05-01', '2024-05-31', 3, 1),
(18, 1750.00, '2024-06-01', '2024-06-30', 3, 1);

-- 7. Dépend de Product et Cart
-- Produits dans le panier avec leurs poids
INSERT INTO pages_cartproducts (id, product_id, cart_id, weight, date_from, date_to) VALUES 
(1, 1, 1, 0.3, '2024-01-01', '2024-12-31'),  -- Riz (30%)
(2, 2, 1, 0.2, '2024-01-01', '2024-12-31'),  -- Lait (20%)
(3, 3, 1, 0.5, '2024-01-01', '2024-12-31');  -- Viande (50%)
