-- A script that creates a database 'hbnb_dev_db'
-- And a database 'performance_schema'
-- A new user 'hbnb_dev' with the password 'hbnb_dv_db'
-- The use must have all privileges on the database 'hbnb_dev_db'
-- And SELECT privilege on 'performance_schema'

CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;
CREATE DATABASE IF NOT EXISTS `performance_schema`;

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
