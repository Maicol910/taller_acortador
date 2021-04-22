-- --------------------------------------------------------
-- Host:                         localhost
-- Versión del servidor:         10.5.8-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para acortador
CREATE DATABASE IF NOT EXISTS `acortador` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `acortador`;

-- Volcando estructura para tabla acortador.acortador_base
CREATE TABLE IF NOT EXISTS `acortador_base` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `usuario_id` int(11) unsigned DEFAULT NULL,
  `acortador` varchar(50) DEFAULT NULL,
  `link` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `acortador` (`acortador`),
  KEY `FK_acortador_base_usuario` (`usuario_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla acortador.acortador_base: ~10 rows (aproximadamente)
/*!40000 ALTER TABLE `acortador_base` DISABLE KEYS */;
INSERT INTO `acortador_base` (`id`, `usuario_id`, `acortador`, `link`) VALUES
	(1, NULL, '90lq', 'https://www.youtube.com/watch?v=8NwhTPAWdO8'),
	(2, NULL, 'oUop', 'https://www.youtube.com/watch?v=Xe6wWVvi-AQ'),
	(4, NULL, 'uZd8', 'https://www.youtube.com/watch?v=VAc0xuVa7jI'),
	(6, 49, 'Pjpq', 'https://drive.google.com/file/d/1P6RMeiysKtKOqVuwYCarhh9AVTmfzj_Z/view'),
	(7, NULL, 'BSUI', 'https://www.youtube.com/watch?v=3y-BLBlBk_8'),
	(8, NULL, '2por', 'https://www.youtube.com/watch?v=3y-BLBlBk_8'),
	(9, NULL, '5Cb1', 'https://www.youtube.com/'),
	(10, NULL, '9VLp', 'https://www.youtube.com/watch?v=aB52h93Bax0'),
	(11, NULL, '6SjD', 'https://www.youtube.com/watch?v=aB52h93Bax0'),
	(13, 49, 'o1Xu', 'https://www.youtube.com/watch?v=f-WjdPl8Tr0');
/*!40000 ALTER TABLE `acortador_base` ENABLE KEYS */;

-- Volcando estructura para tabla acortador.usuario
CREATE TABLE IF NOT EXISTS `usuario` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `verificacion` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `password` (`password`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla acortador.usuario: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` (`id`, `nombre`, `email`, `password`, `verificacion`) VALUES
	(49, 'maicol', 'maicoljosa910@gmail.com', '078563f337ec6d6fedf131ddc857db19', NULL);
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
