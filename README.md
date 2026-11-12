# ProdClub 品牌官网

本分支 codex/prodclub-vip 独立维护静态品牌站，禁止整体合并至 main。

正式官网：[prodclub.vip](https://prodclub.vip/)。向本分支推送已检查的变更后，由 Cloudflare Pages 自动更新；`main` 继续维护原教程站。

本地预览：`python -m http.server 8765 --bind 127.0.0.1 --directory docs`

HTML、本地CSS、原生JavaScript；无构建依赖。品牌站使用 Cloudflare Pages 自动发布，生产分支为 `codex/prodclub-vip`，输出目录为 `docs/`。购买与交付入口：https://prodclub.ai/r/NJJU47?src=pcvip

视觉布局基于 [SaaS Design DevTools 模板](https://github.com/hannah-wright/saas-landing-page-template) 的 HTML 版适配，保留居中首屏与黑白灰配色；按用户反馈采用开放排版，去除整页外框、嵌套卡片及仿窗口流程界面。完整 MIT 许可保留在 `docs/assets/template-license.txt`。未引入模板的运行时 Tailwind CDN、远程字体和脚本切换子页机制；所有内容页保持独立静态网址。流程区用静态三步骤说明，不模拟订单或后台状态。

首页只保留一组四项核心特点，与页头、页尾采用相同的宽容器；流程、指南和问答等正文区域收窄居中，标题继续居中。官方渠道说明并入账号特点，订单售后由开通流程和帮助页面承接。

价格、周期、续费及独立客服渠道待确定。品牌站使用 GA4 免费版单独统计访问、来源和购买按钮点击，与原教程站区分；`service_click` 只是导流点击，不代表付款或订单。统计会使用第一方 Cookie 区分访客和会话，仅在 `prodclub.vip` 正式域启用，本地及部署预览不启用。

`docs/assets/analytics.js` 接收本地点击事件；发送规范页面地址前去掉查询参数与片段，不发送 Session、密码、邮箱或订单资料。相关说明见隐私页。

Cloudflare 构建命令为 `python scripts/check-public-files.py --revision HEAD && python scripts/check-referral-links.py`，检查失败时停止发布；非生产分支暂不自动部署。正式网址采用 Cloudflare 的无扩展名路径，本地预览仍可通过对应 `.html` 文件访问。

IndexNow 使用为品牌站新生成的独立公开验证密钥，不复用旧站密钥。先发布验证文件，确认其 URL 可直接访问，再校验和提交 sitemap 中的规范网址；以下是操作命令，不代表已经完成提交：

```powershell
python scripts/seo-geo/submit-indexnow.py --sitemap --dry-run
python scripts/seo-geo/submit-indexnow.py --sitemap
```

以后可将变更网址作为参数单独提交。新增或轮换密钥时，同步验证文件的文件名与内容、脚本中的 `KEY_FILE`、`.public-files` 和 `.gitignore` 的逐项规则；发布后再提交。IndexNow 返回 200 或 202 只表示请求已收到，不保证收录。

内容日期取自真实 Git 正文变更。当前总价、周期、续费与客服信息请通过原商品及订单页面查看。

<!-- content-updated:start -->
内容更新：2026年11月8日
<!-- content-updated:end -->
