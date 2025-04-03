/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-11.7.2-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: placeme
-- ------------------------------------------------------
-- Server version	11.7.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES
(1,'Can add permission',1,'add_permission'),
(2,'Can change permission',1,'change_permission'),
(3,'Can delete permission',1,'delete_permission'),
(4,'Can view permission',1,'view_permission'),
(5,'Can add group',2,'add_group'),
(6,'Can change group',2,'change_group'),
(7,'Can delete group',2,'delete_group'),
(8,'Can view group',2,'view_group'),
(9,'Can add content type',3,'add_contenttype'),
(10,'Can change content type',3,'change_contenttype'),
(11,'Can delete content type',3,'delete_contenttype'),
(12,'Can view content type',3,'view_contenttype'),
(13,'Can add auth group',4,'add_authgroup'),
(14,'Can change auth group',4,'change_authgroup'),
(15,'Can delete auth group',4,'delete_authgroup'),
(16,'Can view auth group',4,'view_authgroup'),
(17,'Can add auth group permissions',5,'add_authgrouppermissions'),
(18,'Can change auth group permissions',5,'change_authgrouppermissions'),
(19,'Can delete auth group permissions',5,'delete_authgrouppermissions'),
(20,'Can view auth group permissions',5,'view_authgrouppermissions'),
(21,'Can add auth permission',6,'add_authpermission'),
(22,'Can change auth permission',6,'change_authpermission'),
(23,'Can delete auth permission',6,'delete_authpermission'),
(24,'Can view auth permission',6,'view_authpermission'),
(25,'Can add auth user',7,'add_authuser'),
(26,'Can change auth user',7,'change_authuser'),
(27,'Can delete auth user',7,'delete_authuser'),
(28,'Can view auth user',7,'view_authuser'),
(29,'Can add auth user groups',8,'add_authusergroups'),
(30,'Can change auth user groups',8,'change_authusergroups'),
(31,'Can delete auth user groups',8,'delete_authusergroups'),
(32,'Can view auth user groups',8,'view_authusergroups'),
(33,'Can add auth user user permissions',9,'add_authuseruserpermissions'),
(34,'Can change auth user user permissions',9,'change_authuseruserpermissions'),
(35,'Can delete auth user user permissions',9,'delete_authuseruserpermissions'),
(36,'Can view auth user user permissions',9,'view_authuseruserpermissions'),
(37,'Can add django admin log',10,'add_djangoadminlog'),
(38,'Can change django admin log',10,'change_djangoadminlog'),
(39,'Can delete django admin log',10,'delete_djangoadminlog'),
(40,'Can view django admin log',10,'view_djangoadminlog'),
(41,'Can add django content type',11,'add_djangocontenttype'),
(42,'Can change django content type',11,'change_djangocontenttype'),
(43,'Can delete django content type',11,'delete_djangocontenttype'),
(44,'Can view django content type',11,'view_djangocontenttype'),
(45,'Can add django migrations',12,'add_djangomigrations'),
(46,'Can change django migrations',12,'change_djangomigrations'),
(47,'Can delete django migrations',12,'delete_djangomigrations'),
(48,'Can view django migrations',12,'view_djangomigrations'),
(49,'Can add django session',13,'add_djangosession'),
(50,'Can change django session',13,'change_djangosession'),
(51,'Can delete django session',13,'delete_djangosession'),
(52,'Can view django session',13,'view_djangosession'),
(53,'Can add user',14,'add_user'),
(54,'Can change user',14,'change_user'),
(55,'Can delete user',14,'delete_user'),
(56,'Can view user',14,'view_user'),
(57,'Can add placement officer',15,'add_placementofficer'),
(58,'Can change placement officer',15,'change_placementofficer'),
(59,'Can delete placement officer',15,'delete_placementofficer'),
(60,'Can view placement officer',15,'view_placementofficer'),
(61,'Can add placement offer',16,'add_placementoffer'),
(62,'Can change placement offer',16,'change_placementoffer'),
(63,'Can delete placement offer',16,'delete_placementoffer'),
(64,'Can view placement offer',16,'view_placementoffer'),
(65,'Can add student',17,'add_student'),
(66,'Can change student',17,'change_student'),
(67,'Can delete student',17,'delete_student'),
(68,'Can view student',17,'view_student'),
(69,'Can add application',18,'add_application'),
(70,'Can change application',18,'change_application'),
(71,'Can delete application',18,'delete_application'),
(72,'Can view application',18,'view_application'),
(73,'Can add tutor',19,'add_tutor'),
(74,'Can change tutor',19,'change_tutor'),
(75,'Can delete tutor',19,'delete_tutor'),
(76,'Can view tutor',19,'view_tutor'),
(77,'Can add marks',20,'add_marks'),
(78,'Can change marks',20,'change_marks'),
(79,'Can delete marks',20,'delete_marks'),
(80,'Can view marks',20,'view_marks'),
(81,'Can add department',21,'add_department'),
(82,'Can change department',21,'change_department'),
(83,'Can delete department',21,'delete_department'),
(84,'Can view department',21,'view_department'),
(85,'Can add log entry',22,'add_logentry'),
(86,'Can change log entry',22,'change_logentry'),
(87,'Can delete log entry',22,'delete_logentry'),
(88,'Can view log entry',22,'view_logentry'),
(89,'Can add session',23,'add_session'),
(90,'Can change session',23,'change_session'),
(91,'Can delete session',23,'delete_session'),
(92,'Can view session',23,'view_session'),
(93,'Can add tutor approval',24,'add_tutorapproval'),
(94,'Can change tutor approval',24,'change_tutorapproval'),
(95,'Can delete tutor approval',24,'delete_tutorapproval'),
(96,'Can view tutor approval',24,'view_tutorapproval'),
(97,'Can add notification',25,'add_notification'),
(98,'Can change notification',25,'change_notification'),
(99,'Can delete notification',25,'delete_notification'),
(100,'Can view notification',25,'view_notification');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_main_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_main_user_id` FOREIGN KEY (`user_id`) REFERENCES `main_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES
(1,'2025-03-24 12:48:05.684527','1','Computer Science',1,'[{\"added\": {}}]',21,1),
(2,'2025-03-24 12:57:10.547941','2','Electrical & Communication',1,'[{\"added\": {}}]',21,1),
(3,'2025-03-24 13:06:58.154169','1','Arun',1,'[{\"added\": {}}]',19,1),
(4,'2025-03-24 15:31:26.897372','5','placement@gmail.com (a6a8a1dbc5cf6fda2bb5)',1,'[{\"added\": {}}]',14,1),
(5,'2025-03-24 15:31:48.644625','1','Placement Officer: Placement officer',1,'[{\"added\": {}}]',15,1),
(6,'2025-03-24 16:08:04.976025','4','arun@gmail.com (Kgr21cs0181674673192)',2,'[{\"changed\": {\"fields\": [\"Role\"]}}]',14,1),
(7,'2025-03-25 07:09:51.462236','kgr21cs2131234567893','kgr21cs2131234567893',2,'[{\"changed\": {\"fields\": [\"Tutor\"]}}]',17,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES
(22,'admin','logentry'),
(2,'auth','group'),
(1,'auth','permission'),
(3,'contenttypes','contenttype'),
(18,'main','application'),
(4,'main','authgroup'),
(5,'main','authgrouppermissions'),
(6,'main','authpermission'),
(7,'main','authuser'),
(8,'main','authusergroups'),
(9,'main','authuseruserpermissions'),
(21,'main','department'),
(10,'main','djangoadminlog'),
(11,'main','djangocontenttype'),
(12,'main','djangomigrations'),
(13,'main','djangosession'),
(20,'main','marks'),
(25,'main','notification'),
(16,'main','placementoffer'),
(15,'main','placementofficer'),
(17,'main','student'),
(19,'main','tutor'),
(24,'main','tutorapproval'),
(14,'main','user'),
(23,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES
(1,'contenttypes','0001_initial','2025-03-24 12:44:11.837364'),
(2,'contenttypes','0002_remove_content_type_name','2025-03-24 12:44:11.968218'),
(3,'auth','0001_initial','2025-03-24 12:44:12.450752'),
(4,'auth','0002_alter_permission_name_max_length','2025-03-24 12:44:12.548934'),
(5,'auth','0003_alter_user_email_max_length','2025-03-24 12:44:12.569421'),
(6,'auth','0004_alter_user_username_opts','2025-03-24 12:44:12.588628'),
(7,'auth','0005_alter_user_last_login_null','2025-03-24 12:44:12.599342'),
(8,'auth','0006_require_contenttypes_0002','2025-03-24 12:44:12.602533'),
(9,'auth','0007_alter_validators_add_error_messages','2025-03-24 12:44:12.610431'),
(10,'auth','0008_alter_user_username_max_length','2025-03-24 12:44:12.619183'),
(11,'auth','0009_alter_user_last_name_max_length','2025-03-24 12:44:12.627478'),
(12,'auth','0010_alter_group_name_max_length','2025-03-24 12:44:12.667225'),
(13,'auth','0011_update_proxy_permissions','2025-03-24 12:44:12.681150'),
(14,'auth','0012_alter_user_first_name_max_length','2025-03-24 12:44:12.689813'),
(15,'main','0001_initial','2025-03-24 12:44:14.873246'),
(16,'main','0002_department_placementoffer_sem','2025-03-24 12:44:15.037643'),
(17,'main','0003_alter_student_department','2025-03-24 12:44:15.375691'),
(18,'admin','0001_initial','2025-03-24 12:46:07.853689'),
(19,'admin','0002_logentry_remove_auto_add','2025-03-24 12:46:07.894161'),
(20,'admin','0003_logentry_add_action_flag_choices','2025-03-24 12:46:07.931057'),
(21,'sessions','0001_initial','2025-03-24 12:46:08.016421'),
(22,'main','0004_alter_tutor_department','2025-03-24 13:06:32.299842'),
(23,'main','0005_placementoffer_department','2025-03-24 13:11:20.537934'),
(24,'main','0006_notification_tutorapproval','2025-03-25 06:24:24.841348');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES
('b9tmu33lmwm95b5b531vdfygr3pom9gt','.eJxVjDsOwjAQBe_iGln-xD9Kes5grXdtHEC2FCcV4u4QKQW0b2bei0XY1hq3kZc4EzszyU6_WwJ85LYDukO7dY69rcuc-K7wgw5-7ZSfl8P9O6gw6rdWRnoEb4TV2Zk8ueDRismGoCmBKFKBMIZQZO0EFFA-Be8JdUBLxSX2_gDDDDeu:1twhLF:HZ0QfpOgG2vjPrz4aCC3KAidUwhJm3AlKtPggwgglCs','2025-04-07 12:55:45.647152'),
('cu5c0w70awqxe30vgiwgbji8016x2lms','.eJxVjDsOwjAQBe_iGlmbNf5ASc8ZrPWujQPIkeKkQtwdIqWA9s3Me6lI61Lj2vMcR1FnherwuyXiR24bkDu126R5ass8Jr0peqddXyfJz8vu_h1U6vVbey-ZkwiaIyQL5Ayw9WKKCyWjZQ-ZPQYE8YEZAhsgNMxmKOhOdlDvD_AMN8E:1twhIm:jpaRFTnFd7Uv1xS1-B51UFMDF8587ym7rqvmSmJTabk','2025-04-07 12:53:12.114748'),
('mf4awno6hj2f0dje19g8ulxllswtifpv','.eJxVjDsOwjAQBe_iGln-fyjpOYNl765xADlSnFSIu0OkFNC-mXkvlvK2trQNWtKE7MwMO_1uJcOD-g7wnvtt5jD3dZkK3xV-0MGvM9Lzcrh_By2P9q09-hjQmRpsNUqCB8yEpC1FEMprr0xVUoqYAYicLtUQCABpQ3VeE3t_APMXOHM:1twyRU:-6znb9Kf5ltjYWnHwPKGD7zb5DAA0VE8dOZ4fBzjBrU','2025-04-08 07:11:20.505500'),
('sq4e2w4lek5q8aua89su4g7k6h1co0bp','.eJxVjDsOwjAQBe_iGln-fyjpOYNl765xADlSnFSIu0OkFNC-mXkvlvK2trQNWtKE7MwMO_1uJcOD-g7wnvtt5jD3dZkK3xV-0MGvM9Lzcrh_By2P9q09-hjQmRpsNUqCB8yEpC1FEMprr0xVUoqYAYicLtUQCABpQ3VeE3t_APMXOHM:1twhRU:n8HSnaeIaadhPPEpN1Vw_HgR5hbDj3C0eklrrE1ZVpo','2025-04-07 13:02:12.268194');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_application`
--

DROP TABLE IF EXISTS `main_application`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `main_application` (
  `appli_id` int(11) NOT NULL AUTO_INCREMENT,
  `status` varchar(50) NOT NULL,
  `applied_date` date NOT NULL,
  `offer_id_id` int(11) NOT NULL,
  `reg_no_id` varchar(20) NOT NULL,
  PRIMARY KEY (`appli_id`),
  KEY `main_application_offer_id_id_ccd3a0d2_fk_main_plac` (`offer_id_id`),
  KEY `main_application_reg_no_id_0a49ae31_fk_main_student_reg_no` (`reg_no_id`),
  CONSTRAINT `main_application_offer_id_id_ccd3a0d2_fk_main_plac` FOREIGN KEY (`offer_id_id`) REFERENCES `main_placementoffer` (`offer_id`),
  CONSTRAINT `main_application_reg_no_id_0a49ae31_fk_main_student_reg_no` FOREIGN KEY (`reg_no_id`) REFERENCES `main_student` (`reg_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_application`
--

LOCK TABLES `main_application` WRITE;
/*!40000 ALTER TABLE `main_application` DISABLE KEYS */;
/*!40000 ALTER TABLE `main_application` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_department`
--

DROP TABLE IF EXISTS `main_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `main_department` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `code` varchar(10) NOT NULL,
  `head` varchar(100) DEFAULT NULL,
  `contact_email` varchar(254) DEFAULT NULL,
  `description` longtext DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_department`
--

LOCK TABLES `main_department` WRITE;
/*!40000 ALTER TABLE `main_department` DISABLE KEYS */;
INSERT INTO `main_department` VALUES
(1,'Computer Science','CS','hod 1','hod1@gmail.com','Compputer Science and technology'),
(2,'Electrical & Communication','EC','Hod2','hod2@gmail.com','Electrical and Communication engineering');
/*!40000 ALTER TABLE `main_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_marks`
--

DROP TABLE IF EXISTS `main_marks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `main_marks` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cgpa` decimal(4,2) NOT NULL,
  `backlog` int(10) unsigned NOT NULL CHECK (`backlog` >= 0),
  `sem` int(10) unsigned NOT NULL CHECK (`sem` >= 0),
  `reg_no_id` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `main_marks_reg_no_id_sem_9a4a4703_uniq` (`reg_no_id`,`sem`),
  CONSTRAINT `main_marks_reg_no_id_2091b0c0_fk_main_student_reg_no` FOREIGN KEY (`reg_no_id`) REFERENCES `main_student` (`reg_no`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_marks`
--

LOCK TABLES `main_marks` WRITE;
/*!40000 ALTER TABLE `main_marks` DISABLE KEYS */;
INSERT INTO `main_marks` VALUES
(1,9.10,2,6,'kgr21cs2131234567891');
/*!40000 ALTER TABLE `main_marks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_notification`
--

DROP TABLE IF EXISTS `main_notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `main_notification` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `status` tinyint(1) NOT NULL,
  `date` date NOT NULL,
  `receiver_id` bigint(20) NOT NULL,
  `sender_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_notification_receiver_id_ceff4b36_fk_main_user_id` (`receiver_id`),
  KEY `main_notification_sender_id_8c7004b2_fk_main_user_id` (`sender_id`),
  CONSTRAINT `main_notification_receiver_id_ceff4b36_fk_main_user_id` FOREIGN KEY (`receiver_id`) REFERENCES `main_user` (`id`),
  CONSTRAINT `main_notification_sender_id_8c7004b2_fk_main_user_id` FOREIGN KEY (`sender_id`) REFERENCES `main_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_notification`
--

LOCK TABLES `main_notification` WRITE;
/*!40000 ALTER TABLE `main_notification` DISABLE KEYS */;
INSERT INTO `main_notification` VALUES
(1,'New Student registeration ',0,'2025-03-25',4,6),
(2,'New Student registeration ',0,'2025-03-25',4,7);
/*!40000 ALTER TABLE `main_notification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_placementoffer`
--

DROP TABLE IF EXISTS `main_placementoffer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `main_placementoffer` (
  `offer_id` int(11) NOT NULL AUTO_INCREMENT,
  `company_name` varchar(255) NOT NULL,
  `cgpa_required` decimal(4,2) NOT NULL,
  `no_of_backpapers` int(10) unsigned NOT NULL CHECK (`no_of_backpapers` >= 0),
  `salary` decimal(12,2) NOT NULL,
  `description` longtext DEFAULT NULL,
  `skillset` longtext DEFAULT NULL,
  `contact_email` varchar(254) NOT NULL,
  `posted_date` date NOT NULL,
  `final_date` date NOT NULL,
  `created_by_id` bigint(20) NOT NULL,
  `sem` int(11) NOT NULL,
  `department_id` bigint(20) NOT NULL,
  PRIMARY KEY (`offer_id`),
  KEY `main_placementoffer_created_by_id_deb3bcef_fk_main_plac` (`created_by_id`),
  KEY `main_placementoffer_department_id_4a998632_fk_main_department_id` (`department_id`),
  CONSTRAINT `main_placementoffer_created_by_id_deb3bcef_fk_main_plac` FOREIGN KEY (`created_by_id`) REFERENCES `main_placementofficer` (`id`),
  CONSTRAINT `main_placementoffer_department_id_4a998632_fk_main_department_id` FOREIGN KEY (`department_id`) REFERENCES `main_department` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_placementoffer`
--

LOCK TABLES `main_placementoffer` WRITE;
/*!40000 ALTER TABLE `main_placementoffer` DISABLE KEYS */;
INSERT INTO `main_placementoffer` VALUES
(1,'Amazon',6.00,0,6000000.00,'frontend developer','react js , angular js','amazon@gmail.com','2025-03-24','2025-03-29',1,6,1),
(2,'Google',7.00,0,7000000.00,'backend developer','django,python','google@gmail.com','2025-03-24','2025-03-28',1,8,1);
/*!40000 ALTER TABLE `main_placementoffer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_placementoffer_applied_by`
--

DROP TABLE IF EXISTS `main_placementoffer_applied_by`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `main_placementoffer_applied_by` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `placementoffer_id` int(11) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `main_placementoffer_appl_placementoffer_id_user_i_5cc1d364_uniq` (`placementoffer_id`,`user_id`),
  KEY `main_placementoffer_applied_by_user_id_e33ac03f_fk_main_user_id` (`user_id`),
  CONSTRAINT `main_placementoffer__placementoffer_id_58554ef7_fk_main_plac` FOREIGN KEY (`placementoffer_id`) REFERENCES `main_placementoffer` (`offer_id`),
  CONSTRAINT `main_placementoffer_applied_by_user_id_e33ac03f_fk_main_user_id` FOREIGN KEY (`user_id`) REFERENCES `main_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_placementoffer_applied_by`
--

LOCK TABLES `main_placementoffer_applied_by` WRITE;
/*!40000 ALTER TABLE `main_placementoffer_applied_by` DISABLE KEYS */;
INSERT INTO `main_placementoffer_applied_by` VALUES
(13,1,3);
/*!40000 ALTER TABLE `main_placementoffer_applied_by` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_placementoffer_liked_by`
--

DROP TABLE IF EXISTS `main_placementoffer_liked_by`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `main_placementoffer_liked_by` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `placementoffer_id` int(11) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `main_placementoffer_like_placementoffer_id_user_i_8990e550_uniq` (`placementoffer_id`,`user_id`),
  KEY `main_placementoffer_liked_by_user_id_16743491_fk_main_user_id` (`user_id`),
  CONSTRAINT `main_placementoffer__placementoffer_id_2668cd9f_fk_main_plac` FOREIGN KEY (`placementoffer_id`) REFERENCES `main_placementoffer` (`offer_id`),
  CONSTRAINT `main_placementoffer_liked_by_user_id_16743491_fk_main_user_id` FOREIGN KEY (`user_id`) REFERENCES `main_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_placementoffer_liked_by`
--

LOCK TABLES `main_placementoffer_liked_by` WRITE;
/*!40000 ALTER TABLE `main_placementoffer_liked_by` DISABLE KEYS */;
/*!40000 ALTER TABLE `main_placementoffer_liked_by` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_placementofficer`
--

DROP TABLE IF EXISTS `main_placementofficer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `main_placementofficer` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `main_placementofficer_user_id_1065fe69_fk_main_user_id` FOREIGN KEY (`user_id`) REFERENCES `main_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_placementofficer`
--

LOCK TABLES `main_placementofficer` WRITE;
/*!40000 ALTER TABLE `main_placementofficer` DISABLE KEYS */;
INSERT INTO `main_placementofficer` VALUES
(1,5);
/*!40000 ALTER TABLE `main_placementofficer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_student`
--

DROP TABLE IF EXISTS `main_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `main_student` (
  `reg_no` varchar(20) NOT NULL,
  `department_id` bigint(20) NOT NULL,
  `semester` int(10) unsigned NOT NULL CHECK (`semester` >= 0),
  `date_of_birth` date DEFAULT NULL,
  `batch` varchar(20) NOT NULL,
  `division` varchar(20) DEFAULT NULL,
  `phone_no` varchar(20) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  `tutor_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`reg_no`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `main_student_tutor_id_194490d5_fk_main_tutor_tutor_id` (`tutor_id`),
  KEY `main_student_department_id_94f07529` (`department_id`),
  CONSTRAINT `main_student_department_id_94f07529_fk_main_department_id` FOREIGN KEY (`department_id`) REFERENCES `main_department` (`id`),
  CONSTRAINT `main_student_tutor_id_194490d5_fk_main_tutor_tutor_id` FOREIGN KEY (`tutor_id`) REFERENCES `main_tutor` (`tutor_id`),
  CONSTRAINT `main_student_user_id_32abd1a3_fk_main_user_id` FOREIGN KEY (`user_id`) REFERENCES `main_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_student`
--

LOCK TABLES `main_student` WRITE;
/*!40000 ALTER TABLE `main_student` DISABLE KEYS */;
INSERT INTO `main_student` VALUES
('kgr21cs2131234567890',1,6,'2003-03-12','2020','A','9078563412',2,NULL),
('kgr21cs2131234567891',1,6,'2003-03-12','2020','B','9078563412',3,1),
('kgr21cs2131234567893',1,6,'2002-12-31','2020','A','8967452310',6,1),
('kgr21cs2131234567894',1,6,'2000-12-20','2020','A','9067452389',7,1);
/*!40000 ALTER TABLE `main_student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_tutor`
--

DROP TABLE IF EXISTS `main_tutor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `main_tutor` (
  `tutor_id` int(11) NOT NULL AUTO_INCREMENT,
  `tutor_name` varchar(255) NOT NULL,
  `department_id` bigint(20) NOT NULL,
  `semester` int(10) unsigned NOT NULL CHECK (`semester` >= 0),
  `division` varchar(50) NOT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`tutor_id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `main_tutor_department_id_268a4744` (`department_id`),
  CONSTRAINT `main_tutor_department_id_268a4744_fk_main_department_id` FOREIGN KEY (`department_id`) REFERENCES `main_department` (`id`),
  CONSTRAINT `main_tutor_user_id_7485c0d5_fk_main_user_id` FOREIGN KEY (`user_id`) REFERENCES `main_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_tutor`
--

LOCK TABLES `main_tutor` WRITE;
/*!40000 ALTER TABLE `main_tutor` DISABLE KEYS */;
INSERT INTO `main_tutor` VALUES
(1,'Arun',1,6,'A',4);
/*!40000 ALTER TABLE `main_tutor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_tutorapproval`
--

DROP TABLE IF EXISTS `main_tutorapproval`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `main_tutorapproval` (
  `confirm` tinyint(1) NOT NULL,
  `nid_id` bigint(20) NOT NULL,
  `tid` bigint(20) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`tid`),
  KEY `main_tutorapproval_nid_id_3cf5850c_fk_main_notification_id` (`nid_id`),
  CONSTRAINT `main_tutorapproval_nid_id_3cf5850c_fk_main_notification_id` FOREIGN KEY (`nid_id`) REFERENCES `main_notification` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_tutorapproval`
--

LOCK TABLES `main_tutorapproval` WRITE;
/*!40000 ALTER TABLE `main_tutorapproval` DISABLE KEYS */;
INSERT INTO `main_tutorapproval` VALUES
(1,1,1),
(1,2,2);
/*!40000 ALTER TABLE `main_tutorapproval` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_user`
--

DROP TABLE IF EXISTS `main_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `main_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `regno` varchar(20) DEFAULT NULL,
  `role` varchar(20) NOT NULL,
  `username` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `regno` (`regno`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_user`
--

LOCK TABLES `main_user` WRITE;
/*!40000 ALTER TABLE `main_user` DISABLE KEYS */;
INSERT INTO `main_user` VALUES
(1,'pbkdf2_sha256$870000$MxDPL4XhJBTMJczSq8N5kJ$M6Na0u1rYgAuUywEnpswo2OX8d1jQofZLqr3MY/rQN4=','2025-03-24 12:55:45.642482',1,'','','admin@gmail.com',1,1,'2025-03-24 12:47:06.971292','e16eb74c27ebde53554a','student','admin'),
(2,'pbkdf2_sha256$870000$qBr9D1e0Hi2U5YzXyK6K7O$jQzUudTvZ2RKaVmWFUWyNAYi2HzsEqlgitBPOFrl7dw=','2025-03-25 05:46:53.719360',0,'amal','john','amal@gmail.com',0,1,'2025-03-24 12:53:11.104031','kgr21cs2131234567890','student','amal@gmail.com'),
(3,'pbkdf2_sha256$870000$NbrEIbwQH5fnk8q4lsmV6d$zFoudPWsdzGaRr28xF0EHo4qHNcr4i9BazD6btpjD+4=','2025-03-25 05:47:15.633622',0,'john','doe','john@gmail.com',0,1,'2025-03-24 12:58:52.250422','kgr21cs2131234567891','student','john@gmail.com'),
(4,'pbkdf2_sha256$870000$hNZA6DoLWCAyb9CXujk8ES$+wUEFyjBpBytQLw7anWpCD4dTZGtKk3cmz6sHROgSEg=','2025-03-25 07:11:20.501228',0,'Arun','A','arun@gmail.com',0,1,'2025-03-24 13:02:11.000000','Kgr21cs0181674673192','tutor','arun@gmail.com'),
(5,'placement@pass','2025-03-25 05:47:38.975246',0,'Placement','Officer 1','placement@gmail.com',0,1,'2025-03-24 15:29:56.000000','a6a8a1dbc5cf6fda2bb5','placement_officer','Placement officer'),
(6,'pbkdf2_sha256$870000$IUNbTnUFSDmWY31wbpLpPg$fNeJOktHodSec1QhTXx64wcMGuieXIDg7G4hZ0dByvE=','2025-03-25 06:37:01.126039',0,'varun','v','varun@gmail.com',0,1,'2025-03-25 06:36:59.944405','kgr21cs2131234567893','student','varun@gmail.com'),
(7,'pbkdf2_sha256$870000$32AwWmyzAUbPHFnGFk04VY$SGxikyAKT7kmXohv1buVPKWx661OIsSt9FUEFLnslao=','2025-03-25 07:10:35.986425',0,'albin','a','ablin@gmail.com',0,1,'2025-03-25 07:10:34.820466','kgr21cs2131234567894','student','ablin@gmail.com');
/*!40000 ALTER TABLE `main_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_user_groups`
--

DROP TABLE IF EXISTS `main_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `main_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `main_user_groups_user_id_group_id_ae195797_uniq` (`user_id`,`group_id`),
  KEY `main_user_groups_group_id_a337ba62_fk_auth_group_id` (`group_id`),
  CONSTRAINT `main_user_groups_group_id_a337ba62_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `main_user_groups_user_id_df502602_fk_main_user_id` FOREIGN KEY (`user_id`) REFERENCES `main_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_user_groups`
--

LOCK TABLES `main_user_groups` WRITE;
/*!40000 ALTER TABLE `main_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `main_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_user_user_permissions`
--

DROP TABLE IF EXISTS `main_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `main_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `main_user_user_permissions_user_id_permission_id_96b9fadf_uniq` (`user_id`,`permission_id`),
  KEY `main_user_user_permi_permission_id_cd2b56a3_fk_auth_perm` (`permission_id`),
  CONSTRAINT `main_user_user_permi_permission_id_cd2b56a3_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `main_user_user_permissions_user_id_451ce57f_fk_main_user_id` FOREIGN KEY (`user_id`) REFERENCES `main_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_user_user_permissions`
--

LOCK TABLES `main_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `main_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `main_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2025-03-25 12:43:06
