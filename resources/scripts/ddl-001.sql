-- David Sánchez Ruiz

--
-- Creacion de tablas
--

CREATE TABLE `estacion` (
  `nombre` varchar(100) NOT NULL,
  `ubication` point NOT NULL,
  `troncal` bigint(20) NOT NULL
);

CREATE TABLE `sector` (
  `nombre` varchar(100) NOT NULL
);

CREATE TABLE `troncal` (
  `inicial` varchar(1) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `color_hex` varchar(6) NOT NULL,
  `longitud_troncal` decimal(10,3) NOT NULL,
  `longitud_pretroncal` decimal(10,3) NOT NULL,
  `inicio` bigint(20) NOT NULL,
  `fin` bigint(20) NOT NULL
);

CREATE TABLE `via` (
  `nombre` varchar(100) NOT NULL
);

CREATE TABLE `zona` (
  `nombre` varchar(100) NOT NULL,
  `sector` bigint(20) NOT NULL
);

-- Tablas de rompimiento

CREATE TABLE `limites` (
  `zona` bigint(20) NOT NULL,
  `via` bigint(20) NOT NULL
);

CREATE TABLE `transferencia` (
  `troncal` bigint(20) NOT NULL,
  `transferencia` bigint(20) NOT NULL,
  `estacion` bigint(20) NOT NULL
);

CREATE TABLE `zona_troncal` (
  `troncal` bigint(20) NOT NULL,
  `zona` bigint(20) NOT NULL
);