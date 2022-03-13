# X-lab 比赛推送爬虫建设

< 脚本说明文档 >

所有网站都会存在一个在 `./tmp` 文件夹下的 `.tmp` 文件，用来记录上一次更新的通知最晚日期，用来判断最新信息

如果需要重新开始爬取，则清空对应的 `.tmp` 文件即可

按照需求文档中的需求，以目标网站为单位分为四个部分

## 索引

- [x] 【会查查】   ：   `_huixx.cn_.py`
- [x] 【我爱竞赛网】   ：   `_52jingsai.com_`
- [x] 【摩课云】   ：   `_moocllege_.py`
- [x] 【赛氪】   ：   `_saikr.py`

## 必要环境

- python
- python/requests
- python/Python-bs4


## 说明

### 【会查查】使用说明

爬虫本体在`_huixx.cn_.py`中，如果Cookie失效请修改`get_huixx.cn_cookie.py`中的密码和用户名，并运行。

1. 控制 `pageMax` 的值来改变爬取网站列表页数
2. `head` 中使用有效登录 `Cookie` 才能确保获取“联系方式”信息
3. 爬得的信息会存在 `cList` 中，元素类型为 `CInfo`
  - 对应关系如下：

```python
self.url          # info msg url
self.name         # competition name
self.sTime[0]     # sign up time (begin)
self.sTime[1]     # sign up time (end)
self.cTime[0]     # competing time (begin)
self.cTime[1]     # competing time (end)
self.source       # page source
self.bsobj        # page bs4 obj
self.details      # competition details and contract information
```

### 【我爱竞赛网】使用说明


1. 控制 `pageMax[i]` 的值来改变爬取网站列表页数的最大值
  - 0 ~ 2 分别对应正在报名、准备报名、报名结束
2. 爬得的信息会存在 `cList` 中，元素类型为 `CInfo`
  - 对应关系如下：

```python
self.url            # info msg url
self.status         # competition status, 0 ~ 1 分别对应正在报名、准备报名、报名结束
self.source         # page source
self.bsobj          # page bs4 obj
self.summary        # competition summary
self.details        # competition details
```

### 【塞氪】使用说明

1. 控制 `pageMax` 的值来改变爬取网站列表页数
2. 各竞赛详细内容以html形式保存，保存路径见输出
3. 简要信息会存在 `cList` 中，元素类型为 `CInfo`
  - 对应关系如下：
```python
self.url            # info msg url
self.status         # competition status
self.sTime          # sign up time
self.cTime          # competition time
self.name           # name
```

### 【摩课云】使用说明

1. 信息存在 `cList` 中，元素类型为 `CInfo`

  - 对应关系如下：
```python
self.url            # info msg url
self.sTime          # competiotion start time
self.eTime          # competition end time
self.name           # name
```


