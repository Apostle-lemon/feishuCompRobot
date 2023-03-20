## 技术选型

-   语言：Python
-   数据库：MySQL
    因为运维的原因，暂时不考虑使用 NoSQL

创建 database 的 sql 语句如下：

```sql
CREATE DATABASE IF NOT EXISTS xlab_race_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

注意这里一定要指定 `utf8mb4`，否则中文无法被正确存储。

model 对应的 sql 语句如下：

```sql
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
```

-   日志库：logging
-   定时库：schedule
-   ORM：SQLAlchemy