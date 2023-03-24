# 比赛推送爬虫建设

这个仓库是比赛推送爬虫建设的一部分，主要用于爬取比赛信息并存储至数据库。

项目设置了每周三和周六的中午，爬取最近比赛信息，存储至数据库。

## 项目结构

docs：文档目录

docs/dev：开发文档

docs/guide：使用文档

internal：内部包

internal/pkg：内部包, 这里面的模块通常是一些 util 

internal/store：数据库操作

model：数据库模型

deployments：部署文件

configs：配置文件。**特别说明**：这里面应当新建一个 config.yaml 文件，用于存储数据库的连接信息，格式如下：

```yaml
db:
  host: localhost
  port: 3306
  user: root
  password: xxxxxxx
  name: xxxxxxx
```

这一部分交给 运维同学 来填写。

## 项目使用

```bash
python main.py
```

不需要你怎么使用它

## 项目开发

详见开发文档