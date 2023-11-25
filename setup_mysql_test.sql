-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS club_test_db;
CREATE USER IF NOT EXISTS 'club_test'@'localhost' IDENTIFIED BY 'club_test_pwd';
GRANT ALL PRIVILEGES ON `club_test_db`.* TO 'club_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'club_test'@'localhost';
FLUSH PRIVILEGES;