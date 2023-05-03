CREATE DATABASE IF NOT EXISTS xlab_comp_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

use xlab_comp_db;

CREATE TABLE IF NOT EXISTS `comp` (
    `name` VARCHAR(100) NOT NULL,
    `url` VARCHAR(200) NOT NULL UNIQUE,
    `start_time` DATETIME,
    `end_time` DATETIME,
    `location` VARCHAR(100),
    `organizer` VARCHAR(100),
    `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `checked` INT NOT NULL DEFAULT 0,
    PRIMARY KEY (`url`),
    INDEX `comp_create_time` (`create_time`)
) DEFAULT CHARSET=utf8mb4;