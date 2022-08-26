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
  `date` DATE NULL,
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
  `movie_id` INT NOT NULL,
  `creator_user_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_reviews_movies_idx` (`movie_id` ASC) VISIBLE,
  INDEX `fk_reviews_users1_idx` (`creator_user_id` ASC) VISIBLE,
  CONSTRAINT `fk_reviews_movies`
    FOREIGN KEY (`movie_id`)
    REFERENCES `proyecto`.`movies` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_reviews_users1`
    FOREIGN KEY (`creator_user_id`)
    REFERENCES `proyecto`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proyecto`.`users_has_reviews`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyecto`.`users_has_reviews` (
  `user_like_id` INT NOT NULL,
  `review_id` INT NOT NULL,
  PRIMARY KEY (`user_like_id`, `review_id`),
  INDEX `fk_users_has_reviews_reviews1_idx` (`review_id` ASC) VISIBLE,
  INDEX `fk_users_has_reviews_users1_idx` (`user_like_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_reviews_users1`
    FOREIGN KEY (`user_like_id`)
    REFERENCES `proyecto`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_reviews_reviews1`
    FOREIGN KEY (`review_id`)
    REFERENCES `proyecto`.`reviews` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
