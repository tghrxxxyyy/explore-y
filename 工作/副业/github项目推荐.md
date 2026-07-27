# 工作 · 副业（程序员专属）

> 程序员的核心资产是「能把想法变成软件」。本文梳理适合程序员的副业方向，并精选 **GitHub 开源项目**作为弹药库。
> 下列星标数、简介、许可证均于 **2026-07** 通过 GitHub API 实时抓取；星标会持续变化，以仓库当前数据为准。

## 一、为什么程序员适合搞副业
- 边际成本低：写一次可卖多次（模板、SaaS、课程）。
- 全球市场：英语 + 代码即可触达海外用户。
- 自动化能力强：能用脚本替代重复劳动。
- 起步轻：一台电脑 + 云服务商即可开工。

## 二、六大副业方向（配项目索引）
1. **独立开发 / SaaS**：做一个解决小痛点的 Web 工具，订阅制收费。→ 灵感库见 `awesome-indie`、`awesome-indie-cn`、`indie-hacker-tools`。
2. **浏览器插件 / 小程序**：刚需小工具，广告或买断变现。
3. **技术内容创作**：博客、公众号、视频、电子书、付费专栏。→ 素材见 `build-your-own-x`、`developer-roadmap`、`free-programming-books`。
4. **开源捐赠 / GitHub Sponsors**：维护受欢迎的项目获得赞助。→ 入口见 `awesome`、`awesome-selfhosted`。
5. **自托管服务变现**：帮人部署运维（参考 `coolify`、`awesome-selfhost`）。
6. **接外包 / 技术咨询 / 培训**：在平台或圈子接项目，做企业内训。→ 工具见 `n8n`、`uptime-kuma`。

## 三、GitHub 开源项目推荐（直接能用）

> 按「副业用途」分组，每个项目含实时星标、简介、语言/许可证、对副业的价值与用法。

### 🚀 独立开发 / 出海灵感

#### [`mezod/awesome-indie`](https://github.com/mezod/awesome-indie) ⭐ ~11.6k
- **简介**：面向独立开发者「如何赚钱」的资源合集（工具、案例、收入分享、社区）。
- **语言 / 许可证**：列表类（未声明标准 SPDX，引用请保留出处）。
- **对副业的价值**：找方向、找对标、看别人怎么变现的最佳入口；适合用来列「灵感清单」做内容。
- **怎么用**：按分类扫一遍，挑 3 个和你技能匹配的方向做 MVP。

#### [`kuaijierun/awesome-indie-cn`](https://github.com/kuaijierun/awesome-indie-cn) ⭐ 仓库已迁移（原 `yrzx404/awesome-indie-cn`，星标未随迁移保留）
- **简介**：独立开发商赚钱资源合集（中文），汇总国内独立开发者的工具、圈子、收款、案例。
- **语言 / 许可证**：列表类（未声明标准 SPDX）。
- **对副业的价值**：中文语境下最实用的独立开发赚钱资源全集，省去信息差。
- **怎么用**：配合上面的英文版对照看，重点参考「收款/合规/出海」板块。

#### [`weijunext/indie-hacker-tools`](https://github.com/weijunext/indie-hacker-tools) ⭐ ~7.9k
- **简介**：收录独立开发者出海技术栈和工具（框架、部署、支付、分析、增长）。
- **语言 / 许可证**：列表类（未声明标准 SPDX）。
- **对副业的价值**：直接给你一套「从 0 到 1 出海」的工具清单，少踩坑。
- **怎么用**：按里面的技术栈搭 MVP（如 Next.js + 某部署平台 + Stripe/Paddle）。

### 🛠 练手与内容素材（提升硬实力、写文章）

#### [`codecrafters-io/build-your-own-x`](https://github.com/codecrafters-io/build-your-own-x) ⭐ ~531k
- **简介**：通过从零复刻你喜欢的 технологии（Redis、Docker、Git、数据库……）来精通编程。
- **语言 / 许可证**：Markdown 列表（仓库未声明标准许可证）。
- **官网**：https://codecrafters.io
- **对副业的价值**：最好的「硬实力 + 技术文章素材」来源；每复刻一个组件就是一篇爆款博客。
- **怎么用**：挑 1 个和你方向相关的（如 Git/HTTP），边做边写系列文章，沉淀为付费内容。

