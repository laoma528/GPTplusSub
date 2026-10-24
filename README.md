# ChatGPT 订阅与充值选择指南

这个仓库用于整理 ChatGPT 订阅方式、支付问题和第三方充值服务的使用说明。主要读者是想开通订阅、但对付款条件和不同渠道不熟悉的中文用户。

**项目状态：基础建设中。** [阅读指南首页](docs/index.html)已经写入仓库；GitHub Pages 尚未启用，正式服务网址与品牌名称待确认。

## 从哪里开始

| 想解决的问题 | 页面 |
| --- | --- |
| 先比较官网、应用商店和第三方服务 | [订阅方式怎么选](docs/index.html) |
| 想自己订阅 | [自己订阅前要核对什么](docs/self-subscribe.html) |
| 考虑第三方服务 | [怎样判断代充服务](docs/third-party.html) |
| 查找后续写作参考 | [参考资料索引](research/sources.md) |

ChatGPT 订阅与 OpenAI API 分别计费。第三方充值服务也不是 OpenAI 官方服务。具体支付资格、套餐和可用功能，请以账号结算页及 [OpenAI 帮助中心](https://help.openai.com/)当前说明为准。

## 内容计划

先把读者最常问的三件事写清楚：能否自行订阅、第三方服务究竟交付什么、付款失败后怎么处理。以后再扩展套餐对比、续费与取消、订单和售后、常见误区。选题及发布检查项见 [内容路线图](planning/content-plan.md)。

## 本地预览与 Pages

`docs/` 是不依赖构建工具的静态网站。在仓库根目录运行 `python -m http.server 8000 -d docs`，然后打开 `http://localhost:8000/`。

上传到 `main` 后，仓库管理员可在 **Settings → Pages → Build and deployment** 选择 **Deploy from a branch**，分支 `main`、目录 `/docs`。预期地址为 `https://laoma528.github.io/GPTplusSub/`；只有 Pages 部署成功并访问验证后才算上线。

## 边界

本仓库是独立信息项目，与 OpenAI 没有合作、授权或隶属关系。请勿通过 Issue 提交账号凭证或订单个人信息。内容允许参考公开资料的主题与信息结构，但文章、图片和图表需自行创作，引用处保留来源链接。

