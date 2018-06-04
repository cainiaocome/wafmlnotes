## 任务架构图

![Markdown](http://i2.bvimg.com/596029/31e3372e61642aec.png)

## 任务技术简介

1. 训练需要的数据，由当前的waf引擎，采用规则匹配的方式，收集黑白流量日志，到kafka中保存
2. 本地训练由kafka拉取日志数据，sklearn/xgboost进行训练，确认模型的accuracy，precision，recall达到上线要求
3. 线上模型由xgboost运行，再次训练生成模型准备更新线上模型
4. 确认模型运行效率达到上线要求后，更新线上模型，前置到规则匹配的waf引擎前

## 某些行为说明

1. 机器学习模型上线后，由机器学习模型进行流量的第一次过滤，判定为攻击则立即阻断，判定为正常则由规则引擎进行二次判定
2. 规则匹配需要更新规则，新上规则与机器学习模型并列运行
3. 机器学习模型持续学习黑白流量日志，当学习到新规则之后，新规则并入旧规则
4. 目前暂定机器学习算法采用决策树算法，本地训练采用sklearn／tensorflow，线上实现采用tensorflow／spark

## 路线

1. 本地训练环境搭建，决策树算法学习和在多个环境中的实现( 90天 )
2. 黑白流量拉取，特征工程，本地训练( 60天 )
3. 线上模型模拟和测试( 30天 )
4. 上线和持续学习

### 技术选型
1. 本地 sklearn／xgboost
2. 线上 xgboost/spark
3. 6月，漏洞检测模型：sql injection/xss/lfi/rfi/directory traversal/os cmd injection/bruteforce
4. 代码管理 git/内网gitlab
5. python3
6. payload收集
