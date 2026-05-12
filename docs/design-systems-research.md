# 主流 Design System 调研

## 调研目的

梳理主流 Design System（设计系统）的来源、技术实现、适用场景和选型参考，为后续主题系统、组件库选型和自研设计体系提供参考。

## 规范参考框架

自研 Web 组件库或 Design System 时，不建议只参考单一设计体系。更稳妥的方式是按规范层级拆解：用成熟 Design System 参考产品体验，用组件库参考 API 和工程落地，用标准规范约束 Design Token（设计令牌）和 a11y（无障碍访问）。

| 参考类型 | 优先参考 | 主要价值 |
| --- | --- | --- |
| 国际通用 Design System | Material Design、Carbon、Fluent、Spectrum、Polaris、Atlassian Design System、GOV.UK Design System | 视觉语言、组件规范、交互模式、内容设计、可访问性 |
| 企业级组件库 | Ant Design、Arco Design、Element Plus、Naive UI、MUI、Chakra UI、Mantine | 组件 API、主题系统、表单表格、工程化实现 |
| Headless / 底层组件 | Radix UI、Headless UI、Base UI、Ark UI、Reka UI | 复杂组件行为、键盘交互、a11y、可组合性 |
| Design Token 标准 | W3C Design Tokens Community Group、Style Dictionary、Tokens Studio、Ant Design Token、Carbon Tokens | token 分层、跨端输出、主题切换、多品牌 |
| 无障碍规范 | WCAG 2.2、WAI-ARIA APG、Inclusive Components、GOV.UK Accessibility | 对比度、语义结构、焦点管理、键盘操作、错误提示 |
| 平台规范 | Apple HIG、Material Design、Fluent Design | iOS、Android、桌面端和 Web 的平台一致性 |
| 内容设计 | Microsoft Writing Style Guide、Google Developer Documentation Style Guide、Atlassian Content Design、GOV.UK Content Design、Polaris Content | 按钮文案、错误提示、空状态、表单标签、帮助文本 |

推荐的 Design Token 分层：

| 层级 | 示例 | 用途 |
| --- | --- | --- |
| Primitive Token（原始令牌） | `blue-500`、`gray-100`、`spacing-4`、`font-size-14` | 基础色阶、尺寸、排版原子值 |
| Semantic Token（语义令牌） | `color-primary`、`color-bg-page`、`color-text-secondary`、`color-border-default` | 表达业务和界面语义，屏蔽原始值变化 |
| Component Token（组件令牌） | `button-primary-bg`、`button-height-md`、`input-border-focus`、`table-header-bg` | 控制组件内部视觉细节，支持组件级定制 |

每个组件规范至少应覆盖：

| 维度 | 应说明内容 |
| --- | --- |
| 使用规则 | 组件用途、何时使用、何时不使用 |
| 结构与状态 | 组成部分、尺寸、变体、default / hover / active / focus / disabled / loading 等状态 |
| API | props、events、slots、受控 / 非受控模式、扩展点 |
| Token | 使用哪些 semantic token 和 component token，是否支持主题覆盖 |
| 交互 | 鼠标、键盘、触摸、焦点流转和反馈规则 |
| a11y | HTML 语义、ARIA、键盘操作、焦点管理、错误提示关联 |
| 国际化 | 文案长度、RTL（从右到左）布局、日期时间、数字格式 |
| 响应式 | 移动端、桌面端、容器宽度变化和信息密度 |
| 质量标准 | 单元测试、交互测试、视觉回归、文档示例、边界场景 |

以 Button（按钮）为例，基础规范应包含：

| 项 | 建议 |
| --- | --- |
| 用途 | 触发即时操作，避免承载导航或纯展示语义 |
| 变体 | `primary`、`secondary`、`danger`、`ghost`、`link` |
| 尺寸 | `sm`、`md`、`lg`，高度和横向 padding 来自 component token |
| 状态 | default、hover、active、focus-visible、disabled、loading |
| 交互 | 原生 `button` 优先；Enter / Space 可触发；loading 时避免重复提交 |
| a11y | 非原生按钮必须补齐 `role="button"`、`tabindex` 和键盘事件；禁用态区分 `disabled` 与 `aria-disabled` |
| Token | `button-primary-bg`、`button-primary-text`、`button-height-md`、`button-radius` |

