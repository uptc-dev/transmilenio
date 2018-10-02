-- David Sánchez Ruiz

--
-- Restriccion de talas
--

ALTER TABLE `estacion` ADD `id` BIGINT(20) NOT NULL AUTO_INCREMENT FIRST, ADD PRIMARY KEY (`id`);
ALTER TABLE `sector` ADD `id` BIGINT(20) NOT NULL AUTO_INCREMENT FIRST, ADD PRIMARY KEY (`id`);
ALTER TABLE `troncal` ADD `id` BIGINT(20) NOT NULL AUTO_INCREMENT FIRST, ADD PRIMARY KEY (`id`);
ALTER TABLE `via` ADD `id` BIGINT(20) NOT NULL AUTO_INCREMENT FIRST, ADD PRIMARY KEY (`id`);
ALTER TABLE `zona` ADD `id` BIGINT(20) NOT NULL AUTO_INCREMENT FIRST, ADD PRIMARY KEY (`id`);

ALTER TABLE `limites` ADD PRIMARY KEY (`zona`,`via`);
ALTER TABLE `transferencia` ADD PRIMARY KEY (`troncal`,`transferencia`,`estacion`);
ALTER TABLE `zona_troncal` ADD PRIMARY KEY (`troncal`,`zona`);

ALTER TABLE limites ADD FOREIGN KEY (zona) REFERENCES zona(id);
ALTER TABLE limites ADD FOREIGN KEY (via) REFERENCES via(id);
ALTER TABLE zona ADD FOREIGN KEY (sector) REFERENCES sector(id);
ALTER TABLE zona_troncal ADD FOREIGN KEY (troncal) REFERENCES troncal(id);
ALTER TABLE zona_troncal ADD FOREIGN KEY (zona) REFERENCES zona(id);
ALTER TABLE troncal ADD FOREIGN KEY (inicio) REFERENCES estacion(id);
ALTER TABLE troncal ADD FOREIGN KEY (fin) REFERENCES estacion(id);

ALTER TABLE estacion ADD FOREIGN KEY (troncal) REFERENCES troncal(id);
ALTER TABLE transferencia ADD FOREIGN KEY (troncal) REFERENCES troncal(id);
ALTER TABLE transferencia ADD FOREIGN KEY (transferencia) REFERENCES troncal(id);
ALTER TABLE transferencia ADD FOREIGN KEY (estacion) REFERENCES estacion(id);