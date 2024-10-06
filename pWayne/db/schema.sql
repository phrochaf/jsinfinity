-- db/schema.sql
CREATE DATABASE wayne_security;
USE wayne_security;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(100) NOT NULL,
    role ENUM('employee', 'manager', 'security_admin') NOT NULL
);

CREATE TABLE resources (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    description TEXT,
    quantity INT
);

DESCRIBE users;

ALTER TABLE users MODIFY password VARCHAR(255);

SELECT * FROM users;

ALTER TABLE users ADD COLUMN role VARCHAR(20);

ALTER TABLE resources ADD COLUMN description TEXT;
ALTER TABLE resources ADD COLUMN status ENUM('available', 'in_use', 'maintenance') DEFAULT 'available';

ALTER TABLE resources MODIFY COLUMN name VARCHAR(150);  -- Aumenta o tamanho da coluna 'name'
ALTER TABLE resources MODIFY COLUMN quantity INT NOT NULL;  -- Torna a coluna 'quantity' obrigatória
USE wayne_security;

select * from resources

ALTER TABLE resources ADD COLUMN location TEXT;

INSERT INTO resources (name, location, quantity, description, status) VALUES
('Câmera de Vigilância', 'Setor A - Entrada', 15, 'Equipamentos de Vigilância', 'available'),
('Colete à Prova de Balas', 'Depósito Central', 50, 'Acessórios de Segurança', 'available'),
('Veículo Blindado', 'Garagem Sul', 5, 'Veículos de Segurança', 'in_use'),
('Sistema de Controle Biométrico', 'Sede Principal', 8, 'Sistemas de Controle de Acesso', 'available'),
('Manual de Procedimentos', 'Escritório', 100, 'Material de Treinamento', 'in_use'),
('Container de Armazenamento', 'Setor B - Armazém', 10, 'Armazenamento e Transporte', 'available'),
('Rádio Comunicador', 'Setor C - Base', 25, 'Dispositivos de Comunicação', 'available'),
('Pistola Glock 17', 'Arsenal', 30, 'Armas', 'in_use'),
('Espingarda Remington 870', 'Arsenal', 12, 'Armas', 'maintenance'),
('Sistema de Monitoramento de Tráfego', 'Setor D - Portaria', 3, 'Equipamentos de Vigilância', 'maintenance');
