-- 1. Chiffre d'affaires total
SELECT SUM(CAST(c3 AS REAL) * CAST(c4 AS REAL)) AS chiffre_affaires_total
FROM ventes
WHERE c1 != 'date';

-- 2. Ventes par produit
SELECT c2 AS produit, SUM(CAST(c3 AS INTEGER)) AS total_ventes
FROM ventes
WHERE c1 != 'date'
GROUP BY c2;

-- 3. Ventes par région
SELECT c5 AS region, SUM(CAST(c3 AS INTEGER)) AS total_ventes
FROM ventes
WHERE c1 != 'date'
GROUP BY c5;
