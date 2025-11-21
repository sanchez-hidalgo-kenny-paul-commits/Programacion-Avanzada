-- Crear base de datos
CREATE DATABASE IF NOT EXISTS ciudad_servicios;
USE ciudad_servicios;

-- Tabla de Clínicas Particulares
CREATE TABLE clinicas_particulares (
    id_clinica INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(150),
    ciudad VARCHAR(80),
    telefono VARCHAR(20),
    tipo_servicio VARCHAR(80),       -- ej: odontología, pediatría, etc.
    horario VARCHAR(80),             -- ej: 08:00-18:00
    num_consultorios INT,
    tiene_emergencias BOOLEAN
);

-- Tabla de Parques Recreativos
CREATE TABLE parques_recreativos (
    id_parque INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(150),
    ciudad VARCHAR(80),
    area_m2 INT,
    tipo_parque VARCHAR(80),         -- ej: acuático, infantil, ecológico
    tiene_juegos_infantiles BOOLEAN,
    tiene_parqueadero BOOLEAN,
    precio_entrada DECIMAL(6,2),     -- 0 si es gratis
    horario VARCHAR(80)
);

-- Inserción de datos de ejemplo (almacenar información)

INSERT INTO clinicas_particulares
(nombre, direccion, ciudad, telefono, tipo_servicio, horario, num_consultorios, tiene_emergencias)
VALUES
('Clínica Santa María', 'Av. Siempre Viva 123', 'Quito', '022345678', 'Medicina general', '08:00-20:00', 10, TRUE),
('Centro Médico Vida Sana', 'Calle 10 de Agosto 456', 'Guayaquil', '042223344', 'Pediatría', '09:00-18:00', 6, FALSE);

INSERT INTO parques_recreativos
(nombre, direccion, ciudad, area_m2, tipo_parque, tiene_juegos_infantiles, tiene_parqueadero, precio_entrada, horario)
VALUES
('Parque La Alegría', 'Av. Los Álamos s/n', 'Quito', 15000, 'Infantil', TRUE, TRUE, 0.00, '07:00-19:00'),
('Aventura Park', 'Km 5 Vía a la Costa', 'Guayaquil', 25000, 'Acuático', TRUE, TRUE, 5.50, '09:00-18:00');

-- Consultas de ejemplo

-- Todas las clínicas
SELECT * FROM clinicas_particulares;

-- Clínicas con servicio de emergencias
SELECT nombre, ciudad
FROM clinicas_particulares
WHERE tiene_emergencias = TRUE;

-- Parques gratuitos
SELECT nombre, ciudad
FROM parques_recreativos
WHERE precio_entrada = 0;

-- Número de parques por ciudad
SELECT ciudad, COUNT(*) AS cantidad_parques
FROM parques_recreativos
GROUP BY ciudad;
