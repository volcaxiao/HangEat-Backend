-- MySQL dump 10.13  Distrib 8.2.0, for macos14.0 (arm64)
--
-- Host: localhost    Database: HangEat
-- ------------------------------------------------------
-- Server version	8.2.0

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
-- Current Database: `HangEat`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `HangEat` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `HangEat`;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add address',6,'add_address'),(22,'Can change address',6,'change_address'),(23,'Can delete address',6,'delete_address'),(24,'Can view address',6,'view_address'),(25,'Can add comment',7,'add_comment'),(26,'Can change comment',7,'change_comment'),(27,'Can delete comment',7,'delete_comment'),(28,'Can view comment',7,'view_comment'),(29,'Can add dish',8,'add_dish'),(30,'Can change dish',8,'change_dish'),(31,'Can delete dish',8,'delete_dish'),(32,'Can view dish',8,'view_dish'),(33,'Can add post',9,'add_post'),(34,'Can change post',9,'change_post'),(35,'Can delete post',9,'delete_post'),(36,'Can view post',9,'view_post'),(37,'Can add recommend dish',10,'add_recommenddish'),(38,'Can change recommend dish',10,'change_recommenddish'),(39,'Can delete recommend dish',10,'delete_recommenddish'),(40,'Can view recommend dish',10,'view_recommenddish'),(41,'Can add restaurant',11,'add_restaurant'),(42,'Can change restaurant',11,'change_restaurant'),(43,'Can delete restaurant',11,'delete_restaurant'),(44,'Can view restaurant',11,'view_restaurant'),(45,'Can add restaurant tag',12,'add_restauranttag'),(46,'Can change restaurant tag',12,'change_restauranttag'),(47,'Can delete restaurant tag',12,'delete_restauranttag'),(48,'Can view restaurant tag',12,'view_restauranttag'),(49,'Can add tag',13,'add_tag'),(50,'Can change tag',13,'change_tag'),(51,'Can delete tag',13,'delete_tag'),(52,'Can view tag',13,'view_tag'),(53,'Can add 用户',14,'add_user'),(54,'Can change 用户',14,'change_user'),(55,'Can delete 用户',14,'delete_user'),(56,'Can view 用户',14,'view_user'),(57,'Can add subscribe',15,'add_subscribe'),(58,'Can change subscribe',15,'change_subscribe'),(59,'Can delete subscribe',15,'delete_subscribe'),(60,'Can view subscribe',15,'view_subscribe'),(61,'Can add message',16,'add_message'),(62,'Can change message',16,'change_message'),(63,'Can delete message',16,'delete_message'),(64,'Can view message',16,'view_message'),(65,'Can add collection',17,'add_collection'),(66,'Can change collection',17,'change_collection'),(67,'Can delete collection',17,'delete_collection'),(68,'Can view collection',17,'view_collection');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_users_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-12-24 09:49:50.388788','17','破学校',2,'[{\"changed\": {\"fields\": [\"Grade\", \"Avg price\", \"Agrees\"]}}]',9,16);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(6,'restaurant','address'),(7,'restaurant','comment'),(8,'restaurant','dish'),(9,'restaurant','post'),(10,'restaurant','recommenddish'),(11,'restaurant','restaurant'),(12,'restaurant','restauranttag'),(13,'restaurant','tag'),(5,'sessions','session'),(18,'users','authrecord'),(17,'users','collection'),(16,'users','message'),(15,'users','subscribe'),(14,'users','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'restaurant','0001_initial','2023-12-11 06:17:48.313068'),(2,'contenttypes','0001_initial','2023-12-11 06:17:48.346530'),(3,'contenttypes','0002_remove_content_type_name','2023-12-11 06:17:48.370862'),(4,'auth','0001_initial','2023-12-11 06:17:48.461359'),(5,'auth','0002_alter_permission_name_max_length','2023-12-11 06:17:48.484761'),(6,'auth','0003_alter_user_email_max_length','2023-12-11 06:17:48.494679'),(7,'auth','0004_alter_user_username_opts','2023-12-11 06:17:48.500716'),(8,'auth','0005_alter_user_last_login_null','2023-12-11 06:17:48.505636'),(9,'auth','0006_require_contenttypes_0002','2023-12-11 06:17:48.507978'),(10,'auth','0007_alter_validators_add_error_messages','2023-12-11 06:17:48.516961'),(11,'auth','0008_alter_user_username_max_length','2023-12-11 06:17:48.522945'),(12,'auth','0009_alter_user_last_name_max_length','2023-12-11 06:17:48.528613'),(13,'auth','0010_alter_group_name_max_length','2023-12-11 06:17:48.545367'),(14,'auth','0011_update_proxy_permissions','2023-12-11 06:17:48.557962'),(15,'auth','0012_alter_user_first_name_max_length','2023-12-11 06:17:48.564798'),(16,'users','0001_initial','2023-12-11 06:17:48.933978'),(17,'admin','0001_initial','2023-12-11 06:17:48.996798'),(18,'admin','0002_logentry_remove_auto_add','2023-12-11 06:17:49.016002'),(19,'admin','0003_logentry_add_action_flag_choices','2023-12-11 06:17:49.026728'),(20,'restaurant','0002_initial','2023-12-11 06:17:49.561560'),(21,'sessions','0001_initial','2023-12-11 06:17:49.579311'),(22,'restaurant','0003_rename_creater_restaurant_creator_and_more','2023-12-19 06:29:31.044339'),(23,'users','0002_rename_fans_subscribe_subscriber_and_more','2023-12-19 07:33:38.748993'),(24,'users','0003_user_isdelete','2023-12-19 08:35:47.161620'),(25,'restaurant','0004_rename_comment_content_comment_content_and_more','2023-12-19 13:57:30.528730'),(26,'restaurant','0005_alter_post_creator_alter_post_image_and_more','2023-12-22 08:50:52.015822'),(27,'restaurant','0006_alter_post_image','2023-12-22 08:51:46.013919'),(28,'restaurant','0007_remove_post_agree_post_agrees','2023-12-22 09:30:50.162807'),(29,'restaurant','0008_remove_comment_agree_comment_agrees','2023-12-22 11:17:07.061084'),(30,'restaurant','0009_alter_restaurant_options_alter_post_content','2023-12-23 16:28:00.344106'),(31,'restaurant','0010_alter_post_avg_price_alter_restaurant_description','2023-12-24 09:48:08.608996'),(32,'restaurant','0011_alter_post_avg_price','2023-12-24 09:48:08.616520');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0b7z9w4k6arou84p3ng203jfllxna80b','.eJxVjEEOwiAURO_C2pCCUsCl-56BzOeDVA1NSrsy3t026UJ3k3lv5i0C1qWEtaU5jCyuQonTb0eIz1R3wA_U-yTjVJd5JLkr8qBNDhOn1-1w_w4KWtnWnfU2XajvnFfaMQxD4cwK0dq8xey1M71KnimxI6MNETJBM5EHQ3y-7ik5RA:1rGWpz:bYdz-y3L-G7WrtC3WuFvCOBzia2K9u59jRewvv__EcI','2024-01-05 04:08:39.124560'),('0t1ktbgsrhtmydwowivjziy1zh6m256w','.eJxVjMsOwiAQRf-FtSEwU6S4dN9vIDM8pGogKe3K-O_apAvd3nPOfQlP21r81tPi5yguAsXpd2MKj1R3EO9Ub02GVtdlZrkr8qBdTi2m5_Vw_w4K9fKtnTIDK8OQHFmikDNYm6MzpEwKeiCNeNbjAJERIpBLekS2aBQDKMri_QHmKDe1:1rD50l:XM6sIzKnD1NZRXi4wA3gUjGlL7MgEAcutMyzy0yBEgQ','2023-12-26 15:49:31.374173'),('1a8vfm9fza4tm1z6ugtll9oqcckkmcn9','.eJxVjEEOwiAURO_C2pCCUsCl-56BzOeDVA1NSrsy3t026UJ3k3lv5i0C1qWEtaU5jCyuQonTb0eIz1R3wA_U-yTjVJd5JLkr8qBNDhOn1-1w_w4KWtnWnfU2XajvnFfaMQxD4cwK0dq8xey1M71KnimxI6MNETJBM5EHQ3y-7ik5RA:1rCycL:KdsZfWp4jwDYLaPcmc9WFv7Wzy08jjYjSX6fiP3cj9s','2023-12-26 08:59:53.552912'),('1ob7m23alpbvgxn8kzzoui8nlvroys7e','.eJxVjDsOwjAQBe_iGll2_FtT0nMGa9cfHEC2FCcV4u4QKQW0b2beiwXc1hq2kZcwJ3Zmmp1-N8L4yG0H6Y7t1nnsbV1m4rvCDzr4taf8vBzu30HFUb81RVcEFQJyUUgHiLl4hb6UCbK22euoFKBBAZqMniRFKYyxBUBao4G9PwowN-A:1rD6My:pwUSoE_bu2H2779_cMYt7s25MguS1NA_-a26r1N5sjc','2023-12-26 17:16:32.240650'),('1w9lm2k88afoxxdg7csdyqblecotb2ub','.eJxVjMsOwiAQRf-FtSGdluHh0r3fQBgYpGogKe3K-O_apAvd3nPOfQkftrX4rfPi5yTOQonT70YhPrjuIN1DvTUZW12XmeSuyIN2eW2Jn5fD_TsooZdvbZTmMQWFYFJGQDZaUciWh8lmRHSTsZFGnrRCHMARpKyAKRNpg-DE-wPWATeG:1rD4GO:pvgGClKOnUxMk3RlPSagkX6YSnQv3iyXOQBoMtVfcDk','2023-12-26 15:01:36.615461'),('1y78krxp0ep599hwjcu1qtltq85bxdp3','.eJxVjMsOwiAQRf-FtSEwU6S4dN9vIDM8pGogKe3K-O_apAvd3nPOfQlP21r81tPi5yguAsXpd2MKj1R3EO9Ub02GVtdlZrkr8qBdTi2m5_Vw_w4K9fKtnTIDK8OQHFmikDNYm6MzpEwKeiCNeNbjAJERIpBLekS2aBQDKMri_QHmKDe1:1rD4lf:pBQLqZOb3gnK-7LVbzL3eWN9MjlnJ2ZvVyHHc88h8A8','2023-12-26 15:33:55.372386'),('1y78o411pywoymp6hhj2x34mpq0mxqa3','.eJxVjEEOwiAURO_C2pCCUsCl-56BzOeDVA1NSrsy3t026UJ3k3lv5i0C1qWEtaU5jCyuQonTb0eIz1R3wA_U-yTjVJd5JLkr8qBNDhOn1-1w_w4KWtnWnfU2XajvnFfaMQxD4cwK0dq8xey1M71KnimxI6MNETJBM5EHQ3y-7ik5RA:1rGsmz:gLb5i2G7znB_ai0lkxWaqYR5EYkAV3Mg994mOOP1CAQ','2024-01-06 03:35:01.729598'),('22sg9idkfee74ogr5muy4ho9pbblu2du','.eJxVjEEOwiAQRe_C2pDOFAu4dN8zkIEZpGpoUtqV8e7apAvd_vfef6lA21rC1mQJE6uLMur0u0VKD6k74DvV26zTXNdlinpX9EGbHmeW5_Vw_w4KtfKthSgKIjChg2gRBsfnmB2L4Y66nEwCYe_tEHuPJmX0vYFswUDKxKjeHwb-OIQ:1rGg6S:RCCxvGnvay3DsQpTltpgoom6lhJBEYGJ7_jkXT221u0','2024-01-05 14:02:16.651969'),('3w7u3s6u3mrwpwrjv1sxfqlk16ecfajc','.eJxVjDsOwjAQBe_iGlmxiX-U9DmDtV7v4gCypTipEHeHSCmgfTPzXiLCtpa4dVrinMVFKCtOv2MCfFDdSb5DvTWJra7LnOSuyIN2ObVMz-vh_h0U6OVbczYmaAdeDYotB60hadbe2mQouGAA08AMiMGSIrbGI400-rNOTqET7w8RNjiA:1rHKyh:2WD_o-C_4-JtR-2hNRd-4-25oOm0bhCKyOPCHgqg6qY','2024-01-07 09:40:59.163707'),('5031r132thycqp7evgp59ydwv762py8x','.eJxVjEEOwiAUBe_C2hA_BYou3XsGAv-BVA0kpV0Z765NutDtm5n3Ej6sS_FrT7OfIM7CiMPvFgM_Ut0A7qHemuRWl3mKclPkTru8NqTnZXf_Dkro5Vs7gCma0QWQHbRVNp-Og6aks2FonRXYgDEoODiCUqNLibMhMJOy4v0B75g4Zg:1rGvma:Y7VXSQQkDxm_kAvBs9PpFM0LYmnE-6s8WfykPngf90E','2024-01-06 06:46:48.380446'),('58yanr23cqsg6xjv890g0zj5om2zfqr0','.eJxVjMsOwiAQRf-FtSEwU6S4dN9vIDM8pGogKe3K-O_apAvd3nPOfQlP21r81tPi5yguAsXpd2MKj1R3EO9Ub02GVtdlZrkr8qBdTi2m5_Vw_w4K9fKtnTIDK8OQHFmikDNYm6MzpEwKeiCNeNbjAJERIpBLekS2aBQDKMri_QHmKDe1:1rD4z5:6L_-CYncY2vGGk6WvNgo2BnWmwQ-pmV8qMaQCNBpV-s','2023-12-26 15:47:47.955632'),('5o0davntxychp64ujlsw8jckfnrpxhye','.eJxVjEEOwiAQRe_C2hDKABWX7nsGAsyMVA0kpV0Z765NutDtf-_9lwhxW0vYOi1hRnERRpx-txTzg-oO8B7rrcnc6rrMSe6KPGiXU0N6Xg_376DEXr61ZuudhsFAimScBfTGKbSIDDAyjdGgwwHIeLSsBrJZKVCcxrNnnVi8P9TbN9k:1rFZI9:xSNfxM17-J0BY6cBJSfeV0FmbI5CnCkkw4Ct0QxJmnY','2024-01-02 12:33:45.763704'),('78q5absonae4lys0msqw9oetbxoccoat','.eJxVjMsOwiAQRf-FtSEwU6S4dN9vIDM8pGogKe3K-O_apAvd3nPOfQlP21r81tPi5yguAsXpd2MKj1R3EO9Ub02GVtdlZrkr8qBdTi2m5_Vw_w4K9fKtnTIDK8OQHFmikDNYm6MzpEwKeiCNeNbjAJERIpBLekS2aBQDKMri_QHmKDe1:1rDHEB:ElQrjaEGDI8VQDIRt3wt9gWlV1FbtSph85NUW8KkbC4','2023-12-27 04:52:11.341360'),('87qpyqd4dyaq1w89kh2pmkwp1xq39npp','.eJxVjEEOwiAURO_C2pCCUsCl-56BzOeDVA1NSrsy3t026UJ3k3lv5i0C1qWEtaU5jCyuQonTb0eIz1R3wA_U-yTjVJd5JLkr8qBNDhOn1-1w_w4KWtnWnfU2XajvnFfaMQxD4cwK0dq8xey1M71KnimxI6MNETJBM5EHQ3y-7ik5RA:1rGsOP:CnQahhSAQVH27ar0HAr-bOFiCm3xRYcA_5KjoH7XMAU','2024-01-06 03:09:37.042460'),('8ogb2da32zxztt7lo4lweva0sfdidnn8','.eJxVjEEOwiAURO_C2pCCUsCl-56BzOeDVA1NSrsy3t026UJ3k3lv5i0C1qWEtaU5jCyuQonTb0eIz1R3wA_U-yTjVJd5JLkr8qBNDhOn1-1w_w4KWtnWnfU2XajvnFfaMQxD4cwK0dq8xey1M71KnimxI6MNETJBM5EHQ3y-7ik5RA:1rFZ0V:Slc2uDo0y3q4zeEdNU5VDNu_F0062rKDuNFQLn6EWqo','2024-01-02 12:15:31.426503'),('92d0cyo4londj3iy577lo1n4ysqil0rr','.eJxVjDsOwjAQBe_iGln-xJ9Q0ucMlu3dxQFkS3FSIe5OIqWA9s3Me7MQt7WEreMSZmBXZtnld0sxP7EeAB6x3hvPra7LnPih8JN2PjXA1-10_w5K7GWv0Q9GOkU0aqHE4EBqQJQUNXh0Bm02CDKPye6el6AdGVIZyRtBwln2-QLh1Dfo:1rGVmG:27fYn2Hfliz4d89MIMuKrhl9KAaTnstAsNZFpvsrWWQ','2024-01-05 03:00:44.910187'),('9nnbugzx4ig8ozmaxoc7q5ouy7oqvggy','.eJxVjEEOwiAURO_C2pCCUsCl-56BzOeDVA1NSrsy3t026UJ3k3lv5i0C1qWEtaU5jCyuQonTb0eIz1R3wA_U-yTjVJd5JLkr8qBNDhOn1-1w_w4KWtnWnfU2XajvnFfaMQxD4cwK0dq8xey1M71KnimxI6MNETJBM5EHQ3y-7ik5RA:1rFZH1:I67vViND7ZsGjSUwC1iAZ_80iFdBasH-LthfwHtnMiA','2024-01-02 12:32:35.601182'),('bv17164pmk3zmsob35rjj6v5l3pjtkin','.eJxVjDsOwjAQBe_iGln-rImXkp4zWGvvggPIkeKkQtwdIqWA9s3Me6lE61LT2mVOI6uT8urwu2UqD2kb4Du126TL1JZ5zHpT9E67vkwsz_Pu_h1U6vVbhzAUb45eLJBxNjJFKAEMGLIRBdn6jIzxiuLIMhjMAAHJiR8o-KDeH7rCNuA:1rD2Ab:vD6WQzW3Spnxqh-Tmaisv7IChnZ1DJc079eU8ieMBL8','2023-12-26 12:47:29.086349'),('c9nqlh3gztp3z1j38v5m8rr9e16wgtlw','.eJxVjEEOwiAURO_C2pCCUsCl-56BzOeDVA1NSrsy3t026UJ3k3lv5i0C1qWEtaU5jCyuQonTb0eIz1R3wA_U-yTjVJd5JLkr8qBNDhOn1-1w_w4KWtnWnfU2XajvnFfaMQxD4cwK0dq8xey1M71KnimxI6MNETJBM5EHQ3y-7ik5RA:1rCyeF:_SIazqZ91q5CVSzw7L6UebtTZBzHr7UEhSQ3QpKKTNw','2023-12-26 09:01:51.613414'),('dogrgw5c6apzl8nbcj3yb8nk9eu4zwmf','.eJxVjDsOwjAQBe_iGln2bvyjpM8ZLG-84ACypTipEHeHSCmgfTPzXiKmbS1x67zEOYuzMOL0u1GaHlx3kO-p3pqcWl2XmeSuyIN2ObbMz8vh_h2U1Mu3dgG9V5m9cVe2nBlRM5oUQvKAQIAGbCDjgAlAgbaoB8WDJ1bKQhDvD8Y4Nok:1rDnig:-tx9NYS9Jho3tfJP6bmDHyxdEyneAzdsQIKX4CRU35Q','2023-12-28 15:33:50.750960'),('ekbgjpzf2ao7522ahmxum9wagvcvmp51','.eJxVjEEOwiAURO_C2pCCUsCl-56BzOeDVA1NSrsy3t026UJ3k3lv5i0C1qWEtaU5jCyuQonTb0eIz1R3wA_U-yTjVJd5JLkr8qBNDhOn1-1w_w4KWtnWnfU2XajvnFfaMQxD4cwK0dq8xey1M71KnimxI6MNETJBM5EHQ3y-7ik5RA:1rCeug:nUBvyMHShEXHDB1LCriZKhz33RVvi9653t8IrTQYXQ8','2023-12-25 11:57:30.398612'),('esvmf3cpb5j4y5mt6vod5a9xst8hocnk','.eJxVjDsOwjAQBe_iGln-xJ9Q0ucMlu3dxQFkS3FSIe5OIqWA9s3Me7MQt7WEreMSZmBXZtnld0sxP7EeAB6x3hvPra7LnPih8JN2PjXA1-10_w5K7GWv0Q9GOkU0aqHE4EBqQJQUNXh0Bm02CDKPye6el6AdGVIZyRtBwln2-QLh1Dfo:1rFaGC:WjLmXiTrnsdndTGcL3TJDRSNsBrIeta1i6oC38NmS0A','2024-01-02 13:35:48.575096'),('ettga8rpb82uvvz6bscghpxydobzydi6','.eJxVjEEOwiAURO_C2pCCUsCl-56BzOeDVA1NSrsy3t026UJ3k3lv5i0C1qWEtaU5jCyuQonTb0eIz1R3wA_U-yTjVJd5JLkr8qBNDhOn1-1w_w4KWtnWnfU2XajvnFfaMQxD4cwK0dq8xey1M71KnimxI6MNETJBM5EHQ3y-7ik5RA:1rCcDn:5njqQBv9M_3zNGpX8vpHcWV_3QORPuDug-_nLaoQb4g','2023-12-25 09:05:03.503762'),('eyz7cezsj4reb9nkkt1b7fcrtzxoqabb','.eJxVjEEOwiAURO_C2pCCUsCl-56BzOeDVA1NSrsy3t026UJ3k3lv5i0C1qWEtaU5jCyuQonTb0eIz1R3wA_U-yTjVJd5JLkr8qBNDhOn1-1w_w4KWtnWnfU2XajvnFfaMQxD4cwK0dq8xey1M71KnimxI6MNETJBM5EHQ3y-7ik5RA:1rGeqA:c3v-wDxfKyYdnyMab-mykVstVIiHXDXTqMAwvh8sXt0','2024-01-05 12:41:22.697114'),('f8rtu0b3et3ipqtzhg01u65xs6ap5p26','.eJxVjDsOwjAQBe_iGln-xJ9Q0ucMlu3dxQFkS3FSIe5OIqWA9s3Me7MQt7WEreMSZmBXZtnld0sxP7EeAB6x3hvPra7LnPih8JN2PjXA1-10_w5K7GWv0Q9GOkU0aqHE4EBqQJQUNXh0Bm02CDKPye6el6AdGVIZyRtBwln2-QLh1Dfo:1rFvyP:Lvl1wr5PeX4D6cgD5p12LblZ1OY8QD6ln_g_Er5Q5dw','2024-01-03 12:46:53.499853'),('g0tgrlng20lpglxpgn6opihvv4l753nc','.eJxVjEEOwiAQRe_C2pDOFAu4dN8zkIEZpGpoUtqV8e7apAvd_vfef6lA21rC1mQJE6uLMur0u0VKD6k74DvV26zTXNdlinpX9EGbHmeW5_Vw_w4KtfKthSgKIjChg2gRBsfnmB2L4Y66nEwCYe_tEHuPJmX0vYFswUDKxKjeHwb-OIQ:1rFvuw:-kpNBn4E7IpfGqyUjh99WMi5-RBmqosquIdTbtSbJ7w','2024-01-03 12:43:18.816751'),('g5vosnv7p7jud5sworsiefldtd85rx1k','.eJxVjEEOwiAURO_C2pCCUsCl-56BzOeDVA1NSrsy3t026UJ3k3lv5i0C1qWEtaU5jCyuQonTb0eIz1R3wA_U-yTjVJd5JLkr8qBNDhOn1-1w_w4KWtnWnfU2XajvnFfaMQxD4cwK0dq8xey1M71KnimxI6MNETJBM5EHQ3y-7ik5RA:1rFbRu:Koz5U3HRfd1TQDgst2G1l-yozmSll8R-efYXs3avx-4','2024-01-02 14:51:58.197429'),('glf6qrhchsg0am2jyjnlrj2db47ugwv6','.eJxVjEEOwiAQRe_C2pDOFAu4dN8zkIEZpGpoUtqV8e7apAvd_vfef6lA21rC1mQJE6uLMur0u0VKD6k74DvV26zTXNdlinpX9EGbHmeW5_Vw_w4KtfKthSgKIjChg2gRBsfnmB2L4Y66nEwCYe_tEHuPJmX0vYFswUDKxKjeHwb-OIQ:1rGWwF:Mcj4BctVEseA96wZty9Ch1FDRWOopEcACfotXtKbkjI','2024-01-05 04:15:07.436170'),('gv8z7wi2xo2zp2v7118cceejfmtsmp25','.eJxVjDsOwjAQBe_iGln-rImXkp4zWGvvggPIkeKkQtwdIqWA9s3Me6lE61LT2mVOI6uT8urwu2UqD2kb4Du126TL1JZ5zHpT9E67vkwsz_Pu_h1U6vVbhzAUb45eLJBxNjJFKAEMGLIRBdn6jIzxiuLIMhjMAAHJiR8o-KDeH7rCNuA:1rCy8o:gBThuLiMtPjd-ir0zi1sI1oqfO3jaaF5wgR0MfyS_Vk','2023-12-26 08:29:22.967661'),('h22eq73yynhlf5xisopaelvzr74uu2wl','.eJxVjDsOwjAQBe_iGln-xJ9Q0ucMlu3dxQFkS3FSIe5OIqWA9s3Me7MQt7WEreMSZmBXZtnld0sxP7EeAB6x3hvPra7LnPih8JN2PjXA1-10_w5K7GWv0Q9GOkU0aqHE4EBqQJQUNXh0Bm02CDKPye6el6AdGVIZyRtBwln2-QLh1Dfo:1rFvuW:wZ8mAUP2Okl6UObv1cPy-qli0RXLdJLSRUn5JRPY4eU','2024-01-03 12:42:52.582236'),('hf79emdy9mdczfbcrdgw4766sj4tywfd','.eJxVjMsOwiAQRf-FtSEwU6S4dN9vIDM8pGogKe3K-O_apAvd3nPOfQlP21r81tPi5yguAsXpd2MKj1R3EO9Ub02GVtdlZrkr8qBdTi2m5_Vw_w4K9fKtnTIDK8OQHFmikDNYm6MzpEwKeiCNeNbjAJERIpBLekS2aBQDKMri_QHmKDe1:1rD4tX:9fAP_QQMwxsxg3olGg-dqRkDerMyn2bA2DK3-TsVH-g','2023-12-26 15:42:03.333366'),('kkfhtcbjwf2hoyx7ak6wmhvxz86csxvb','.eJxVjDsOwjAQBe_iGln-xJ9Q0ucMlu3dxQFkS3FSIe5OIqWA9s3Me7MQt7WEreMSZmBXZtnld0sxP7EeAB6x3hvPra7LnPih8JN2PjXA1-10_w5K7GWv0Q9GOkU0aqHE4EBqQJQUNXh0Bm02CDKPye6el6AdGVIZyRtBwln2-QLh1Dfo:1rFaqB:S1tF8lwoNocKMH-r72dRBNlogz0_fSbh_s4V5U8jGS8','2024-01-02 14:12:59.236251'),('lqtyojqi3cuq70b7g6gn81v1twwgcp1d','.eJxVjLEOwjAMRP8lM4qSEjstIzvfEDm2QwuolZp2Qvw7rdQBhlvuvbu3SbQufVqrzmkQczHBnH67TPzUcQfyoPE-WZ7GZR6y3RV70Gpvk-jrerh_Bz3Vfltj7lgbHzlEj1wiFMHoCoJ6waaFAJ2UAOzVMdKW3J6LB_Ak2qFz5vMF4fE3rQ:1rD6Hz:Fz-vnwuKs8FQwnV4escAncnvZgqqos0L8IiBEoCtubs','2023-12-26 17:11:23.773253'),('mgc5w4bvzyk1qjy13m613o5lygzhmzmu','.eJxVjDsOwjAQBe_iGln-xJ9Q0ucMlu3dxQFkS3FSIe5OIqWA9s3Me7MQt7WEreMSZmBXZtnld0sxP7EeAB6x3hvPra7LnPih8JN2PjXA1-10_w5K7GWv0Q9GOkU0aqHE4EBqQJQUNXh0Bm02CDKPye6el6AdGVIZyRtBwln2-QLh1Dfo:1rGtE1:xajOGXbrjT9pFaMfeMPmD1dfRlpd-zIoisi2FlBB20U','2024-01-06 04:02:57.124153'),('mgdux4zcj3chcskfj27vgva7i02p35x2','.eJxVjEEOwiAURO_C2pCCUsCl-56BzOeDVA1NSrsy3t026UJ3k3lv5i0C1qWEtaU5jCyuQonTb0eIz1R3wA_U-yTjVJd5JLkr8qBNDhOn1-1w_w4KWtnWnfU2XajvnFfaMQxD4cwK0dq8xey1M71KnimxI6MNETJBM5EHQ3y-7ik5RA:1rFVak:iCHFl7I9T1rD6jgksfdJhIpH2Ezlw2ukNaIJShlMNgU','2024-01-02 08:36:42.476890'),('mqb6o74gt5ffyyvau4erleo8io0jiqyx','.eJxVjEEOwiAQRe_C2hAYKAWX7j0DmWFAqoYmpV0Z765NutDtf-_9l4i4rTVuPS9xYnEWIE6_G2F65LYDvmO7zTLNbV0mkrsiD9rldeb8vBzu30HFXr-1ZxjBQikD5xKCKwgwkEat2Dogoz1oC0qzKmb0rMgQ5xRKdmwcpSTeH9rzOCI:1rCyd8:84dEtSHoZqhegEbdJcg8GyFxhgPqfz-ae6OIgbC_RGU','2023-12-26 09:00:42.201498'),('msrmdc590654nimxuvc4uvdzcsds4a6u','.eJxVjMsOwiAQRf-FtSEwU6S4dN9vIDM8pGogKe3K-O_apAvd3nPOfQlP21r81tPi5yguAsXpd2MKj1R3EO9Ub02GVtdlZrkr8qBdTi2m5_Vw_w4K9fKtnTIDK8OQHFmikDNYm6MzpEwKeiCNeNbjAJERIpBLekS2aBQDKMri_QHmKDe1:1rD4cT:dDDa4oz22x4Pl7ueoy0qg6uDHTa2q_pNezZCd6bZsZw','2023-12-26 15:24:25.662965'),('ne0ywzic53glmmk6bh518n4vt53nu730','.eJxVjEEOwiAQRe_C2pDOFAu4dN8zkIEZpGpoUtqV8e7apAvd_vfef6lA21rC1mQJE6uLMur0u0VKD6k74DvV26zTXNdlinpX9EGbHmeW5_Vw_w4KtfKthSgKIjChg2gRBsfnmB2L4Y66nEwCYe_tEHuPJmX0vYFswUDKxKjeHwb-OIQ:1rFZbF:I_mk5oCHNSK6AA_HeBJWGW6Ki1NSvWX2H3dKCe7YQSs','2024-01-02 12:53:29.100710'),('nxvafars9w2ayke9q0ktqf9rn2ee1fhf','.eJxVjMsOwiAQRf-FtSEwU6S4dN9vIDM8pGogKe3K-O_apAvd3nPOfQlP21r81tPi5yguAsXpd2MKj1R3EO9Ub02GVtdlZrkr8qBdTi2m5_Vw_w4K9fKtnTIDK8OQHFmikDNYm6MzpEwKeiCNeNbjAJERIpBLekS2aBQDKMri_QHmKDe1:1rD4yH:bAYDvEhMxLljFgh_QMOi_ZnuN_eJux_XXGyHV5gb308','2023-12-26 15:46:57.783395'),('pgbvmfoweha1md3shhgdfivzjpmp61ck','.eJxVjEEOwiAURO_C2pCCUsCl-56BzOeDVA1NSrsy3t026UJ3k3lv5i0C1qWEtaU5jCyuQonTb0eIz1R3wA_U-yTjVJd5JLkr8qBNDhOn1-1w_w4KWtnWnfU2XajvnFfaMQxD4cwK0dq8xey1M71KnimxI6MNETJBM5EHQ3y-7ik5RA:1rCycL:KdsZfWp4jwDYLaPcmc9WFv7Wzy08jjYjSX6fiP3cj9s','2023-12-26 08:59:53.553120'),('pyiwu9dskztnvkks1drt9zqkknf6p6o8','.eJxVjMsOwiAQRf-FtSEwU6S4dN9vIDM8pGogKe3K-O_apAvd3nPOfQlP21r81tPi5yguAsXpd2MKj1R3EO9Ub02GVtdlZrkr8qBdTi2m5_Vw_w4K9fKtnTIDK8OQHFmikDNYm6MzpEwKeiCNeNbjAJERIpBLekS2aBQDKMri_QHmKDe1:1rD7d4:hCwbSLvTtfkH1CcT6MlK2C6uGsL6ak-dtHIulfT0j-s','2023-12-26 18:37:14.995913'),('q80g5x4d7vu10panl75nm8bq3htpw15d','.eJxVjEEOgjAQRe_StWkK09KOS_ecoZnOtIIaSCisjHcXEha6_e-9_1aRtnWIW81LHEVdFajL75aIn3k6gDxous-a52ldxqQPRZ-06n6W_Lqd7t_BQHXYaxMaKYil2BA8WjYFxDUkSEIMHoyxzGx854pNbUoBWwAUcEzY7b76fAHoEDfk:1rD3Mz:d7G9bhoLfUIm0_Y8zGgPbeEX5bJsH0USF5zo7SRq7vM','2023-12-26 14:04:21.531588'),('qc042l81a2bdadcv02ru96slej900arj','.eJxVjDsOwjAQBe_iGln-rImXkp4zWGvvggPIkeKkQtwdIqWA9s3Me6lE61LT2mVOI6uT8urwu2UqD2kb4Du126TL1JZ5zHpT9E67vkwsz_Pu_h1U6vVbhzAUb45eLJBxNjJFKAEMGLIRBdn6jIzxiuLIMhjMAAHJiR8o-KDeH7rCNuA:1rD1FO:mfzRP9RKqBn-R8fBRKCNERIe7mbMxCBzucSj4p6LrFk','2023-12-26 11:48:22.198662'),('qt2kph7o1cq5b2larw3j3ghn0c2do2l5','.eJxVjMsOwiAQRf-FtSEwU6S4dN9vIDM8pGogKe3K-O_apAvd3nPOfQlP21r81tPi5yguAsXpd2MKj1R3EO9Ub02GVtdlZrkr8qBdTi2m5_Vw_w4K9fKtnTIDK8OQHFmikDNYm6MzpEwKeiCNeNbjAJERIpBLekS2aBQDKMri_QHmKDe1:1rFVa0:tfknpWsxX2CsMKY8Sc-sZX3DtbbrSMiIrUw-XMlMeHQ','2024-01-02 08:35:56.825073'),('rffiu7m4gmmevkr2lks68ru6zl4rib1g','.eJxVjEEOwiAURO_C2pCCUsCl-56BzOeDVA1NSrsy3t026UJ3k3lv5i0C1qWEtaU5jCyuQonTb0eIz1R3wA_U-yTjVJd5JLkr8qBNDhOn1-1w_w4KWtnWnfU2XajvnFfaMQxD4cwK0dq8xey1M71KnimxI6MNETJBM5EHQ3y-7ik5RA:1rGsYC:XHwX4Nkr2r5C2gUad8OReH-xz_mW60aH1OnSiysOD3o','2024-01-06 03:19:44.418417'),('s4df3v8k2iatdch631vkjbtnumgsyx34','.eJxVjEEOwiAQRe_C2pDOFAu4dN8zkIEZpGpoUtqV8e7apAvd_vfef6lA21rC1mQJE6uLMur0u0VKD6k74DvV26zTXNdlinpX9EGbHmeW5_Vw_w4KtfKthSgKIjChg2gRBsfnmB2L4Y66nEwCYe_tEHuPJmX0vYFswUDKxKjeHwb-OIQ:1rFZKD:J9a0-uOhpnvTaZmrVp6i2xzvnP01NZGj6tULmBcuTBs','2024-01-02 12:35:53.715984'),('t03kc4e2xmvtk1dt8j843uwyc5hvcrui','.eJxVjDsOwjAQBe_iGln-xJ9Q0ucMlu3dxQFkS3FSIe5OIqWA9s3Me7MQt7WEreMSZmBXZtnld0sxP7EeAB6x3hvPra7LnPih8JN2PjXA1-10_w5K7GWv0Q9GOkU0aqHE4EBqQJQUNXh0Bm02CDKPye6el6AdGVIZyRtBwln2-QLh1Dfo:1rFrfh:idQeYGy-upfZfEof-RmChAoGps1RCaiacpiJ1hkD7fk','2024-01-03 08:11:17.208392'),('t3khnl966024oxil7thlsgys1q8ixv5s','.eJxVjMsOwiAQRf-FtSEwU6S4dN9vIDM8pGogKe3K-O_apAvd3nPOfQlP21r81tPi5yguAsXpd2MKj1R3EO9Ub02GVtdlZrkr8qBdTi2m5_Vw_w4K9fKtnTIDK8OQHFmikDNYm6MzpEwKeiCNeNbjAJERIpBLekS2aBQDKMri_QHmKDe1:1rD4W7:H6B_Lf4Be9PwnZUtR662omEx0rWl3fWC3krklTiN4eE','2023-12-26 15:17:51.876836'),('tcga8nnwiqqro3y07qa4qxd4v7fqinnh','.eJxVjEEOwiAUBe_C2hA_BYou3XsGAv-BVA0kpV0Z765NutDtm5n3Ej6sS_FrT7OfIM7CiMPvFgM_Ut0A7qHemuRWl3mKclPkTru8NqTnZXf_Dkro5Vs7gCma0QWQHbRVNp-Og6aks2FonRXYgDEoODiCUqNLibMhMJOy4v0B75g4Zg:1rGkgB:9SWSVrdASNjwseZ6erZD3iUHP7l5IomeGCoEQzHZESQ','2024-01-05 18:55:27.784765'),('udvmtynyi51imq2mrstil12hlvrn4ntf','.eJxVjEEOwiAURO_C2pCCUsCl-56BzOeDVA1NSrsy3t026UJ3k3lv5i0C1qWEtaU5jCyuQonTb0eIz1R3wA_U-yTjVJd5JLkr8qBNDhOn1-1w_w4KWtnWnfU2XajvnFfaMQxD4cwK0dq8xey1M71KnimxI6MNETJBM5EHQ3y-7ik5RA:1rGtst:O-aNUNCd7LzUPhRItZK1OyEluxY7ApdAQWaTXDVceEQ','2024-01-06 04:45:11.200449'),('uo2jok8yxlunq0olf6cne7o0vkhgyusn','.eJxVjMsOwiAQRf-FtSEwU6S4dN9vIDM8pGogKe3K-O_apAvd3nPOfQlP21r81tPi5yguAsXpd2MKj1R3EO9Ub02GVtdlZrkr8qBdTi2m5_Vw_w4K9fKtnTIDK8OQHFmikDNYm6MzpEwKeiCNeNbjAJERIpBLekS2aBQDKMri_QHmKDe1:1rDUPe:tRUVaAKUzQqWwxVXPAbsG_2ARVA7uz1V9JRYNfLoKv8','2023-12-27 18:56:54.767298'),('w1mwta9j7l5zidwwza0bxegs5iwma8t1','.eJxVjEEOwiAQRe_C2pDOFAu4dN8zkIEZpGpoUtqV8e7apAvd_vfef6lA21rC1mQJE6uLMur0u0VKD6k74DvV26zTXNdlinpX9EGbHmeW5_Vw_w4KtfKthSgKIjChg2gRBsfnmB2L4Y66nEwCYe_tEHuPJmX0vYFswUDKxKjeHwb-OIQ:1rFaLQ:FLBxEV9mXFs_bl2L6jUu9NPP4pBM-xz3egcU0yWmM18','2024-01-02 13:41:12.318882'),('wn3hn0nzfqi9qufud1yvx7qbvcp3neef','.eJxVjDsOwjAQBe_iGln-rImXkp4zWGvvggPIkeKkQtwdIqWA9s3Me6lE61LT2mVOI6uT8urwu2UqD2kb4Du126TL1JZ5zHpT9E67vkwsz_Pu_h1U6vVbhzAUb45eLJBxNjJFKAEMGLIRBdn6jIzxiuLIMhjMAAHJiR8o-KDeH7rCNuA:1rCy8o:gBThuLiMtPjd-ir0zi1sI1oqfO3jaaF5wgR0MfyS_Vk','2023-12-26 08:29:22.967707'),('ywnweqz1i9iyr4nq0y8hmh9fvlc7l7m3','.eJxVjEEOwiAQRe_C2pDOFAu4dN8zkIEZpGpoUtqV8e7apAvd_vfef6lA21rC1mQJE6uLMur0u0VKD6k74DvV26zTXNdlinpX9EGbHmeW5_Vw_w4KtfKthSgKIjChg2gRBsfnmB2L4Y66nEwCYe_tEHuPJmX0vYFswUDKxKjeHwb-OIQ:1rFvlD:JWX5z5ylCNgYZH6mHgoSHeQ1DZTk9BNjdOH7WnBfhiE','2024-01-03 12:33:15.812601');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `restaurant_address`
--

