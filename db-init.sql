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
INSERT INTO `user` (username, password, email) VALUES 
('admin','admin','admin@admin.com'),
('test','test',NULL),
('aabc','1234','test@123.de'),
('hallo123','uDjHwxooHcyaGwUNKM','test@schuttenberg.net'),
('public','',''),
('test123','test123','test@test.com');

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
INSERT INTO `project` (title, user_id) VALUES 
('Web2_Development',1),
('Web2_Projekt',4),
('Einkaufsliste',4),
('Shopping',4);

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
INSERT INTO `todo` (description, due_date, project_id, author) VALUES
('Build a Flask app','2024-05-01 00:00:00',1,NULL),
('Finalize project scope','2024-04-15 00:00:00',1,NULL),
('Implement authentication system','2024-04-25 00:00:00',1,NULL),
('Develop the user profile section','2024-05-05 00:00:00',1,NULL),
('Setup database backups','2024-05-10 00:00:00',1,NULL),
('Run user acceptance testing','2024-05-15 00:00:00',1,NULL),
('Conduct post-launch review meeting','2024-05-25 00:00:00',4,NULL),
('Salat',NULL,3,NULL),
('asdasd','2024-04-27 19:00:00',3,NULL),
('test',NULL,2,NULL),
('alio',NULL,4,NULL),
('testserfsdf',NULL,3,NULL),
('asdasd',NULL,4,NULL),
('asdasd',NULL,2,NULL),
('<script>alert(5)</script>',NULL,1,NULL),
('lol',NULL,3,NULL);