企业级 Web 组件库建议优先组合参考：

| 目标 | 推荐组合 |
| --- | --- |
| 国内中后台 | Ant Design、Arco Design、Element Plus、Naive UI |
| Vue 组件库实现 | Element Plus、Naive UI、Ant Design Vue、TDesign Vue Next、Reka UI |
| 主题系统 | W3C Design Tokens、Style Dictionary、Ant Design Token、Carbon Tokens、CSS Variables |
| 复杂交互组件 | Radix UI、WAI-ARIA APG、Headless UI、Ark UI |
| 可访问性基线 | WCAG 2.2、WAI-ARIA APG、Carbon、Spectrum、GOV.UK |
| 内容和表单体验 | GOV.UK、Polaris、Atlassian Design System |

常用官方入口：

| 资源 | 地址 |
| --- | --- |
| Material Design | https://m3.material.io/ |
| Carbon Design System | https://carbondesignsystem.com/ |
| Fluent Design System | https://fluent2.microsoft.design/ |
| Atlassian Design System | https://atlassian.design/ |
| Shopify Polaris | https://polaris.shopify.com/ |
| Adobe Spectrum | https://spectrum.adobe.com/ |
| Ant Design | https://ant.design/ |
| Arco Design | https://arco.design/ |
| Element Plus | https://element-plus.org/ |
| Radix UI | https://www.radix-ui.com/ |
| WCAG 2.2 | https://www.w3.org/TR/WCAG22/ |
| WAI-ARIA APG | https://www.w3.org/WAI/ARIA/apg/ |
| Design Tokens Community Group | https://design-tokens.github.io/community-group/ |
| Style Dictionary | https://amzn.github.io/style-dictionary/ |

## 品牌级 Design System

| Design System | 来源 | 技术实现 / 组件库 | 特点 |
| --- | --- | --- | --- |
| Material Design | Google | MUI、Angular Material、Material Web、Vuetify | 全球主流设计系统，规范完整，覆盖 Web、Android、iOS |
| Fluent Design | Microsoft | Fluent UI | 微软生态，适合企业软件、Office 风格产品 |
| Carbon Design System | IBM | Carbon React、Carbon Web Components | 企业级、数据密集型、可访问性强 |
| Polaris | Shopify | Polaris React | 电商后台和商家工具场景强 |
| Spectrum | Adobe | React Spectrum、Spectrum Web Components | 创意工具、专业软件、可访问性优秀 |
| Lightning Design System | Salesforce | SLDS、Lightning Web Components | CRM、企业 SaaS 场景 |
| Atlassian Design System | Atlassian | Atlaskit、Atlassian Design | 协作工具、项目管理、企业产品，官网：https://atlassian.design |
| Primer | GitHub | Primer CSS、Primer React | GitHub 自身产品设计体系 |
| Ant Design | 蚂蚁集团 | Ant Design React、Ant Design Vue、NG-ZORRO | 国内中后台事实标准之一 |
| Arco Design | 字节跳动 | Arco React、Arco Vue | 企业级后台，主题定制能力强 |
| Semi Design | 抖音 / 字节 | Semi React | 内容平台、企业后台，设计感较现代 |
| TDesign | 腾讯 | React、Vue、MiniProgram、Web Components | 腾讯体系，多框架、多端覆盖 |
| WeUI | 微信 | H5、小程序 | 微信生态官方设计体系 |
| Apple Human Interface Guidelines | Apple | UIKit、SwiftUI | iOS / macOS 官方交互与视觉规范 |
| SAP Fiori | SAP | UI5、UI5 Web Components | ERP、企业管理系统 |
| GOV.UK Design System | 英国政府 | GOV.UK Frontend | 政务系统，可访问性和表单体验强 |
| U.S. Web Design System | 美国政府 | USWDS | 政府网站标准化设计系统 |
| NHS Design System | 英国 NHS | NHS Frontend | 医疗公共服务场景 |

## Apple Human Interface Guidelines

