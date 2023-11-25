-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS club_db;
CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'admin_pwd';
GRANT ALL PRIVILEGES ON `club_db`.* TO 'admin'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'admin'@'localhost';
FLUSH PRIVILEGES;