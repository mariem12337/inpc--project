-- Insérer des types de produits
INSERT INTO pages_producttype (code, label, description) VALUES
('ALI', 'Alimentation', 'Produits alimentaires de base'),
('HYG', 'Hygiène', 'Produits d''hygiène et de soins'),
('HAB', 'Habillement', 'Vêtements et accessoires');

-- Insérer des familles de produits
INSERT INTO pages_famille (nom) VALUES
('Céréales'),
('Produits laitiers'),
('Viandes'),
('Légumes'),
('Fruits');

-- Insérer des produits
INSERT INTO pages_product (code, name, description, unit_measure, product_type_id, famille_id) VALUES
('RIZ001', 'Riz', 'Riz blanc de qualité supérieure', 'kg', 1, 1),
('LAI001', 'Lait', 'Lait entier', 'litre', 1, 2),
('VIA001', 'Viande bovine', 'Viande de bœuf fraîche', 'kg', 1, 3),
('TOM001', 'Tomates', 'Tomates fraîches', 'kg', 1, 4),
('BAN001', 'Bananes', 'Bananes fraîches', 'kg', 1, 5);

-- Insérer une wilaya
INSERT INTO pages_wilaya (code, name) VALUES ('W01', 'Nouakchott');

-- Insérer une moughataa
INSERT INTO pages_moughataa (code, label, wilaya_id) VALUES ('M01', 'Tevragh Zeina', 1);

-- Insérer une commune
INSERT INTO pages_commune (code, name, moughataa_id) VALUES ('C01', 'Tevragh Zeina Nord', 1);

-- Insérer des points de vente
INSERT INTO pages_pointofsale (code, type, gps_lat, gps_lon, commune_id) VALUES
('MAR001', 'Marché', 18.1091, -15.9785, 1),
('SUP001', 'Supermarché', 18.1156, -15.9794, 1);

-- Insérer des prix de produits (12 mois de données)
INSERT INTO pages_productprice (valeur, date_de_debut, date_fin, produit_id, point_de_vente_id) VALUES
-- Riz
(350.00, '2024-01-01', '2024-01-31', 1, 1),
(360.00, '2024-02-01', '2024-02-29', 1, 1),
(370.00, '2024-03-01', '2024-03-31', 1, 1),
(380.00, '2024-04-01', '2024-04-30', 1, 1),
(390.00, '2024-05-01', '2024-05-31', 1, 1),
(400.00, '2024-06-01', '2024-06-30', 1, 1),
-- Lait
(280.00, '2024-01-01', '2024-01-31', 2, 1),
(285.00, '2024-02-01', '2024-02-29', 2, 1),
(290.00, '2024-03-01', '2024-03-31', 2, 1),
(295.00, '2024-04-01', '2024-04-30', 2, 1),
(300.00, '2024-05-01', '2024-05-31', 2, 1),
(305.00, '2024-06-01', '2024-06-30', 2, 1),
-- Viande
(1500.00, '2024-01-01', '2024-01-31', 3, 1),
(1550.00, '2024-02-01', '2024-02-29', 3, 1),
(1600.00, '2024-03-01', '2024-03-31', 3, 1),
(1650.00, '2024-04-01', '2024-04-30', 3, 1),
(1700.00, '2024-05-01', '2024-05-31', 3, 1),
(1750.00, '2024-06-01', '2024-06-30', 3, 1);

-- Insérer des paniers
INSERT INTO pages_cart (code, name, description) VALUES
('PAN001', 'Panier de base', 'Panier contenant les produits de première nécessité'),
('PAN002', 'Panier familial', 'Panier adapté aux besoins d''une famille');

-- Insérer des produits dans les paniers avec leurs poids
INSERT INTO pages_cartproducts (product_id, cart_id, weight, date_from, date_to) VALUES
-- Panier de base
(1, 1, 0.3, '2024-01-01', '2024-12-31'),  -- Riz
(2, 1, 0.2, '2024-01-01', '2024-12-31'),  -- Lait
(3, 1, 0.5, '2024-01-01', '2024-12-31'),  -- Viande
-- Panier familial
(1, 2, 0.25, '2024-01-01', '2024-12-31'), -- Riz
(2, 2, 0.25, '2024-01-01', '2024-12-31'), -- Lait
(3, 2, 0.5, '2024-01-01', '2024-12-31');  -- Viande
