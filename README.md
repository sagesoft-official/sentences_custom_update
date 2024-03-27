# Sentences Custom Update

![version](https://img.shields.io/badge/Version-1.1.3-cyan) ![python](https://img.shields.io/badge/Python-3.8.10-blue)

bot插件扩展，用于快速更新语录库

## 如何使用

### Install

- pip install -r requirements.txt

![help](help.jpg)

## Version

- x.x.x.y x为scu版本，y为语录功能版本

## ChangeLog

### 语录库更新

- 发送语录支持图片，通过random函数随机抽取

- 修改语录合集上传的图片和其他语录一样为单独的路径避免产生未知的bug

- 十连合并为一条发送避免被风控

- 扩展楠桐语录和语录合集查询功能，支持查询占比和统计

- 楠桐语录和语录合集查询功能新增卡池

- 楠桐语录十连新增当次合计

- 楠桐语录查询新增累计抽卡次数

- 压缩楠桐语录查询的消息长度避免被风控

- 发送语录新增稀有度显示

注：该功能为实验性功能，目前可能存在超出预计的性能问题，届时可能会移除该功能

- 楠桐语录十连新增稀有度显示

注：该功能为实验性功能，目前可能存在超出预计的性能问题，届时可能会移除该功能

- 楠桐语录卡池新增总数

- 语录格式改为〔g{text["id"]}〕

- 在楠桐语录调用结束后尝试通过gc.collect()清理内存避免发生性能问题

- 楠桐语录除语录库外的path改为bot的path_config

经过短期测试如无问题其他语录将会一起适配，scu暂不确定是否适配

- 楠桐语录十连改为n抽，目前支持1抽-30抽，触发：楠桐语录.n抽 目前支持1抽-30抽

- 移除楠桐语录.n抽触发关键词，n抽触发与楠桐语录触发关键词合并，触发：楠桐语录 + n抽|单抽 目前支持1抽-30抽 例：楠桐语录30抽，楠桐语录14抽，楠桐语录单抽

n抽触发正则：([0-9]+抽|零抽|单抽|抽)

- 尝试通过延长核心超时时间修复n抽报Timeout的问题

- n抽默认上限改为50

- 新增配置上限命令，可配置n抽单次抽卡次数，默认5级以上权限才能触发，<s>该配置目前为全局配置，所有群的上限都会被修改！</s>（已修复）

- 新增简易错误码系统，可使用帮助楠桐语录查看

- 配置上限触发格式改为：楠桐语录["配置上限", "修改上限"]

- 超限警告的值改为变量方便后续更新

- 修改抽卡超限报错提示

- n抽新增触发关键词：一井|抽卡

- 修复单抽和抽卡不会触发的问题

- 楠桐语录新增单角色卡池 触发：楠桐语录[“限定”, “指定”] 角色 | 楠桐语录限定n抽 角色（角色必须为全名，可使用楠桐语录查询获取）

- 修复一个变量复用导致的bug

- 将n抽上限的键值对移到单独的配置文件避免与查询产生冲突

- 楠桐语录以用户为键新增cd，默认10s

- 配置上限改为每个群的独立配置，在第一次使用多抽且未配置上限时默认配置为50发

注：该功能为测试功能，不确定是否有奇怪的bug

- 调整了部分卡的稀有度

- 桑吉语录新增触发词：{"桑急语录", "羊驼语录"}

- 楠桐语录新增触发词：{"腩酮语录", "腩通语录", "腩桐语录", "喃酮语录", "喃铜语录", "喃通语录", "喃桐语录", "南酮语录", "南铜语录", "南桐语录", "南通语录"}

- 楠桐语录查询新增配置项 - 显示/隐藏：总数、统计、占比、卡池，触发：显示/隐藏总数 | 显示/隐藏统计 | 显示/隐藏占比 | 显示/隐藏卡池

因为需要配置文件暂时又不考虑用真寻的配置，所以楠桐语录改为了模块的形式，如果没有配置文件bot启动时会在插件目录下生成config.yml，默认为全显示

例：
楠桐语录查询 显示总数
楠桐语录 查询 隐藏总数

注：从这个版本开始要安装PyYAML依赖，已提供requirements.txt可直接安装

- 回调稀有度

- 修复了晨于曦Asahi不是N卡的bug

- 将楠桐语录抽卡上限的配置文件从json改为yaml并和config.yml合并

- config.yml路径改为bot的data路径

- 桑吉语录触发新增：桑姨语录

- 楠桐语录新增手动调整稀有度，默认需要5级权限

- 楠桐语录调整稀有度新增卡池调整，可单独指定某个人，默认需要5级权限

- 细分楠桐语录权限组，将抽卡上限、调整卡池百分比、调整角色稀有度拆分为单独的配置项

- 调整卡池百分比和角色稀有度的默认权限为6级（群管理的权限等级为5级，需要找超管修改用户的权限等级）

- 尝试修复调整指定角色卡池后查询不会去重的bug

- 楠桐语录n抽、限定n抽、查询将通过合并转发发送而不再是合并为一条发送

- 移除楠桐语录配置抽卡上限的最高限制和警告

- 优化楠桐语录限定卡池的循环代码

- 移除楠桐语录发送语录的控制台log

- 优化楠桐语录一部分bot发送的内容

- 楠桐语录限定卡池单抽上限：1000 => 500

- 楠桐语录未配置抽卡上限时触发n抽：配置为50抽并停止抽卡 => 配置为50抽并继续抽卡

- 楠桐语录限定卡池适配字典

- 修复新增字典后楠桐语录不会加载新键值对的问题

- 适配新的字典

- 楠桐语录新增用户抽卡统计

注：数据将保存在bot的data目录下db文件中

- 用户抽卡统计新增查询功能

触发：楠桐语录 统计

注：目前查询仅能查询触发该命令用户的全局抽卡数
全局抽卡数：指该用户在所有群的抽卡记录

统计时间从2023-11-01 21:40:02开始

- 楠桐语录查询结果将会按照语录数排序

- 楠桐语录查询的占比将会按照语录数排序

- 占比和统计改为从大到小排序

- 楠桐语录统计新增关键词统计

- 关键词统计作者支持字典

- 关键词统计新增占比

触发：
楠桐语录 统计 关键词

- 删除一处残留的debug代码

- 修复楠桐语录小晨含量过低的问题

现在如果单抽出的卡不是晨于曦Asahi，该卡将会有40%的概率替换为晨于曦Asahi

注：该功能可能存在性能问题

- 现在判定成功时将会发送一条消息

- 楠桐语录up卡功能扩展为列表

#### 1.1.3 | 2023.10.1

- 新增提取语录功能，支持字典

触发：提取语录 语录名称 语录作者（如果是不需要作者的语录该参数可以省略）| 提取不需要作者的语录时，将会过滤掉该语录中其余的键值对仅保留语录内容，提取需要作者的语录时，仅保留该作者的语录内容

注：提取后的文件格式为json，内容为格式化后的列表

提取无需作者的语录功能目前为测试版，可能存在未知的问题

#### 1.1.2 | 2023.9.28

- 撤回语录备份功能扩展，新增可配置的最大备份数量，通过bot的config配置，默认10

最大备份数量指的是当备份的文件数超过配置的值时，将会删除最旧的文件并备份最新的，备份文件的数量将保持为配置的值

#### 1.1.1 | 2023.9.18

- 修改还原语录备份文件的后缀

- 修复还原语录使用了其他触发器的问题

- 新增撤回语录功能

触发：撤回语录 语录名称 撤回次数（默认如果没有撤回次数将撤回1次）

该命令会将语录库撤回到上一条语录，默认会在撤回后自动重载语录，可修改bot的config配置是否启用，重载语录需求和手动重载一样

将在后续版本适配字典

#### 1.1.0 | 2023.9.17

- 新增还原语录功能

触发：还原语录 语录名称

该命令会将语录库还原到上传最后一条语录之前，默认会在还原后自动重载语录，可修改bot的config配置是否启用，重载语录需求和手动重载一样

将在后续版本适配字典

#### 1.0.16 | 2023.9.17

- 黑名单新增查询功能，无权限要求，触发：上传语录 黑名单 查询

#### 1.0.15 | 2023.9.17

- 新增黑名单，在黑名单的id将无法上传至语录，默认6级权限（注：指这个id无法被上传至语录，而不是这个id不能上传语录）

触发：上传语录 黑名单 添加/删除 作者/别名

#### 1.0.14 | 2023.9.14

- 调换字典的键值对，现在一个作者可以有多个别名了

#### 1.0.13 | 2023.9.14

- 新增查询字典，触发：上传语录 字典 查询

#### 1.0.12 | 2023.9.13

- 新增字典，目前仅在scu生效，将在后续版本中适配单独语录

- 字典扩展：[回复] 上传语录 字典 作者 该命令将会把回复的人的群id作为别名

触发：上传语录 字典 作者（保存在语录中的名字） 别名 | 该命令将会为指定的作者添加一个别名，目前仅在上传语录时可直接写别名而不需要写全名

#### 1.0.11 | 2023.9.4

- 通过回复上传楠桐语录和语录合集时支持手动指定作者

例：[回复] 上传语录 楠桐 晨于曦Asahi（如不填写作者将默认为群名称）

#### 1.0.10 | 2023.8.29 & 8.30

- 新增重载语录，触发：重载语录

用备份的语录文件替换语录系统的文件并刷新数据库后重启语录系统，一般用于手动修改语录后重载，也可用于语录系统意外崩溃后pm2未自动重启，但这种情况重载不一定有用

- 上传后重启语录系统的脚本路径与重载语录的脚本路径同步

#### 1.0.9 | 2023.7.29

- 修复通过回复上传语录时如果回复中存在空格会导致语录作者出现错误的问题

#### 1.0.8 | 2023.7.27

- 上传语录支持回复，回复不需要填写作者，默认为群名称

例外：
”小丑竟是我自己“=”桑吉Sage“
“冰蓝艾思博录”=“毕方”

- 修复因为服务器在中国大陆导致的github无法推送使bot卡死的问题，现在为每天0点推送

#### 1.0.7 | 2023.7.26

##### add：

- 上传图片支持回复 ![example1](example1.jpg)

#### 1.0.6 | 2023.7.25

##### add：

- 新增查询功能，目前可查询已收录语录列表

##### change：

-  稍微优化了一下代码并移除了未使用的变量

#### 1.0.5 | 2023.7.19

##### change:

- 移除上传语录所需的权限要求

##### fix：

- 修复在同一个进程中多次上传图片时，当前时间不刷新的问题

#### 1.0.4 | 2023.7.19

##### add:

- 上传语录初步支持上传图片，上传的图片将会按照语录分类

#### 1.0.3 | 2023.7.18

##### add:

- 成功上传语录后发送的消息内容新增语录的当前id

##### fix：

- 修复一个逻辑bug，该bug不会影响程序的执行，但会抛出一个异常从而被except捕捉

#### 1.0.2 | 2023.7.17

##### add:

- 刷新数据库通过scu触发，不再通过监测文件变动，之后应该是即时刷新（强制延迟2-5s）而不是延迟30s了

#### 1.0.1

##### add:

- 适配语录合集

#### 1.0.1

##### add:

- 适配小晨语录

#### 1.0.1 | 2023.7.6

##### add:

- 添加权限管理，上传语录现在需要5级以上权限（群管理）

##### fix:

- 修复语录不存在时只会后台报错不会提示的问题

#### 1.0.0 | 2023.7.6