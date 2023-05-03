# 比赛推送爬虫建设

这个仓库是比赛推送爬虫建设及相应的飞书机器人推送，用于爬取比赛信息并存储至数据库，定期检查数据库的更新，将其同步到飞书文档中。

项目设置了每周三和周六的中午，爬取最近比赛信息，存储至数据库。

## 项目结构

docs：文档目录

docs/dev：开发文档

docs/guide：使用文档

python: 爬虫代码

golang: 飞书机器人代码

deployments：部署文件

configs：配置文件。在此项目中，只需要填写 golang/config.yaml 下的 feishu 相关内容即可。

## 技术选型

-   语言：Python
-   数据库：MySQL

创建 database 的 sql 语句如下：

```sql
CREATE DATABASE IF NOT EXISTS xlab_comp_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

注意这里一定要指定 `utf8mb4`，否则中文无法被正确存储。

model 对应的 sql 语句如下：

```sql
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
```

我们存放了初始化使用的 init.sql 在 python/init.sql 中

-   日志库：logging
-   定时库：schedule
-   ORM：SQLAlchemy

## 部署

采用了 docker-compose 部署，部署文件在 deployments/docker-compose.yml 中。