Apple Human Interface Guidelines（苹果人机界面指南，简称 HIG）是 Apple 官方设计规范，覆盖 iOS、iPadOS、macOS、watchOS、tvOS、visionOS 等平台。它不是传统意义上的 Web 组件库，而是 Apple 生态的交互、视觉、布局、动效、输入方式和平台体验规范。

| 维度 | 内容 |
| --- | --- |
| 来源 | Apple |
| 覆盖平台 | iOS、iPadOS、macOS、watchOS、tvOS、visionOS |
| 技术实现 | UIKit、SwiftUI、AppKit、WatchKit、RealityKit |
| 核心关注 | 清晰性、顺应性、深度感、一致性、直接操作 |
| 典型场景 | 原生 Apple 生态应用、跨平台产品的 Apple 平台适配 |
| 参考价值 | 平台体验、交互模式、动效、系统控件、适配规范 |

Apple HIG 和其他设计系统的差异：

| 体系 | 更偏向 |
| --- | --- |
| Apple HIG | 平台体验规范 |
| Material Design | 跨平台视觉与交互规范 |
| Fluent Design | 企业软件和微软生态体验 |
| Ant Design | 中后台产品设计规范 |
| Carbon | 企业级复杂系统设计规范 |

## Atlassian Design System

Atlassian Design System 是 Atlassian 官方设计系统，官网为 https://atlassian.design。它服务于 Jira、Confluence、Trello、Bitbucket 等协作与研发管理产品，重点关注团队协作、任务流、信息密度、权限状态、通知反馈和复杂业务流程。

| 维度 | 内容 |
| --- | --- |
| 来源 | Atlassian |
| 官网 | https://atlassian.design |
| 代表产品 | Jira、Confluence、Trello、Bitbucket、Atlassian Admin |
| 技术实现 | Atlaskit、Design Tokens（设计令牌）、React 组件生态 |
| 核心场景 | 项目管理、知识协作、研发流程、企业协同、权限与工作流 |
| 参考价值 | 信息架构、复杂表单、任务状态、导航体系、协作体验、可访问性 |

Atlassian Design System 对自研中后台和协作类产品很有参考价值，尤其适合研究：

| 研究方向 | 参考价值 |
| --- | --- |
| 信息密度 | 如何在复杂页面中保持可读性和层级清晰 |
| 导航体系 | 项目、空间、组织、个人工作区之间的导航关系 |
| 状态表达 | Issue（问题）、Task（任务）、Workflow（工作流）等状态设计 |
| 协作反馈 | 评论、提及、通知、权限、共享等协作体验 |
| Design Token | 颜色、间距、字体、阴影和状态变量的系统化管理 |
| 可访问性 | 企业级产品中的键盘操作、语义结构和辅助技术支持 |

如果要做 Web 主题系统，Apple HIG 的价值不是直接复用组件库，而是参考间距、层级、留白、直接操作、即时反馈、动效节奏、Light / Dark Mode（明暗模式）、可访问性、设备尺寸适配和系统级一致性体验。

## 开源 / 组件库型 Design System

| Design System | 技术栈 | 特点 |
| --- | --- | --- |
| shadcn/ui | React + Tailwind CSS + Radix UI | 复制源码式组件，适合自定义设计系统 |
| Radix UI | React | Headless UI（无样式组件），可访问性基础好 |
| Base UI | React | MUI 团队推出的无样式组件基础库 |
| Headless UI | React / Vue | Tailwind 官方无样式组件 |
| Ark UI | React / Vue / Solid / Svelte | Chakra 团队跨框架 Headless 组件库 |
| Chakra UI | React | 主题系统好，适合 SaaS 产品 |
| Mantine | React | 组件丰富，Hooks（钩子函数）多，适合应用开发 |
| Evergreen | React | Segment 出品，企业应用风格 |
| Blueprint | React | 数据密集型后台和工具型产品 |
| PrimeReact / PrimeVue / PrimeNG | React / Vue / Angular | 组件覆盖全，表格能力强 |
| PatternFly | React | Red Hat 企业级产品设计系统 |
| Grommet | React | 响应式、可访问性较好 |
| Shoelace | Web Components | 框架无关，适合跨技术栈 |
| FAST | Web Components | 微软 Web Components 设计系统基础 |
| Vaadin | Web Components / Java | 企业级 Web App 组件 |
| UI5 Web Components | Web Components | SAP 生态 Web Components |
| Clarity | Angular / Web Components | VMware 企业级设计系统 |
| Elastic UI | React | Elastic 产品体系，数据和搜索场景强 |

