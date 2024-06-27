-- Drop tables if they exist
DROP TABLE IF EXISTS `todo`;
DROP TABLE IF EXISTS `project`;
DROP TABLE IF EXISTS `user`;

-- Create user table
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(80) NOT NULL,
  `password` varchar(80) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
);

-- Populate user table


-- Create project table
CREATE TABLE `project` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `project_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
); 

-- Populate project table (ensure all user_ids exist in `user` table)


-- Create todo table
CREATE TABLE `todo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `description` varchar(999) DEFAULT NULL,
  `due_date` datetime DEFAULT NULL,
  `project_id` int DEFAULT NULL,
  `author` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `project_id` (`project_id`),
  CONSTRAINT `todo_ibfk_1` FOREIGN KEY (`project_id`) REFERENCES `project` (`id`)
);

-- Populate todo table

