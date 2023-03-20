CREATE DATABASE IF NOT EXISTS xlab_race_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

use xlab_race_db;

CREATE TABLE IF NOT EXISTS `race` (
    `name` VARCHAR(100) NOT NULL,
    `url` VARCHAR(200) NOT NULL UNIQUE,
    `start_time` DATETIME,
    `end_time` DATETIME,
    `location` VARCHAR(100),
    `organizer` VARCHAR(100),
    `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`url`),
    INDEX `race_create_time` (`create_time`)
) DEFAULT CHARSET=utf8mb4;