## 国际大厂 Design System

| Design System | 来源 | 特点 |
| --- | --- | --- |
| Material Design | Google | 跨平台设计规范完整，覆盖颜色、排版、动效、组件、可访问性 |
| Fluent Design | Microsoft | 微软生态，适合企业软件、办公软件、桌面感 Web 应用 |
| Carbon Design System | IBM | 企业级、数据密集型、可访问性强 |
| Spectrum | Adobe | 创意工具、专业软件体验，可访问性体系成熟 |
| Polaris | Shopify | 电商后台、商家管理工具场景强 |
| Lightning Design System | Salesforce | CRM、企业 SaaS（软件即服务）场景 |
| Atlassian Design System | Atlassian | Jira、Confluence 这类协作工具体验，官网：https://atlassian.design |
| Primer | GitHub | GitHub 自身产品设计体系，适合开发者工具 |
| SAP Fiori | SAP | ERP（企业资源计划）、企业管理系统 |
| Elastic UI | Elastic | 搜索、数据分析、可视化平台 |
| PatternFly | Red Hat | 企业级云平台、运维平台 |
| Carbon for AI | IBM | IBM 针对 AI 产品体验的扩展设计指导 |

## 国内常见 Design System

| Design System | 来源 | 技术实现 | 适合场景 |
| --- | --- | --- | --- |
| Ant Design | 蚂蚁集团 | React、Vue、Angular 生态 | 中后台、企业系统、金融 |
| Arco Design | 字节跳动 | React、Vue | 企业后台、B 端系统 |
| Semi Design | 抖音 / 字节 | React | 内容平台、运营后台 |
| TDesign | 腾讯 | React、Vue、小程序、Web Components | 多端业务、腾讯生态 |
| Element / Element Plus | 饿了么社区 | Vue 2 / Vue 3 | Vue 中后台 |
| Naive UI | 图森未来社区 | Vue 3 | Vue 3 工具型产品 |
| Vant | 有赞 | Vue / 小程序 | 移动 H5、电商业务 |
| NutUI | 京东 | Vue / Taro | 移动端、多端、小程序 |
| WeUI | 微信 | H5 / 小程序 | 微信生态页面 |

## 政府 / 公共服务 Design System

| Design System | 来源 | 特点 |
| --- | --- | --- |
| GOV.UK Design System | 英国政府 | 政务系统标杆，可访问性、表单体验强 |
| U.S. Web Design System | 美国政府 | 美国政府网站标准化设计体系 |
| NHS Design System | 英国 NHS | 医疗公共服务场景 |
| Australian Government Design System | 澳大利亚政府 | 政府服务网站设计规范 |
| Canada.ca Design System | 加拿大政府 | 政府信息服务体验 |
| Singapore Government Design System | 新加坡政府 | 政务数字服务规范 |

## 金融 / 企业服务 Design System

| Design System | 来源 | 特点 |
| --- | --- | --- |
| Goldman Sachs Design System | Goldman Sachs | 金融机构内部体验体系 |
| Morningstar Design System | Morningstar | 金融数据和投资产品 |
| Backstage Design System | Spotify | 开发者门户、内部平台 |
| Shopify Polaris | Shopify | 商家后台、电商 SaaS |
| Zendesk Garden | Zendesk | 客服系统、企业 SaaS |
| ServiceNow Design System | ServiceNow | 企业工作流和 IT 服务管理 |

## 开发者工具 / 技术平台 Design System

| Design System | 来源 | 特点 |
| --- | --- | --- |
| GitLab Pajamas | GitLab | DevOps（开发运维一体化）平台 |
| GitHub Primer | GitHub | 开发者平台、代码协作 |
| Backstage | Spotify | 内部开发者门户 |
| Vercel Geist | Vercel | 极简、现代、开发者产品风格 |
| Linear Design System | Linear | 高质感协作工具、项目管理产品 |
| Railway / Supabase 风格体系 | 社区参考 | 开发者工具类产品视觉参考价值高 |

