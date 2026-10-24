# Avarce Apple 礼品卡教程更新核验｜2026-10-24

核验对象：[Avarce/chatgpt-plus-china-guide](https://github.com/Avarce/chatgpt-plus-china-guide) 2026-10-22 更新，涉及 $19.99 内购价、$20 礼品卡、Oregon 账单地址、付款信息提示、Pockyt 库存和人民币价格。此处只记录公开资料能证明的边界，不复述操作步骤。

| 说法 | 核验结果 | 依据与边界 |
| --- | --- | --- |
| 10 月 22 日确有更新及读者反馈 | **属实** | [更新发布](https://github.com/Avarce/chatgpt-plus-china-guide/releases/tag/2026.10.22)、[当日读者评论](https://github.com/Avarce/chatgpt-plus-china-guide/issues/1#issuecomment-6343536819)和 [README 提交](https://github.com/Avarce/chatgpt-plus-china-guide/commit/1369f380c3243da37872c56d36d1ceb14ca2857e)存在。评论是单个用户自述，不是 Apple 的故障诊断。 |
| 美国区 ChatGPT iOS App 的 Plus 内购标价 $19.99 | **当前公开列表可核实** | [美国区 App Store 的 ChatGPT 页面](https://apps.apple.com/us/app/chatgpt/id6448311069)于本次核验时列出 `ChatGPT Plus $19.99`。这是列表价格，实际结算额还应以账户中的付款确认页为准。 |
| 美国 App Store 交易可能按账单地址计税 | **方向正确** | [Apple 开发者交易税字段](https://developer.apple.com/help/app-store-connect/reference/reporting/transaction-tax-report-fields)按客户账单地址记录州、市等税务字段；[Oregon 税务局](https://www.oregon.gov/dor/programs/businesses/Pages/Sales-Tax.aspx)说明该州没有一般销售税。因此某些其他地区的税使 $19.99 超过 $20 余额，逻辑上可能成立。Apple 未确认该读者的具体提示就是税费造成。 |
| “账单州不是 Oregon 就会加税” | **不准确** | Oregon 并非唯一无一般销售税的州；[Delaware 税务部门](https://revenue.delaware.gov/business-tax-forms/doing-business-in-delaware/step-4-gross-receipts-taxes/)也说明该州无州或地方销售税。具体税额还取决于真实交易和地址。 |
| “把地址改成 Oregon 即可，不用绑卡” | **不能作为通用承诺** | 该仓库记录了一位读者改地址后付款成功；但 [Apple 官方说明](https://support.apple.com/en-us/118245)指出，即使用账户余额，某些购买仍可能要求留存信用卡。[Apple 更改账户地区指南](https://support.apple.com/en-us/118283)也提示可能需要新地区有效的付款方式。应填写真实、适用的账单资料，不能建议中国大陆读者借用不真实的 Oregon 地址绕过支付或税务要求。 |
| Pockyt 于 10 月 22 日仍在售 | **有作者当日截图，无法独立确认实时库存** | README 的 [Pockyt 段落](https://github.com/Avarce/chatgpt-plus-china-guide#pockyt-status)附有 10 月 22 日面额截图；[Pockyt 商品链接](https://shop.pockyt.io/goodsDetail/9WLYdh2/Apple%20Gift%20Card%20US/all)目前仍有公开页面入口，但本轮只读工具未取得实时库存或成功结账状态，不能断言今天可买。 |
| 7 月实付 ¥135.98、10 月 13 日页面 ¥134.44 | **作者历史记录，非当前报价** | README 的历史截图与表格支持“作者当时看到/支付的金额”，无法独立核查交易，且汇率、折扣和供应会变化。SEO 页面不应把 ¥134.44 写成固定价格。 |

## 给本站内容的安全表述

“美国区 App Store 当前公开列出 ChatGPT Plus 内购价 $19.99。Apple 礼品卡可进入相应地区的 Apple 账户余额，但实际付款总额可能受税费影响；即使余额充足，Apple 对某些购买也可能要求账户留有付款方式。购买礼品卡前，先核对账户地区、真实账单信息、订阅确认页总额及商家退款规则。第三方截图只代表当时的购买经历，不保证同样条件下可复现。”

本次按项目规则先运行 `ego-browser skill`，并尝试使用 ego lite 查看 Pockyt 实时货架；普通权限无法连接 bootstrap，提升权限后本地状态写入遇到 `EPERM`，未完成页面核验。不能把可访问的商品 URL 当作“有库存/可结账”的证据。