#### [`buhe/build-your-own-x-zh`](https://github.com/buhe/build-your-own-x-zh) ⭐ ~423
- **简介**：`build-your-own-x` 的简体中文版，降低阅读门槛。
- **语言 / 许可证**：列表类（未声明标准 SPDX）。
- **对副业的价值**：英文吃力时的中文入口，同样可做中文教程素材。

#### [`nilbuild/developer-roadmap`](https://github.com/nilbuild/developer-roadmap) ⭐ ~362k（原 `kamranahmedse/developer-roadmap`，已迁移至 nilbuild 组织）
- **简介**：交互式成长路线图、指南与教育内容，帮开发者规划职业路径（前端/后端/DevOps 等）。
- **语言 / 许可证**：TypeScript（路线图内容通常为 CC-BY-NC-SA，商用/转载需注意）。
- **官网**：https://roadmap.sh
- **对副业的价值**：做教程/培训的内容框架；也可据此做「陪练/带练」服务。
- **怎么用**：选一条路线图，做成带作业和答疑的付费训练营。

#### [`EbookFoundation/free-programming-books`](https://github.com/EbookFoundation/free-programming-books) ⭐ ~393k
- **简介**：免费可获取的程序设计书籍大全。
- **语言 / 许可证**：Python / CC-BY-4.0。
- **对副业的价值**：做课程、写解读、整理「书单」类内容的数据源。
- **怎么用**：按主题挑书，做「X 方向必读书单 + 笔记」变现。

#### [`sindresorhus/awesome`](https://github.com/sindresorhus/awesome) ⭐ ~489k
- **简介**：各类有趣主题的 awesome 列表之总入口。
- **语言 / 许可证**：列表类 / CC0-1.0。
- **对副业的价值**：找灵感、找细分领域的资源母库。
- **怎么用**：搜你感兴趣的方向（如 awesome-ml、awesome-devtools），再深挖。

### 🖥 自托管 / 部署变现

#### [`awesome-selfhosted/awesome-selfhosted`](https://github.com/awesome-selfhosted/awesome-selfhosted) ⭐ ~308k
- **简介**：可在自己服务器上托管运行的免费软件网络服务与应用清单。
- **语言 / 许可证**：列表类（未声明标准 SPDX）。
- **官网**：https://awesome-selfhosted.net/
- **对副业的价值**：找「可自托管软件」做部署/运维副业的选型字典。
- **怎么用**：挑一类（监控/相册/笔记），提供「一键部署 + 代运维」收费服务。

#### [`wesley-archives/awesome-selfhost`](https://github.com/wesley-archives/awesome-selfhost) ⭐ 新仓库（Docker 模板集合）
- **简介**：用 Docker 容器 + 现成配置，轻松在自己服务器上部署和管理常用服务。
- **语言 / 许可证**：MIT。
- **对副业的价值**：降低运维门槛，把「帮人部署」做成标准化交付。
- **怎么用**：直接 fork 当部署脚本库，给客户做私有化部署。

#### [`coollabsio/coolify`](https://github.com/coollabsio/coolify) ⭐ ~59.6k
- **简介**：开源自托管的 PaaS，可替代 Vercel / Heroku / Netlify，一键部署静态站、数据库、全栈应用及 280+ 服务。
- **语言 / 许可证**：PHP / Apache-2.0。
- **官网**：https://coolify.io
- **对副业的价值**：接单时给客户一个「自己的 Vercel」，做托管/代运维收月费。
- **怎么用**：在自己服务器装 Coolify，对外提供「帮你上云」服务。

#### [`n8n-io/n8n`](https://github.com/n8n-io/n8n) ⭐ ~198k
- **简介**：公平代码（fair-code）的可视化工作流自动化平台，原生支持 AI，400+ 集成，可自托管或上云。
- **语言 / 许可证**：TypeScript（fair-code 许可，商用需注意条款）。
- **官网**：https://n8n.io
- **对副业的价值**：帮企业打通电商/客服/表单/通知，按项目或月费收费。
- **怎么用**：学官方模板，给小商家做「自动化顾问」。

