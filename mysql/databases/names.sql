-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema users_schema
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema dojos_and_ninjas_schema
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema twitter
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema books_schema
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema friendships_schema
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema names
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema names
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `names` DEFAULT CHARACTER SET utf8mb3 ;
USE `names` ;

-- -----------------------------------------------------
-- Table `names`.`names`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `names`.`names` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
