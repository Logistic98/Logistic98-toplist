## BlackCatのTopList

### 1. 项目简介

- 一个基于Django的信息聚合平台，使用Scrapy抓取各大主流平台的榜单资讯将其推荐给用户。

### 2. 技术选型

- MySQL数据库：使用MySQL替代Django默认的SQLite数据库。
- Django框架：使用Django与MySQL数据库交互，开发前端展示部分的服务端。
- Scrapy框架：使用Scrapy来开发网络爬虫部分。
- Bootsrtap框架：使用Bootstrap来设计响应式前端。

### 3. 使用方法

- Step1：将本项目clone到本地，然后使用`pip`命令安装`requirements.txt`里的项目依赖
- Step2：配置本地的MySQL环境，并填写`toplist\toplist\settings.example.py`的`DATABASES`信息，然后将其重命名为`settings.py`
- Step3：将`toplist\weiboscrapy\weiboscrapy\settings.example.py`重命名为`settings.py`
- Step4：在Pycharm的Terminal里运行`toplist_env\Scripts\activate`命令激活虚拟环境（停止：deactivate）
- Step5：在激活的虚拟环境里运行`python manage.py runserver`命令运行Django项目（停止：Ctrl+C）
- Step6：运行`toplist\weiboscrapy\weiboscrapy`里的`main.py`文件，使用Scrapy爬虫将资讯爬取入库
- Step7：在Chrome浏览器地址栏输入`http://127.0.0.1:8000/`，即可看到本项目运行后的结果

### 4. 搭建过程

- 本项目的完整搭建过程参见我的个人博客：[基于Django和Scrapy的信息聚合平台的设计与实现](https://www.blackcat.monster/index.php/2020/05/27/%e5%9f%ba%e4%ba%8edjango%e5%92%8cscrapy%e7%9a%84%e4%bf%a1%e6%81%af%e8%81%9a%e5%90%88%e5%b9%b3%e5%8f%b0%e7%9a%84%e8%ae%be%e8%ae%a1%e4%b8%8e%e5%ae%9e%e7%8e%b0/)
- 注：如果你在部署使用方面遇到了困难，可以参见这篇项目文档来寻找解决办法

### 5. 功能界面

[1] 首页

![](https://chevereto.blackcat.monster/images/2020/05/22/16da93f6f64605b8fb1349b4df9b3164.png)

[2] 网站导航

![](https://chevereto.blackcat.monster/images/2020/05/22/a5eafd3327f724332a3c59737a1539ab.png)

[3] 微博头条

![](https://chevereto.blackcat.monster/images/2020/05/27/9aba40eb181de91bd82b5889b6a703fa.png)

[4] 开源项目

![](https://chevereto.blackcat.monster/images/2020/05/22/7c9ff8104cced93b0fc5cb49e8ce18a1.png)

[5] 知识碎片

![](https://chevereto.blackcat.monster/images/2020/05/22/024a1cd5bd1bd4d11765bba9b167fca3.png)