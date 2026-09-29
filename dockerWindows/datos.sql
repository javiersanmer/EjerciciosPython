CREATE DATABASE IF NOT EXISTS juegos;
USE juegos;

CREATE TABLE IF NOT EXISTS videojuegos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    portada VARCHAR(255) NOT NULL,
    fecha_lanzamiento DATE
);

INSERT INTO videojuegos (titulo, portada, fecha_lanzamiento) VALUES
('Minecraft', 'minecraft.jpg', '2011-11-18'),
('Grand Theft Auto V', 'gta.jpg', '2013-09-17'),
('The Witcher 3: Wild Hunt', 'witcher.jpg', '2015-05-19'),
('Red Dead Redemption 2', 'rdr2.jpg', '2018-10-26'),
('Elden Ring', 'eldenring.jpg', '2022-02-25');