## Web Components / 跨框架 Design System

| Design System | 来源 | 特点 |
| --- | --- | --- |
| Shoelace | Web Components | 框架无关组件库，适合多技术栈 |
| FAST | Microsoft | Web Components 设计系统基础 |
| Vaadin | Vaadin | 企业级 Web App 组件 |
| UI5 Web Components | SAP | SAP 生态 Web Components |
| Spectrum Web Components | Adobe | Adobe Spectrum 的 Web Components 实现 |
| Lion | ING | 企业级 Web Components 基础库 |
| Material Web | Google | Material Design 的 Web Components 实现 |

## 自研组件库常参考

| Design System / Library | 技术栈 | 价值 |
| --- | --- | --- |
| Radix UI | React | Headless UI（无样式组件）和可访问性基础 |
| Base UI | React | MUI 团队的新一代无样式组件基础 |
| Headless UI | React / Vue | Tailwind 官方无样式组件 |
| Ark UI | React / Vue / Solid / Svelte | 跨框架 Headless 组件 |
| Zag | 多框架 | 基于状态机的组件交互逻辑 |
| shadcn/ui | React / Tailwind | 复制源码式组件，适合自定义设计系统 |
| Reka UI | Vue | Vue 生态 Headless UI 基础组件 |

## 按场景推荐

| 场景 | 推荐 |
| --- | --- |
| 全球通用产品 | Material Design |
| 企业办公软件 | Fluent Design |
| 数据密集型企业系统 | Carbon、Blueprint、Ant Design |
| 电商后台 | Polaris、Ant Design |
| 创意 / 专业工具 | Spectrum |
| CRM / 企业 SaaS | Lightning、PatternFly、Carbon |
| 国内中后台 | Ant Design、Arco Design、Semi Design、TDesign |
| Vue 中后台 | Element Plus、Naive UI、Ant Design Vue、TDesign Vue Next |
| 多端统一 | TDesign、Ionic、Material Design |
| 政务 / 公共服务 | GOV.UK Design System、USWDS |
| 自研 Design System | Radix UI、Base UI、Headless UI、Ark UI、shadcn/ui |
| 颜色体系 / Token | Material Design、Ant Design、Carbon、TDesign |
| 可访问性 | Spectrum、Carbon、GOV.UK、Radix UI |
| 跨平台体验 | Material Design、Apple HIG、Fluent Design |
| Web 组件架构 | Radix UI、Base UI、Ark UI、Shoelace |
| 政务 / 表单体验 | GOV.UK、USWDS、NHS |
| 开发者工具体验 | Primer、Pajamas、Geist、Linear |

## 主题系统研究优先级

如果目标是研究颜色主题、Design Token（设计令牌）和组件库主题架构，优先看以下设计系统：

| 优先级 | Design System | 研究价值 |
| --- | --- | --- |
| 1 | Material Design | 规范完整，颜色、排版、状态、动效都有体系 |
| 2 | Ant Design | Token 分层清晰，适合中后台主题系统研究 |
| 3 | Carbon | 企业级设计系统成熟，文档严谨 |
| 4 | Fluent UI | 企业软件和桌面感交互成熟 |
| 5 | Spectrum | 可访问性和专业工具体验强 |
| 6 | TDesign | 国内多端设计系统参考价值高 |
| 7 | Radix UI + shadcn/ui | 适合研究自研组件库底层架构 |
| 8 | Polaris | 电商后台和商家工具体验成熟 |
| 9 | Primer | 开发者工具和代码协作产品参考价值高 |
| 10 | GOV.UK Design System | 政务、表单、可访问性和内容设计标杆 |

## 初步结论

如果项目面向国际化通用 Web 产品，Material Design、Fluent Design、Carbon 和 Spectrum 更值得优先研究。

如果项目面向国内企业中后台，Ant Design、Arco Design、Semi Design 和 TDesign 更贴近实际业务场景。

如果目标是自研 Design System，建议重点研究 Design Token（设计令牌）、CSS Variables（CSS 变量）、Headless UI（无样式组件）和组件状态机模型，可参考 Radix UI、Base UI、Headless UI、Ark UI、Zag 和 shadcn/ui。