#### [`louislam/uptime-kuma`](https://github.com/louislam/uptime-kuma) ⭐ ~89.5k
- **简介**：漂亮的自托管监控面板（ uptime 监控 + 告警）。
- **语言 / 许可证**：JavaScript / MIT。
- **官网**：https://uptime.kuma.pet
- **对副业的价值**：卖给小团队做「网站/接口可用性监控」，或作为代运维的附赠。
- **怎么用**：部署后给客户开通只读账号，收监控服务费。

#### [`immich-app/immich`](https://github.com/immich-app/immich) ⭐ ~108.9k
- **简介**：高性能自托管照片与视频管理方案（Google Photos 开源替代）。
- **语言 / 许可证**：TypeScript / **AGPL-3.0**。
- **官网**：https://immich.app
- **对副业的价值**：隐私相册私有化需求大，可做「家庭/团队相册部署」服务。
- **怎么用**：注意 AGPL——若修改后提供网络服务，需开源衍生代码。

#### [`public-apis/public-apis`](https://github.com/public-apis/public-apis) ⭐ ~452k
- **简介**：免费 API 合集（按类别整理）。
- **语言 / 许可证**：Python / MIT。
- **对副业的价值**：做产品的数据源；也可做「API 导航站」变现。
- **怎么用**：挑几个稳定免费的 API，快速验证产品想法。

### 一键对照表（星标为 2026-07 实时值）
| 项目 | 星标 | 语言 | 许可证 | 副业用途 |
| --- | --- | --- | --- | --- |
| `codecrafters-io/build-your-own-x` | ~531k | Markdown | 列表 | 练手 + 技术文素材 |
| `sindresorhus/awesome` | ~489k | — | CC0-1.0 | 灵感母库 |
| `public-apis/public-apis` | ~452k | Python | MIT | 产品数据源 |
| `EbookFoundation/free-programming-books` | ~393k | Python | CC-BY-4.0 | 教程素材 |
| `nilbuild/developer-roadmap` | ~362k | TypeScript | 内容 CC-BY-NC-SA | 培训框架 |
| `awesome-selfhosted/awesome-selfhosted` | ~308k | — | 列表 | 自托管选型 |
| `immich-app/immich` | ~108.9k | TypeScript | AGPL-3.0 | 相册部署 |
| `louislam/uptime-kuma` | ~89.5k | JavaScript | MIT | 监控面板 |
| `n8n-io/n8n` | ~198k | TypeScript | fair-code | 自动化外包 |
| `coollabsio/coolify` | ~59.6k | PHP | Apache-2.0 | 自托管 PaaS |
| `mezod/awesome-indie` | ~11.6k | — | 列表 | 独立开发灵感 |
| `weijunext/indie-hacker-tools` | ~7.9k | — | 列表 | 出海技术栈 |
| `buhe/build-your-own-x-zh` | ~423 | — | 列表 | 中文练手 |
| `wesley-archives/awesome-selfhost` | 新仓库 | — | MIT | Docker 一键部署 |

## 四、起步实操清单
1. 选一个你自己的痛点做产品（别凭空想象需求）。
2. 用 `Next.js` + `Supabase`/`Firebase` 快速出 MVP。
3. 部署到 `Vercel`/`Cloudflare Pages` 或自托管 `Coolify`，接 `Stripe`/`Paddle` 收款。
4. 去 `Product Hunt`、`Hacker News`、`Indie Hackers` 发布。
5. 写开发博客（SEO 带来长期流量），沉淀为付费内容。

## 五、避坑
- 别一开始就 All in，用业余时间验证。
- 先有 10 个真实用户，再谈扩张。
- 注意合规：数据隐私、支付税务、海外收款资质。
- 副业不影响主业与竞业协议为前提。
- **许可证红线**：`immich`/`logseq`/`AppFlowy`/`maybe` 等为 **AGPL-3.0**，修改后作为网络服务分发须开源衍生代码；`n8n` 为 fair-code，商用需看其许可条款。

> 🔗 想练手又想学原理：`codecrafters-io/build-your-own-x` 是最佳起点；想直接找变现资源：`kuaijierun/awesome-indie-cn` 最实用。
