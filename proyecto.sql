-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema proyecto
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema proyecto
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `proyecto` DEFAULT CHARACTER SET utf8 ;
USE `proyecto` ;

-- -----------------------------------------------------
-- Table `proyecto`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyecto`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nickname` VARCHAR(100) NULL,
  `first_name` VARCHAR(100) NULL,
  `last_name` VARCHAR(100) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proyecto`.`movies`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyecto`.`movies` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `year` YEAR NULL,
  `genre` VARCHAR(255) NULL,
  `director` VARCHAR(255) NULL,
  `country` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proyecto`.`reviews`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyecto`.`reviews` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `content` TEXT NULL,
  `rate` TINYINT(1) NULL,
  `movies_id` INT NOT NULL,
  `users_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_reviews_movies_idx` (`movies_id` ASC) VISIBLE,
  INDEX `fk_reviews_users1_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_reviews_movies`
    FOREIGN KEY (`movies_id`)
    REFERENCES `proyecto`.`movies` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_reviews_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `proyecto`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
