-- script that prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS tsp_db;
GRANT ALL PRIVILEGES ON tsp_db.* TO 'tsp_user'@'localhost' IDENTIFIED BY 'tsp_user_pwd';
GRANT SELECT ON performance_schema.* TO 'tsp_user'@'localhost';
