# ChatGPT 订阅与充值选择指南

这个仓库用于整理 ChatGPT 订阅方式、支付问题和第三方充值服务的使用说明。主要读者是想开通订阅、但对付款条件和不同渠道不熟悉的中文用户。

**项目状态：基础版已上线。** [阅读在线指南](https://laoma528.github.io/GPTplusSub/)。需要第三方订阅协助的读者，可在了解选择条件后前往 [ProdClub 订阅服务网站](https://prodclub.xyz/r/3F8974?src=GPTsub)查看当前商品与条款。该站公开流程涉及提交一次 Session，购买前请阅读[安全与售后说明](docs/third-party.html)。

## 从哪里开始

| 想解决的问题 | 页面 |
| --- | --- |
| 先比较官网、应用商店和第三方服务 | [订阅方式怎么选](docs/index.html) |
| 想自己订阅 | [自己订阅前要核对什么](docs/self-subscribe.html) |
| 考虑第三方服务 | [怎样判断代充服务](docs/third-party.html) |
| 查找后续写作参考 | [参考资料索引](research/sources.md) |

ChatGPT 订阅与 OpenAI API 分别计费。第三方充值服务也不是 OpenAI 官方服务。具体支付资格、套餐和可用功能，请以账号结算页及 [OpenAI 帮助中心](https://help.openai.com/)当前说明为准。

## 内容计划

先把读者最常问的三件事写清楚：能否自行订阅、第三方服务究竟交付什么、付款失败后怎么处理。以后再扩展套餐对比、续费与取消、订单和售后、常见误区。ProdClub 的商品、交付与售后细则需按真实流程继续核对；选题及发布检查项见 [内容路线图](planning/content-plan.md)。

## 本地预览与 Pages

`docs/` 是不依赖构建工具的静态网站。在仓库根目录运行 `python -m http.server 8000 -d docs`，然后打开 `http://localhost:8000/`。

页面的色彩、字体层级、留白和组件排版参考 [DESIGN-openai.md](DESIGN-openai.md)。它是设计参考，页面文案与本站身份仍保持独立。

GitHub Pages 已设为从 `main` 的 `/docs` 目录发布，地址为 <https://laoma528.github.io/GPTplusSub/>。首次构建成功，首页、两篇指南和样式文件均已返回 HTTP 200（2026-10-24）。后续更新推送到 `main` 后会重新构建。

## 边界

本仓库是独立信息项目，与 OpenAI 没有合作、授权或隶属关系。请勿通过 Issue 提交账号凭证或订单个人信息。内容允许参考公开资料的主题与信息结构，但文章、图片和图表需自行创作，引用处保留来源链接。

