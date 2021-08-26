-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: localhost    Database: db_students
-- ------------------------------------------------------
-- Server version	8.0.25

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
-- Table structure for table `tb_class`
--

DROP TABLE IF EXISTS `tb_class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_class` (
  `classID` int NOT NULL,
  `gradeID` int NOT NULL,
  `className` varchar(20) NOT NULL,
  PRIMARY KEY (`classID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_class`
--

LOCK TABLES `tb_class` WRITE;
/*!40000 ALTER TABLE `tb_class` DISABLE KEYS */;
INSERT INTO `tb_class` VALUES (1,10001,'撒旦撒'),(3,20001,'二班'),(4,20001,'三班'),(11,20002,'一班'),(12,20002,'二班'),(111,20003,'一班'),(112,20003,'二班'),(113,20003,'三班'),(114,20003,'四班'),(1001,2021001,'一班'),(1002,2021001,'二班'),(1003,2021001,'三班'),(2001,2021002,'一班'),(2002,2021002,'二班'),(3001,2021003,'一班'),(3002,2021003,'二班'),(1000000001,10001,'2656');
/*!40000 ALTER TABLE `tb_class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_examkinds`
--

DROP TABLE IF EXISTS `tb_examkinds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_examkinds` (
  `kindID` int NOT NULL,
  `kindName` varchar(40) NOT NULL,
  PRIMARY KEY (`kindID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_examkinds`
--

LOCK TABLES `tb_examkinds` WRITE;
/*!40000 ALTER TABLE `tb_examkinds` DISABLE KEYS */;
INSERT INTO `tb_examkinds` VALUES (1,'期中考试'),(2,'期末考试');
/*!40000 ALTER TABLE `tb_examkinds` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_grade`
--

DROP TABLE IF EXISTS `tb_grade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_grade` (
  `gradeID` int NOT NULL,
  `gradeName` varchar(20) NOT NULL,
  PRIMARY KEY (`gradeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_grade`
--

LOCK TABLES `tb_grade` WRITE;
/*!40000 ALTER TABLE `tb_grade` DISABLE KEYS */;
INSERT INTO `tb_grade` VALUES (20001,'高中一年级'),(20002,'高中二年级'),(20003,'高中三年级');
/*!40000 ALTER TABLE `tb_grade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_result`
--

DROP TABLE IF EXISTS `tb_result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_result` (
  `id` int NOT NULL AUTO_INCREMENT,
  `stuID` varchar(20) NOT NULL,
  `kindID` int NOT NULL,
  `subID` int NOT NULL,
  `result` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_result`
--

LOCK TABLES `tb_result` WRITE;
/*!40000 ALTER TABLE `tb_result` DISABLE KEYS */;
INSERT INTO `tb_result` VALUES (20,'00001',1,1,100),(21,'00003',1,1,99),(22,'00006',1,1,100),(23,'00006',1,2,80),(24,'00002',1,1,89),(25,'00002',1,2,65),(26,'00002',1,3,30),(27,'00005',1,1,110),(28,'00005',1,2,80),(29,'00005',1,3,50),(30,'00005',2,1,88),(31,'00005',2,3,65),(32,'00005',2,2,66),(33,'00002',2,1,90),(34,'00002',2,2,88),(35,'00002',2,3,40),(36,'00001',2,1,100),(37,'00001',2,2,90),(38,'00001',2,3,97),(39,'00003',2,1,120),(40,'00003',2,2,80),(41,'00003',2,3,65),(42,'00006',2,1,66),(43,'00006',2,2,98),(44,'00006',2,3,40);
/*!40000 ALTER TABLE `tb_result` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_student`
--

DROP TABLE IF EXISTS `tb_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_student` (
  `stuID` varchar(20) NOT NULL,
  `stuName` varchar(20) NOT NULL,
  `classID` int NOT NULL,
  `gradeID` int NOT NULL,
  `age` int NOT NULL,
  `sex` char(4) NOT NULL,
  `phone` char(20) DEFAULT NULL,
  `address` varchar(100) NOT NULL,
  PRIMARY KEY (`stuID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_student`
--

LOCK TABLES `tb_student` WRITE;
/*!40000 ALTER TABLE `tb_student` DISABLE KEYS */;
INSERT INTO `tb_student` VALUES ('00001','张三',3,20001,12,'男','3123123123','12312312312'),('00002','李四',11,20002,12,'男','32131231','1231231231'),('00003','弄弄',3,20001,13,'女','132165131','465131651633'),('00005','啊三',111,20003,14,'女','2312312','12312312312313'),('00006','算法',4,20001,165,'女','1331651','161561616351'),('10001','张三',1001,2021001,15,'男','15987796548','云南省玉溪市红塔区'),('10002','李四',1001,2021001,16,'女','13145678921','云南省玉溪市通海县'),('20001','王麻子',2001,2021002,17,'男','186877688994','农讲所卡的技法卢卡斯大家');
/*!40000 ALTER TABLE `tb_student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_subject`
--

DROP TABLE IF EXISTS `tb_subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_subject` (
  `subID` int NOT NULL,
  `subName` varchar(50) NOT NULL,
  PRIMARY KEY (`subID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_subject`
--

LOCK TABLES `tb_subject` WRITE;
/*!40000 ALTER TABLE `tb_subject` DISABLE KEYS */;
INSERT INTO `tb_subject` VALUES (1,'语文'),(2,'英语'),(3,'数学'),(4,'政治'),(5,'历史'),(6,'化学'),(7,'物理');
/*!40000 ALTER TABLE `tb_subject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_user`
--

DROP TABLE IF EXISTS `tb_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_user` (
  `userName` varchar(20) NOT NULL,
  `userPwd` varchar(50) NOT NULL,
  PRIMARY KEY (`userName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_user`
--

LOCK TABLES `tb_user` WRITE;
/*!40000 ALTER TABLE `tb_user` DISABLE KEYS */;
INSERT INTO `tb_user` VALUES ('root','1234');
/*!40000 ALTER TABLE `tb_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `v_classinfo`
--

DROP TABLE IF EXISTS `v_classinfo`;
/*!50001 DROP VIEW IF EXISTS `v_classinfo`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `v_classinfo` AS SELECT 
 1 AS `classID`,
 1 AS `gradeID`,
 1 AS `gradeName`,
 1 AS `className`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_resultinfo`
--

DROP TABLE IF EXISTS `v_resultinfo`;
/*!50001 DROP VIEW IF EXISTS `v_resultinfo`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `v_resultinfo` AS SELECT 
 1 AS `ID`,
 1 AS `stuID`,
 1 AS `stuName`,
 1 AS `kindName`,
 1 AS `subName`,
 1 AS `className`,
 1 AS `gradeName`,
 1 AS `result`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_studentinfo`
--

DROP TABLE IF EXISTS `v_studentinfo`;
/*!50001 DROP VIEW IF EXISTS `v_studentinfo`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `v_studentinfo` AS SELECT 
 1 AS `stuID`,
 1 AS `stuName`,
 1 AS `age`,
 1 AS `sex`,
 1 AS `phone`,
 1 AS `address`,
 1 AS `className`,
 1 AS `gradeName`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `v_classinfo`
--

/*!50001 DROP VIEW IF EXISTS `v_classinfo`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = gbk */;
/*!50001 SET character_set_results     = gbk */;
/*!50001 SET collation_connection      = gbk_chinese_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_classinfo` AS select `tb_class`.`classID` AS `classID`,`tb_grade`.`gradeID` AS `gradeID`,`tb_grade`.`gradeName` AS `gradeName`,`tb_class`.`className` AS `className` from (`tb_class` join `tb_grade`) where (`tb_class`.`gradeID` = `tb_grade`.`gradeID`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_resultinfo`
--

/*!50001 DROP VIEW IF EXISTS `v_resultinfo`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = gbk */;
/*!50001 SET character_set_results     = gbk */;
/*!50001 SET collation_connection      = gbk_chinese_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_resultinfo` AS select `tb_result`.`id` AS `ID`,`tb_result`.`stuID` AS `stuID`,`v_studentinfo`.`stuName` AS `stuName`,`tb_examkinds`.`kindName` AS `kindName`,`tb_subject`.`subName` AS `subName`,`v_studentinfo`.`className` AS `className`,`v_studentinfo`.`gradeName` AS `gradeName`,`tb_result`.`result` AS `result` from (((`tb_subject` join `tb_result`) join `tb_examkinds`) join `v_studentinfo`) where ((`tb_result`.`stuID` = `v_studentinfo`.`stuID`) and (`tb_result`.`kindID` = `tb_examkinds`.`kindID`) and (`tb_result`.`subID` = `tb_subject`.`subID`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_studentinfo`
--

/*!50001 DROP VIEW IF EXISTS `v_studentinfo`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = gbk */;
/*!50001 SET character_set_results     = gbk */;
/*!50001 SET collation_connection      = gbk_chinese_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_studentinfo` AS select `tb_student`.`stuID` AS `stuID`,`tb_student`.`stuName` AS `stuName`,`tb_student`.`age` AS `age`,`tb_student`.`sex` AS `sex`,`tb_student`.`phone` AS `phone`,`tb_student`.`address` AS `address`,`tb_class`.`className` AS `className`,`tb_grade`.`gradeName` AS `gradeName` from ((`tb_student` join `tb_class`) join `tb_grade`) where ((`tb_student`.`classID` = `tb_class`.`classID`) and (`tb_student`.`gradeID` = `tb_grade`.`gradeID`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-08-26 18:22:54
