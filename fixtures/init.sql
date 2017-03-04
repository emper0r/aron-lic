DROP TABLE IF EXISTS `Licenza_license`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Licenza_license` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `client` varchar(64) NOT NULL,
  `province` varchar(16) NOT NULL,
  `name` varchar(32) NOT NULL,
  `email` varchar(254) NOT NULL,
  `active_date` date NOT NULL,
  `exp_date` date NOT NULL,
  `active_lic` tinyint(1) NOT NULL,
  `req` varchar(64) NOT NULL,
  `lic` varchar(64) NOT NULL,
  `server_id` varchar(32) DEFAULT NULL,
  `qty_dev` integer(40) NOT NULL,
  `pwd_client` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