DROP TABLE IF EXISTS `restaurant_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `restaurant_address` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `longitude` double NOT NULL,
  `latitude` double NOT NULL,
  `address_name` varchar(50) NOT NULL,
  `address_detail` varchar(50) NOT NULL,
  `display_data` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restaurant_address`
--

LOCK TABLES `restaurant_address` WRITE;
/*!40000 ALTER TABLE `restaurant_address` DISABLE KEYS */;
/*!40000 ALTER TABLE `restaurant_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `restaurant_comment`
--

DROP TABLE IF EXISTS `restaurant_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `restaurant_comment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `content` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `comment_time` datetime(6) NOT NULL,
  `author_id` int NOT NULL,
  `refer_post_id` bigint NOT NULL,
  `reply_to_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `restaurant_comment_author_id_f293d292_fk_users_user_id` (`author_id`),
  KEY `restaurant_comment_refer_post_id_686544fb_fk_restaurant_post_id` (`refer_post_id`),
  KEY `restaurant_comment_reply_to_id_c227c1a6_fk_restaurant_comment_id` (`reply_to_id`),
  CONSTRAINT `restaurant_comment_author_id_f293d292_fk_users_user_id` FOREIGN KEY (`author_id`) REFERENCES `users_user` (`id`),
  CONSTRAINT `restaurant_comment_refer_post_id_686544fb_fk_restaurant_post_id` FOREIGN KEY (`refer_post_id`) REFERENCES `restaurant_post` (`id`),
  CONSTRAINT `restaurant_comment_reply_to_id_c227c1a6_fk_restaurant_comment_id` FOREIGN KEY (`reply_to_id`) REFERENCES `restaurant_comment` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restaurant_comment`
--

LOCK TABLES `restaurant_comment` WRITE;
/*!40000 ALTER TABLE `restaurant_comment` DISABLE KEYS */;
INSERT INTO `restaurant_comment` VALUES (1,'评论内容','2023-12-22 12:21:40.891912',1,1,NULL),(2,'评论内容','2023-12-22 12:22:11.894403',1,1,NULL),(3,'评论内容','2023-12-22 12:24:42.890459',1,1,1),(4,'aaaaaaaaa','2023-12-22 12:28:33.865779',1,1,2),(5,'3说的是个啥呀','2023-12-22 12:29:31.573939',1,1,3),(10,'4说的是个啥呀','2023-12-23 22:32:54.337858',6,1,5),(11,'5说的是个啥呀','2023-12-23 22:33:12.618423',6,1,10),(12,'6说的是个啥呀','2023-12-23 22:33:21.525640',6,1,11),(13,'[x] 这里不支持 Markdown','2023-12-23 22:33:38.397436',6,1,12),(16,'Hello','2023-12-23 22:37:05.430222',6,1,3),(17,'HHHHH','2023-12-23 22:37:46.126298',6,1,3),(21,'123123123','2023-12-23 22:48:37.988141',6,1,5),(27,'123','2023-12-23 22:57:43.600769',6,1,11),(28,'啊啊啊啊啊啊','2023-12-24 00:06:14.666244',1,1,2),(29,'Toby说的是个啥呀','2023-12-24 00:06:45.830767',1,1,12),(30,'哈哈哈哈哈哈xcgg说他要顺着网线暗杀你哈哈哈哈哈','2023-12-24 05:32:47.108143',4,11,NULL),(31,'123\n123\n123\n123\n123','2023-12-24 06:41:25.008389',5,7,NULL),(32,'你小子😡我直接顺着你北航邮箱来暗杀你！','2023-12-24 06:43:43.344233',1,11,NULL),(33,'😈\n😈\n😈\n😈','2023-12-24 06:44:46.809674',4,11,32);
/*!40000 ALTER TABLE `restaurant_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `restaurant_comment_agrees`
--

DROP TABLE IF EXISTS `restaurant_comment_agrees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `restaurant_comment_agrees` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `comment_id` bigint NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `restaurant_comment_agrees_comment_id_user_id_08407c15_uniq` (`comment_id`,`user_id`),
  KEY `restaurant_comment_agrees_user_id_d3b3a192_fk_users_user_id` (`user_id`),
  CONSTRAINT `restaurant_comment_a_comment_id_d519e0c2_fk_restauran` FOREIGN KEY (`comment_id`) REFERENCES `restaurant_comment` (`id`),
  CONSTRAINT `restaurant_comment_agrees_user_id_d3b3a192_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restaurant_comment_agrees`
--

LOCK TABLES `restaurant_comment_agrees` WRITE;
/*!40000 ALTER TABLE `restaurant_comment_agrees` DISABLE KEYS */;
INSERT INTO `restaurant_comment_agrees` VALUES (2,2,1),(1,3,1),(5,4,1),(8,10,1),(7,11,1),(6,12,1);
/*!40000 ALTER TABLE `restaurant_comment_agrees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `restaurant_dish`
--

DROP TABLE IF EXISTS `restaurant_dish`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `restaurant_dish` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `dish_name` varchar(20) NOT NULL,
  `dish_description` varchar(200) NOT NULL,
  `dish_price` double NOT NULL,
  `dish_img` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restaurant_dish`
--

LOCK TABLES `restaurant_dish` WRITE;
/*!40000 ALTER TABLE `restaurant_dish` DISABLE KEYS */;
/*!40000 ALTER TABLE `restaurant_dish` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `restaurant_post`
--

DROP TABLE IF EXISTS `restaurant_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `restaurant_post` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `content` varchar(2000) NOT NULL,
  `grade` int NOT NULL,
  `avg_price` int NOT NULL,
  `image` varchar(100) NOT NULL,
  `date` datetime(6) NOT NULL,
  `restaurant_id` bigint NOT NULL,
  `creator_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `restaurant_post_restaurant_id_9e8b9388_fk_restauran` (`restaurant_id`),
  KEY `restaurant_post_creator_id_41ccb73d_fk_users_user_id` (`creator_id`),
  CONSTRAINT `restaurant_post_creator_id_41ccb73d_fk_users_user_id` FOREIGN KEY (`creator_id`) REFERENCES `users_user` (`id`),
  CONSTRAINT `restaurant_post_restaurant_id_9e8b9388_fk_restauran` FOREIGN KEY (`restaurant_id`) REFERENCES `restaurant_restaurant` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restaurant_post`
--

LOCK TABLES `restaurant_post` WRITE;
/*!40000 ALTER TABLE `restaurant_post` DISABLE KEYS */;
INSERT INTO `restaurant_post` VALUES (1,'帖子标题','帖子内容啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊',5,50,'post_image/default.png','2023-12-22 08:46:16.601929',1,1),(2,'我是标题','<p>内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容<strong>内容内容内容内容内容内容内容内容内容内容内容内容内容内容</strong></p>',4,66,'post_image/default.png','2023-12-22 08:49:32.025347',1,1),(3,'好吃的','<h1>啥呀</h1><h2>不知道</h2><blockquote>assadscadvas</blockquote><ul><li>啊啊啊啊啊啊啊啊</li></ul><pre class=\"ql-syntax\" spellcheck=\"false\">Restaurant.objects.filter(tags__name=tag).all()\n</pre><ul><li><img src=\"https://hangeat.oss-cn-beijing.aliyuncs.com/media/assert/5944272d-50a4-47cb-9af9-f3f5ae265da8.jpg\" data-align=\"left\" style=\"display: inline; margin: 0px 1em 1em 0px; float: left; cursor: nwse-resize;\" width=\"224\" height=\"168\"></li></ul>',4,33,'post_image/default.png','2023-12-23 16:28:11.352194',1,1),(4,'好吃的','<ol><li>真好吃</li><li>真好吃</li><li>真好吃</li></ol>',3,61,'post_image/default.png','2023-12-23 17:15:14.638688',1,6),(5,'好吃的','<ol><li>好吃的</li><li>好吃的</li><li>好吃的</li></ol>',3,61,'post_image/default.png','2023-12-23 17:16:20.474881',1,6),(6,'好吃的','<ol><li>好吃的</li><li>好吃的</li><li>好吃的</li></ol>',3,61,'post_image/屏幕截图_2022-06-14_205019.png','2023-12-23 17:17:35.169536',1,6),(7,'Yammmmmmm','',3,123,'post_image/屏幕截图_2022-06-05_231729.png','2023-12-23 17:25:46.067261',1,6),(9,'阿尼亚真可爱','<h1>阿尼亚真可爱</h1><p><br></p>',4,34,'post_image/阿尼亚.png','2023-12-23 19:39:34.999503',5,6),(10,'好吃的','<p>123<em> 123</em> <em> 123 </em> 123<em> 123</em>  </p><p><strong>123</strong> </p>',5,64,'post_image/102023-12-24_001807.3195540000.png','2023-12-24 00:18:07.163315',5,4),(11,'xcgg好吃的','<p>好吃的xcgg</p>',5,10000,'post_image/112023-12-24_011953.6224100000.png','2023-12-24 01:19:53.226431',1,9),(12,'好吃，爱吃，下次还来','<p>编什么什么术，坐我右边的小孩馋哭了。</p>',5,5500,'post_image/122023-12-24_013932.6485970000.png','2023-12-24 01:39:32.053569',8,10),(13,'怎么哪都有wxm啊','<p>佬！浇浇编译！！</p>',1,666,'post_image/132023-12-24_020256.0777880000.png','2023-12-24 02:02:55.514889',8,9),(15,'啊？','<p>五星上将麦克阿瑟评价道：“好，很有精神”</p>',5,5500,'post_image/152023-12-24_070409.1687490000.png','2023-12-24 07:04:08.554028',8,1),(16,'<font color=\"red\">TEST</font>','<script>alert(\'xss test\');</script>',-1,0,'post_image/default.png','2023-12-24 07:08:08.862751',1,15),(17,'破学校','<img src=\"#\" onerror=\"alert(\'xss test\')\"/>',1,0,'post_image/default.png','2023-12-24 07:20:25.233743',8,15),(18,'11111','<p><img src=\"https://hangeat.oss-cn-beijing.aliyuncs.com/media/assert/c016ef3f-d901-4f49-94f0-27ec7377960c.jpg\" width=\"780\" height=\"551.6078581526862\" style=\"\"></p><p>大图片（1.9M）</p>',5,55,'post_image/182023-12-24_081446.4236530000.png','2023-12-24 08:14:44.376828',5,5),(20,'潇湘阁是真的狠辣','<h1>太辣了家人们</h1><p>标题: 💥【必打卡】潇湘阁——火辣辣的味蕾盛宴🔥</p><p><br></p><p>正文: 👀 看这里！看这里！📢 我发现了一家宝藏餐厅——潇湘阁！😍 这里的菜品真的超级辣，简直就是辣食爱好者的天堂！🌶️🌶️🌶️</p><p><br></p><p>家人们，谁懂啊，他们的菜品真的是绝绝子！👍 无论是毛氏红烧肉、剁椒鱼头还是辣椒炒肉，每一道菜都能让你感受到正宗的湖南风味和辣味。🍲 而且，他们的厨师团队还经常推出新菜品，好吃到翘jiojio，让你的味蕾每次都有新的体验！🆕</p><p><br></p><p>再来说说他们的环境吧！🏠 室内和室外的装修都非常精美，让人一进去就感觉特别舒适。😌 而且，他们的服务也是一级棒，服务员们总是面带微笑，让你感到像在自己家一样自在。💁‍♀️</p><p><br></p><p>最后，我必须强调，他们的菜品真的很辣！🔥 如果你是辣食爱好者，那么这里绝对是你的天堂，暴风吸入，真的绝绝子！😋。但是，如果你不太能接受辣味的话，记得提前告知服务员调整口味哦。😉</p><p><br></p><p>总的来说，潇湘阁是一家非常值得推荐的餐厅。无论是菜品、环境还是服务，都给人留下了深刻的印象。👏 赶快带上你的小伙伴一起去体验一下吧！👫</p><p><br></p><p>#美食探店 #湖南菜 #辣椒爱好者 #美食日记 #必打卡餐厅</p><p><br></p><p>(以上内容由小爱同学生成，注意甄别)</p>',5,66,'post_image/202023-12-24_093028.9882920000.png','2023-12-24 09:30:28.713085',2,1),(21,'猫猫！','<p>看看会动的🥹</p>',5,111,'post_image/212023-12-24_123240.6862260000.png','2023-12-24 12:32:39.889087',7,13);
/*!40000 ALTER TABLE `restaurant_post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `restaurant_post_agrees`
--

DROP TABLE IF EXISTS `restaurant_post_agrees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `restaurant_post_agrees` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `post_id` bigint NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `restaurant_post_agrees_post_id_user_id_11c3f7a6_uniq` (`post_id`,`user_id`),
  KEY `restaurant_post_agrees_user_id_a4ee5577_fk_users_user_id` (`user_id`),
  CONSTRAINT `restaurant_post_agrees_post_id_8a455387_fk_restaurant_post_id` FOREIGN KEY (`post_id`) REFERENCES `restaurant_post` (`id`),
  CONSTRAINT `restaurant_post_agrees_user_id_a4ee5577_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restaurant_post_agrees`
--

LOCK TABLES `restaurant_post_agrees` WRITE;
/*!40000 ALTER TABLE `restaurant_post_agrees` DISABLE KEYS */;
INSERT INTO `restaurant_post_agrees` VALUES (20,1,1),(15,1,5),(6,2,4),(21,7,6),(30,12,1),(24,12,10),(28,13,1),(25,13,9),(29,15,1),(31,17,16),(32,20,13);
/*!40000 ALTER TABLE `restaurant_post_agrees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `restaurant_recommenddish`
--

DROP TABLE IF EXISTS `restaurant_recommenddish`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `restaurant_recommenddish` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `recommend_time` datetime(6) NOT NULL,
  `reason` varchar(200) NOT NULL,
  `price` double NOT NULL,
  `dish_id` bigint NOT NULL,
  `post_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `restaurant_recommenddish_dish_id_2b4fb87b_fk_restaurant_dish_id` (`dish_id`),
  KEY `restaurant_recommenddish_post_id_9894471e_fk_restaurant_post_id` (`post_id`),
  CONSTRAINT `restaurant_recommenddish_dish_id_2b4fb87b_fk_restaurant_dish_id` FOREIGN KEY (`dish_id`) REFERENCES `restaurant_dish` (`id`),
  CONSTRAINT `restaurant_recommenddish_post_id_9894471e_fk_restaurant_post_id` FOREIGN KEY (`post_id`) REFERENCES `restaurant_post` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restaurant_recommenddish`
--

LOCK TABLES `restaurant_recommenddish` WRITE;
/*!40000 ALTER TABLE `restaurant_recommenddish` DISABLE KEYS */;
/*!40000 ALTER TABLE `restaurant_recommenddish` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `restaurant_restaurant`
--

DROP TABLE IF EXISTS `restaurant_restaurant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `restaurant_restaurant` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` varchar(500) NOT NULL,
  `detail_addr` varchar(200) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `img` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `address_id` bigint DEFAULT NULL,
  `creator_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `restaurant_restauran_address_id_874b3688_fk_restauran` (`address_id`),
  KEY `restaurant_restaurant_creator_id_c927e7dd_fk_users_user_id` (`creator_id`),
  CONSTRAINT `restaurant_restauran_address_id_874b3688_fk_restauran` FOREIGN KEY (`address_id`) REFERENCES `restaurant_address` (`id`),
  CONSTRAINT `restaurant_restaurant_creator_id_c927e7dd_fk_users_user_id` FOREIGN KEY (`creator_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restaurant_restaurant`
--

LOCK TABLES `restaurant_restaurant` WRITE;
/*!40000 ALTER TABLE `restaurant_restaurant` DISABLE KEYS */;
INSERT INTO `restaurant_restaurant` VALUES (1,'费大厨','','可莉不知道哦','11451411','restaurant/费大厨2023-12-23_083832.1704500000.png','2023-12-11 08:43:26.575703','2023-12-23 08:38:32.563778',NULL,2),(2,'潇湘阁','只在北京开的正宗湘菜馆','北京连锁的，好多地方都有，自己搜去叭','114514','restaurant/潇湘阁2023-12-23_064728.8329180000.png','2023-12-11 08:44:06.123143','2023-12-24 09:34:51.567674',NULL,1),(3,'小香哥','','可莉不知道哦','114514','restaurant/default.png','2023-12-11 08:46:10.614969','2023-12-11 08:46:10.615046',NULL,1),(5,'小猫酒馆','这里是小猫酒馆！欢迎你来玩哦!\n这里是小猫酒馆！欢迎你来玩哦!\n这里是小猫酒馆！欢迎你来玩哦!','小猫星球','meow','restaurant/小猫酒馆2023-12-22_181228.0784360000.png','2023-12-22 17:30:12.427888','2023-12-22 18:46:51.615540',NULL,4),(6,'香菜馆','','种满香菜的地方','煤油','restaurant/default.png','2023-12-23 02:28:55.550485','2023-12-24 08:49:08.200978',NULL,1),(7,'小猫 Cafe','小猫咖啡馆☕️','小猫星球','meow','restaurant/小猫_Cafe2023-12-23_052726.3484090000.png','2023-12-23 05:26:58.343827','2023-12-23 05:27:26.718221',NULL,4),(8,'北京二次元大厂子','','北京市海淀区37号','010-83429695','restaurant/北京二次元大厂子2023-12-24_014407.5310950000.png','2023-12-24 01:34:12.460539','2023-12-24 01:44:07.773165',NULL,10);
/*!40000 ALTER TABLE `restaurant_restaurant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `restaurant_restauranttag`
--

DROP TABLE IF EXISTS `restaurant_restauranttag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `restaurant_restauranttag` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `restaurant_id` bigint NOT NULL,
  `tag_id` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `restaurant_restauran_restaurant_id_52338bda_fk_restauran` (`restaurant_id`),
  KEY `restaurant_restauranttag_tag_id_f0535003_fk_restaurant_tag_name` (`tag_id`),
  CONSTRAINT `restaurant_restauran_restaurant_id_52338bda_fk_restauran` FOREIGN KEY (`restaurant_id`) REFERENCES `restaurant_restaurant` (`id`),
  CONSTRAINT `restaurant_restauranttag_tag_id_f0535003_fk_restaurant_tag_name` FOREIGN KEY (`tag_id`) REFERENCES `restaurant_tag` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restaurant_restauranttag`
--

LOCK TABLES `restaurant_restauranttag` WRITE;
/*!40000 ALTER TABLE `restaurant_restauranttag` DISABLE KEYS */;
INSERT INTO `restaurant_restauranttag` VALUES (1,'2023-12-11 08:44:20.814309',2,'湘菜'),(2,'2023-12-11 08:44:20.819435',2,'斯哈斯哈'),(3,'2023-12-11 08:44:20.823625',2,'好辣好辣'),(4,'2023-12-19 09:27:34.245399',3,'湘菜'),(5,'2023-12-22 18:43:40.188799',5,'酒馆'),(7,'2023-12-22 18:51:48.859766',5,'小猫'),(8,'2023-12-23 05:26:58.386031',7,'meow'),(9,'2023-12-23 05:26:58.394454',7,'Cafe'),(10,'2023-12-23 05:26:58.399783',7,'小猫');
/*!40000 ALTER TABLE `restaurant_restauranttag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `restaurant_tag`
--

DROP TABLE IF EXISTS `restaurant_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `restaurant_tag` (
  `name` varchar(20) NOT NULL,
  `description` varchar(200) NOT NULL,
  `creator_id` int DEFAULT NULL,
  PRIMARY KEY (`name`),
  KEY `restaurant_tag_creator_id_34f16e9d_fk_users_user_id` (`creator_id`),
  CONSTRAINT `restaurant_tag_creator_id_34f16e9d_fk_users_user_id` FOREIGN KEY (`creator_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restaurant_tag`
--

LOCK TABLES `restaurant_tag` WRITE;
/*!40000 ALTER TABLE `restaurant_tag` DISABLE KEYS */;
INSERT INTO `restaurant_tag` VALUES ('Cafe','',4),('meow','',4),('好辣好辣','',1),('小猫','',4),('斯哈斯哈','',1),('湘菜','',1),('酒馆','',4);
/*!40000 ALTER TABLE `restaurant_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_authrecord`
--

DROP TABLE IF EXISTS `users_authrecord`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_authrecord` (
  `id` int NOT NULL AUTO_INCREMENT,
  `login_at` datetime(6) NOT NULL,
  `expires_by` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `users_authrecord_user_id_f991b03f_fk_users_user_id` (`user_id`),
  CONSTRAINT `users_authrecord_user_id_f991b03f_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=141 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_authrecord`
--

LOCK TABLES `users_authrecord` WRITE;
/*!40000 ALTER TABLE `users_authrecord` DISABLE KEYS */;
INSERT INTO `users_authrecord` VALUES (41,'2023-12-19 08:35:56.822201','2023-12-25 08:35:56.822201',3),(84,'2023-12-23 06:46:48.366203','2023-12-29 06:46:48.366203',5),(99,'2023-12-24 00:57:28.844512','2023-12-30 00:57:28.844512',7),(100,'2023-12-24 00:57:50.658835','2023-12-30 00:57:50.658835',8),(101,'2023-12-24 01:19:25.949171','2023-12-30 01:19:25.949171',9),(105,'2023-12-24 04:15:12.832307','2023-12-30 04:15:12.832307',12),(112,'2023-12-24 05:35:11.595234','2023-12-30 05:35:11.595234',14),(114,'2023-12-24 06:40:37.706238','2023-12-30 06:40:37.706238',15),(116,'2023-12-24 06:54:06.624761','2023-12-30 06:54:06.624761',11),(125,'2023-12-24 11:58:42.099726','2023-12-30 11:58:42.099726',10),(126,'2023-12-24 12:31:07.354291','2023-12-30 12:31:07.354291',13),(131,'2023-12-24 15:35:25.935633','2023-12-30 15:35:25.935633',1),(140,'2023-12-24 18:18:20.345186','2023-12-30 18:18:20.345186',6);
/*!40000 ALTER TABLE `users_authrecord` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_collection`
--

DROP TABLE IF EXISTS `users_collection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_collection` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `collections_id` bigint NOT NULL,
  `collectors_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `users_collection_collections_id_095939d0_fk_restauran` (`collections_id`),
  KEY `users_collection_collectors_id_0c391c26_fk_users_user_id` (`collectors_id`),
  CONSTRAINT `users_collection_collections_id_095939d0_fk_restauran` FOREIGN KEY (`collections_id`) REFERENCES `restaurant_restaurant` (`id`),
  CONSTRAINT `users_collection_collectors_id_0c391c26_fk_users_user_id` FOREIGN KEY (`collectors_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_collection`
--

LOCK TABLES `users_collection` WRITE;
/*!40000 ALTER TABLE `users_collection` DISABLE KEYS */;
INSERT INTO `users_collection` VALUES (2,'2023-12-22 03:26:50.387557',2,6),(9,'2023-12-23 03:50:27.872738',6,1),(10,'2023-12-23 04:33:54.622072',5,4),(15,'2023-12-23 05:34:08.449468',7,4),(19,'2023-12-23 06:47:07.231319',7,5),(20,'2023-12-23 07:47:56.264919',1,2),(21,'2023-12-23 08:36:35.752604',1,1),(24,'2023-12-23 11:22:27.579735',1,5),(25,'2023-12-23 12:12:12.219715',2,1),(26,'2023-12-24 01:44:56.146959',8,10),(27,'2023-12-24 04:16:56.242139',7,12),(28,'2023-12-24 07:01:32.942750',8,1),(29,'2023-12-24 15:41:17.675034',7,1),(30,'2023-12-24 17:44:00.811380',5,6);
/*!40000 ALTER TABLE `users_collection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_message`
--

DROP TABLE IF EXISTS `users_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_message` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `content` varchar(200) NOT NULL,
  `time` datetime(6) NOT NULL,
  `isRead` tinyint(1) NOT NULL,
  `receiver_id` int NOT NULL,
  `sender_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `users_message_receiver_id_dd5bba90_fk_users_user_id` (`receiver_id`),
  KEY `users_message_sender_id_d1e3d44e_fk_users_user_id` (`sender_id`),
  CONSTRAINT `users_message_receiver_id_dd5bba90_fk_users_user_id` FOREIGN KEY (`receiver_id`) REFERENCES `users_user` (`id`),
  CONSTRAINT `users_message_sender_id_d1e3d44e_fk_users_user_id` FOREIGN KEY (`sender_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_message`
--

LOCK TABLES `users_message` WRITE;
/*!40000 ALTER TABLE `users_message` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_subscribe`
--

DROP TABLE IF EXISTS `users_subscribe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_subscribe` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `subscriber_id` int NOT NULL,
  `subscription_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `users_subscribe_subscriber_id_314add7e_fk_users_user_id` (`subscriber_id`),
  KEY `users_subscribe_subscription_id_58db0aae_fk_users_user_id` (`subscription_id`),
  CONSTRAINT `users_subscribe_subscriber_id_314add7e_fk_users_user_id` FOREIGN KEY (`subscriber_id`) REFERENCES `users_user` (`id`),
  CONSTRAINT `users_subscribe_subscription_id_58db0aae_fk_users_user_id` FOREIGN KEY (`subscription_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_subscribe`
--

LOCK TABLES `users_subscribe` WRITE;
/*!40000 ALTER TABLE `users_subscribe` DISABLE KEYS */;
INSERT INTO `users_subscribe` VALUES (5,'2023-12-14 11:46:07.972298',1,3),(6,'2023-12-14 12:14:34.349427',3,4),(18,'2023-12-19 13:32:07.693004',2,4),(19,'2023-12-19 13:40:15.746963',5,6),(23,'2023-12-19 13:45:17.052079',6,4),(27,'2023-12-20 07:38:23.028855',4,6),(31,'2023-12-23 07:46:05.407326',4,2),(38,'2023-12-23 11:26:35.133840',2,5),(39,'2023-12-24 00:17:19.744078',6,1),(40,'2023-12-24 01:40:17.772639',4,10),(41,'2023-12-24 01:40:33.352917',1,10),(42,'2023-12-24 01:51:33.961792',6,10),(43,'2023-12-24 02:00:32.660638',10,9),(44,'2023-12-24 02:27:29.945897',9,10),(45,'2023-12-24 05:54:13.828392',9,1),(46,'2023-12-24 08:13:26.374393',3,1),(47,'2023-12-24 10:01:12.944474',10,1);
/*!40000 ALTER TABLE `users_subscribe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user`
--

DROP TABLE IF EXISTS `users_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `password` varchar(256) NOT NULL,
  `email` varchar(254) NOT NULL,
  `gender` varchar(32) NOT NULL,
  `motto` varchar(256) NOT NULL,
  `avatar` varchar(100) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `last_login` datetime(6) NOT NULL,
  `last_ip` char(39) DEFAULT NULL,
  `isDelete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user`
--

LOCK TABLES `users_user` WRITE;
/*!40000 ALTER TABLE `users_user` DISABLE KEYS */;
INSERT INTO `users_user` VALUES (1,0,'volca','','',0,1,'pbkdf2_sha256$600000$3i8ky8HTvZbSjupPGxoeUx$pYmsPNmi+eKM0SC6nyPzH0a2ZMyFtKqFUu0hPaT46cM=','21373254@buaa.edu.cn','保密','生性爱吃~🤤🤣','avatar/volca2023-12-24_082141.0801040000.png','2023-12-11 08:31:53.602941','2023-12-24 08:21:42.880866','2001:250:206:5ffe:cddf:bbfe:1f10:f2a5',0),(2,0,'volca2','','',0,1,'pbkdf2_sha256$600000$vOGPNw8VCbW3dxTeKqhjyt$Z2NDu+sMiXAitQV9CDT/rCgYO9fLT2aXAKOLBPojqAQ=','volcaxiaoc@buaa.edu.cn','保密','这个人很难，就很懒','avatar/default.png','2023-12-11 08:37:20.718343','2023-12-23 07:53:05.367011','2001:250:206:5ffe:cddf:bbfe:1f10:f2a5',0),(3,0,'default','','',0,1,'pbkdf2_sha256$600000$1ph4Al84Sjepl0e41YOSHV$K+WQ0poFXUHqL9FSkQtcOddoB4Zat6+qTqaF5Grl4cI=','','保密','该用户已注销','avatar/delete.png','2023-12-11 10:00:58.840936','2023-12-19 11:54:37.334291','106.39.42.212, ::1',1),(4,0,'TobyQQ','','',0,1,'pbkdf2_sha256$600000$Ddf0fZAIi0iJGwAvJl6mnl$Kj5MEn5fW2VcARrwsS+MEYGZEaiQTyQBt7lQLEIvXcg=','toby3030@qq.com','保密','阿妮亚最可爱啦！','avatar/TobyQQ.png','2023-12-12 15:01:36.354743','2023-12-23 04:01:25.938760','::1',0),(5,0,'SRZ','','',0,1,'pbkdf2_sha256$600000$pSXwfxf1XMuDMSScgh7KmU$/NFBWq4umtC8BL15r4CFXyGHy0C429DiucM+V03iArM=','shiruizhi@buaa.edu.cn','保密','这个人很懒，什么都没有留下','avatar/SRZ2023-12-22_185638.9177490000.png','2023-12-14 15:33:50.511853','2023-12-23 06:46:48.350973','::1',0),(6,0,'TobyShi','','',0,1,'pbkdf2_sha256$600000$1oducBOAB7QXIg1AdyQxNT$8HsUrOMinPo2sposOevyepMNL7lFGoK1N/U/aKQINRA=','21373433@buaa.edu.cn','保密','这个人很懒，什么都没有留下?\n哼哼哼','avatar/TobyShi2023-12-22_042056.1871040000.png','2023-12-19 13:35:48.292520','2023-12-23 04:02:57.118489','2001:250:206:813f:a414:1a2c:aaf3:2a7d',0),(7,0,'拙墨Yt','','',0,1,'pbkdf2_sha256$600000$LhLEcsXjBedp2iRPABYlXo$Q2qtd7eVSJAEyCgJ1qlfxA01jStwsK5OAPwISAd1Ifg=','22373337@buaa.edu.cn','保密','恰恰恰，饭饭饭，有fun请务必喊我','avatar/拙墨Yt2023-12-24_005836.6986770000.png','2023-12-24 00:57:27.261672','2023-12-24 01:01:20.496779','106.39.42.235, ::1',0),(8,0,'Tengpaz','','',0,1,'pbkdf2_sha256$600000$YyLCBi4qFnFKpSBlopgm6o$UNU6zPX9dpBhHi46eF1u5LGdw8hs1RWNyvsCFXWuMgI=','23373097@buaa.edu.cn','保密','aaaa这位是渣渣','avatar/Tengpaz2023-12-24_005811.8684250000.png','2023-12-24 00:57:49.140475','2023-12-24 00:58:32.195343','106.39.42.209, ::1',0),(9,0,'vocal-是xcgg！！','','',0,1,'pbkdf2_sha256$600000$9rrXh0rsFY5HBJzOvT6t4R$SkmnqOzBf034q05IvWSoH9BCgXUFFs8OdIdRWgCNwug=','22373058@buaa.edu.cn','保密','这个人很懒，什么都没有留下','avatar/vocal-是xcgg2023-12-24_020122.5582350000.png','2023-12-24 01:19:24.457829','2023-12-24 02:01:22.902747','106.39.42.243, ::1',0),(10,0,'zlrのfan','','',0,1,'pbkdf2_sha256$600000$WtA3EfdOHgJSgnNz9rgWqD$dpvsr2UkJUI09Bje0E/z4yFOHOn5eNSunNDQjCF/yvs=','22373300@buaa.edu.cn','保密','新东门有k,新东门有k,新东门有k!','avatar/zlrのfan2023-12-24_014641.2658880000.png','2023-12-24 01:29:22.048687','2023-12-24 01:46:45.098881','106.39.42.227, ::1',0),(11,0,'Nyamu','','',0,1,'pbkdf2_sha256$600000$invbb0TSfOPUANqaYDEslX$Qr/fzTbM3zCgY2AaRD0Ga1d+GlY3MH2YOIo1V0FRsgQ=','21373490@buaa.edu.cn','保密','这个人很懒，什么都没有留下','avatar/Movzr2023-12-24_072618.9874300000.png','2023-12-24 04:08:54.382419','2023-12-24 07:29:04.714283','106.39.42.201, ::1',0),(12,0,'k','','',0,1,'pbkdf2_sha256$600000$WyE4Puw0bXbYJSliUZsh2m$6w+M2jXa1mB2xdN7bC8lGm425+bTza8ce6tg/1D8zmQ=','22373080@buaa.edu.cn','保密','这个人很懒，什么都没有留下','avatar/swkfk2023-12-24_075542.0856620000.png','2023-12-24 04:15:11.372550','2023-12-24 07:55:43.487696','106.39.42.218, ::1',0),(13,0,'fatiger','','',0,1,'pbkdf2_sha256$600000$Re0GzwzNMUAG8fUDiTobWI$o7KAJ2NA5wBVkxIxB7gLAxmPMN/cXzjt/4KX3bQXzWQ=','22371351@buaa.edu.cn','保密','🥵炫在北航','avatar/fatiger2023-12-24_044459.1071490000.png','2023-12-24 04:43:53.263251','2023-12-24 06:57:37.899374','106.39.42.219, ::1',0),(14,0,'pluto','','',0,1,'pbkdf2_sha256$600000$LuOEXDYsx6phB7TXrOpVfD$LTiS/8P3rA9poT7pfNMfOHSOucbJR1HGM4udr4WPh+0=','21373061@buaa.edu.cn','保密','这个人很懒，什么都没有留下','avatar/default.png','2023-12-24 05:35:09.954236','2023-12-24 05:35:09.954430','45.8.220.194, ::1',0),(15,0,'wtester','','',0,1,'pbkdf2_sha256$600000$jmHeAmfjekFgZBLmiGgz1V$EPMD0fSlJEbpqWszotfO+MEntQhL/e9oUWiT4EcPa40=','auqa6_invite@qq.com','保密','%253Cscript%253Ealert(`xss test`)%253C/script%253E','avatar/default.png','2023-12-24 06:39:59.995058','2023-12-24 06:47:01.180759','106.39.42.233, ::1',0),(16,1,'admin','','',1,1,'pbkdf2_sha256$600000$oJTuZtfpjvVfxfnkpcW351$GGvmeZ5YfOfdVlQI7nGwAxkml+aVaGOj/hgl1r4oF0o=','2322863798@qq.com','保密','这个人很懒，什么都没有留下','avatar/default.png','2023-12-24 09:40:40.175541','2023-12-24 09:40:59.161302',NULL,0);
/*!40000 ALTER TABLE `users_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user_groups`
--

DROP TABLE IF EXISTS `users_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_user_groups_user_id_group_id_b88eab82_uniq` (`user_id`,`group_id`),
  KEY `users_user_groups_group_id_9afc8d0e_fk_auth_group_id` (`group_id`),
  CONSTRAINT `users_user_groups_group_id_9afc8d0e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `users_user_groups_user_id_5f6f5a90_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user_groups`
--

LOCK TABLES `users_user_groups` WRITE;
/*!40000 ALTER TABLE `users_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user_user_permissions`
--

DROP TABLE IF EXISTS `users_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_user_user_permissions_user_id_permission_id_43338c45_uniq` (`user_id`,`permission_id`),
  KEY `users_user_user_perm_permission_id_0b93982e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `users_user_user_perm_permission_id_0b93982e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `users_user_user_permissions_user_id_20aca447_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user_user_permissions`
--

LOCK TABLES `users_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `users_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-25  2:18:30
