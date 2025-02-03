-- Supprimer les données existantes
DELETE FROM pages_productprice;
DELETE FROM pages_cartproducts;
DELETE FROM pages_product;
DELETE FROM pages_producttype;
DELETE FROM pages_famille;
DELETE FROM pages_cart;
DELETE FROM pages_pointofsale;
DELETE FROM pages_commune;
DELETE FROM pages_moughataa;
DELETE FROM pages_wilaya;

-- Type de produit
INSERT INTO pages_producttype (id, code, label, description) VALUES 
(1, 'ALI', 'Alimentation', 'Produits alimentaires de base');

-- Familles
INSERT INTO pages_famille (id, nom, description) VALUES 
(1, 'Céréales', 'Produits céréaliers'),
(2, 'Produits laitiers', 'Produits laitiers et dérivés'),
(3, 'Viandes', 'Viandes et produits carnés');

-- Wilaya
INSERT INTO pages_wilaya (id, code, name) VALUES 
(1, 'W01', 'Nouakchott');

-- Moughataa
INSERT INTO pages_moughataa (id, code, label, wilaya_id) VALUES 
(1, 'M01', 'Tevragh Zeina', 1);

-- Commune
INSERT INTO pages_commune (id, code, name, moughataa_id) VALUES 
(1, 'C01', 'Tevragh Zeina Nord', 1);

-- Point de vente
INSERT INTO pages_pointofsale (id, code, type, gps_lat, gps_lon, commune_id) VALUES 
(1, 'MAR001', 'Marché', 18.1091, -15.9785, 1);

-- Produits
INSERT INTO pages_product (id, code, name, description, unit_measure, product_type_id, famille_id) VALUES 
(1, 'RIZ001', 'Riz', 'Riz blanc de qualité supérieure', 'kg', 1, 1),
(2, 'LAI001', 'Lait', 'Lait entier', 'litre', 1, 2),
(3, 'VIA001', 'Viande bovine', 'Viande de bœuf fraîche', 'kg', 1, 3);

-- Panier
INSERT INTO pages_cart (id, code, name, description) VALUES 
(1, 'PAN001', 'Panier de base', 'Panier contenant les produits de première nécessité');

-- Prix des produits (12 mois avec inflation différenciée)
-- Riz (inflation modérée)
INSERT INTO pages_productprice (valeur, date_de_debut, date_fin, produit_id, point_de_vente_id) VALUES 
(350.00, '2024-01-01', '2024-01-31', 1, 1),
(355.00, '2024-02-01', '2024-02-29', 1, 1),
(360.00, '2024-03-01', '2024-03-31', 1, 1),
(365.00, '2024-04-01', '2024-04-30', 1, 1),
(370.00, '2024-05-01', '2024-05-31', 1, 1),
(375.00, '2024-06-01', '2024-06-30', 1, 1),
(380.00, '2024-07-01', '2024-07-31', 1, 1),
(385.00, '2024-08-01', '2024-08-31', 1, 1),
(390.00, '2024-09-01', '2024-09-30', 1, 1),
(395.00, '2024-10-01', '2024-10-31', 1, 1),
(400.00, '2024-11-01', '2024-11-30', 1, 1),
(405.00, '2024-12-01', '2024-12-31', 1, 1);

-- Lait (inflation faible)
INSERT INTO pages_productprice (valeur, date_de_debut, date_fin, produit_id, point_de_vente_id) VALUES 
(280.00, '2024-01-01', '2024-01-31', 2, 1),
(282.00, '2024-02-01', '2024-02-29', 2, 1),
(284.00, '2024-03-01', '2024-03-31', 2, 1),
(286.00, '2024-04-01', '2024-04-30', 2, 1),
(288.00, '2024-05-01', '2024-05-31', 2, 1),
(290.00, '2024-06-01', '2024-06-30', 2, 1),
(292.00, '2024-07-01', '2024-07-31', 2, 1),
(294.00, '2024-08-01', '2024-08-31', 2, 1),
(296.00, '2024-09-01', '2024-09-30', 2, 1),
(298.00, '2024-10-01', '2024-10-31', 2, 1),
(300.00, '2024-11-01', '2024-11-30', 2, 1),
(302.00, '2024-12-01', '2024-12-31', 2, 1);

-- Viande (inflation élevée)
INSERT INTO pages_productprice (valeur, date_de_debut, date_fin, produit_id, point_de_vente_id) VALUES 
(1500.00, '2024-01-01', '2024-01-31', 3, 1),
(1550.00, '2024-02-01', '2024-02-29', 3, 1),
(1600.00, '2024-03-01', '2024-03-31', 3, 1),
(1650.00, '2024-04-01', '2024-04-30', 3, 1),
(1700.00, '2024-05-01', '2024-05-31', 3, 1),
(1750.00, '2024-06-01', '2024-06-30', 3, 1),
(1800.00, '2024-07-01', '2024-07-31', 3, 1),
(1850.00, '2024-08-01', '2024-08-31', 3, 1),
(1900.00, '2024-09-01', '2024-09-30', 3, 1),
(1950.00, '2024-10-01', '2024-10-31', 3, 1),
(2000.00, '2024-11-01', '2024-11-30', 3, 1),
(2050.00, '2024-12-01', '2024-12-31', 3, 1);

-- Produits dans le panier avec leurs poids (valide toute l'année)
INSERT INTO pages_cartproducts (product_id, cart_id, weight, date_from, date_to) VALUES 
(1, 1, 0.3, '2024-01-01', '2024-12-31'),  -- Riz (30%)
(2, 1, 0.2, '2024-01-01', '2024-12-31'),  -- Lait (20%)
(3, 1, 0.5, '2024-01-01', '2024-12-31');  -- Viande (50%)
