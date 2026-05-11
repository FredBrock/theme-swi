# GitHub 热门 UI 组件库调研

## 调研目的

梳理 GitHub 上常见且活跃的 UI 组件库（UI component libraries，界面组件库），为后续项目选型提供参考。

## React 生态

| 组件库 | 特点 | 适合场景 |
| --- | --- | --- |
| shadcn/ui | 基于 Radix UI + Tailwind CSS，复制源码到项目中，定制性强 | 现代 SaaS、后台、产品原型 |
| MUI / Material UI | Google Material Design 风格，组件完整，生态成熟 | 企业后台、中大型 React 项目 |
| Ant Design | 中后台能力强，表单、表格、布局组件成熟 | 管理平台、企业系统 |
| Chakra UI | API 简洁，主题系统友好，可访问性较好 | 快速开发、设计系统原型 |
| Mantine | 组件丰富，Hooks（钩子函数）多，开发体验好 | Web 应用、Dashboard（仪表盘） |
| Radix UI | Headless UI（无样式组件），可访问性强 | 自定义设计系统 |
| Headless UI | Tailwind 官方团队出品，无样式基础组件 | Tailwind 项目、自定义 UI |
| HeroUI / NextUI | 现代视觉风格，适合快速做漂亮界面 | Landing page（落地页）、应用界面 |
| Blueprint | 偏复杂、数据密集型界面 | 工具型后台、数据平台 |

## Vue 生态

| 组件库 | 特点 | 适合场景 |
| --- | --- | --- |
| Element Plus | Vue 3 主流中后台组件库 | 管理后台、企业系统 |
| Vuetify | Material Design 风格，组件较全 | Vue 应用、后台系统 |
| Naive UI | Vue 3，TypeScript（类型脚本）支持好，风格现代 | 中后台、工具类应用 |
| Ant Design Vue | Ant Design 的 Vue 实现 | 企业后台、表单系统 |
| Quasar | 一套代码支持 Web、移动端、桌面端 | 跨平台应用 |
| PrimeVue | 组件数量多，表格能力强 | 企业应用、数据表格系统 |

## Angular 生态

| 组件库 | 特点 | 适合场景 |
| --- | --- | --- |
| Angular Material | 官方 Material Design 组件库 | 标准 Angular 应用 |
| NG-ZORRO | Ant Design 风格 Angular 实现 | 企业后台 |
| PrimeNG | 组件丰富，数据表格强 | 企业级 Angular 项目 |

## PC 端热门组件库 Top 100

以下列表按 GitHub star（收藏数）热度、项目知名度和 PC Web 适用性综合整理，属于近似排序。GitHub 搜索结果会混入纯图标库、移动端专用库、文档工具、模板项目和非 UI 组件库项目，本列表已按“PC 端 Web UI 组件库 / CSS 框架 / Headless 组件 / Design System（设计系统）”口径过滤。

| 排名 | 组件库 / 仓库 | 技术栈 | 定位 |
| --- | --- | --- | --- |
| 1 | Bootstrap / twbs/bootstrap | HTML / CSS / JS | 经典响应式 CSS 框架，PC 与移动都适用 |
| 2 | MUI / mui/material-ui | React | Material Design React 组件库 |
| 3 | Ant Design / ant-design/ant-design | React | 企业级中后台组件库 |
| 4 | Tailwind CSS / tailwindlabs/tailwindcss | CSS | Utility-first CSS（工具类优先 CSS）框架 |
| 5 | Element UI / ElemeFE/element | Vue 2 | Vue 2 中后台组件库 |
| 6 | Semantic UI / Semantic-Org/Semantic-UI | HTML / CSS / JS | 语义化 CSS 组件框架 |
| 7 | Bulma / jgthms/bulma | CSS | 基于 Flexbox 的 CSS 框架 |
| 8 | Vuetify / vuetifyjs/vuetify | Vue | Material Design Vue 组件框架 |
| 9 | DaisyUI / saadeghi/daisyui | Tailwind CSS | Tailwind CSS 组件插件 |
| 10 | Chakra UI / chakra-ui/chakra-ui | React | 面向 SaaS 的 React 组件系统 |
| 11 | Materialize / Dogfalo/materialize | CSS / JS | Material Design CSS 框架 |
| 12 | Layui / layui/layui | HTML / CSS / JS | 浏览器原生态 Web UI 组件库 |
| 13 | HeroUI / heroui-inc/heroui | React | 现代 React UI 组件库，原 NextUI |
| 14 | Element Plus / element-plus/element-plus | Vue 3 | Vue 3 中后台组件库 |
| 15 | Quasar / quasarframework/quasar | Vue | Vue 跨端 UI 框架，PC Web 与桌面端均可用 |
| 16 | Angular Material / angular/components | Angular | Angular 官方 Material Design 组件库 |
| 17 | View UI / iview/iview | Vue 2 | 早期高质量 Vue 中后台 UI Toolkit |
| 18 | React Bootstrap / react-bootstrap/react-bootstrap | React | Bootstrap 的 React 组件实现 |
| 19 | Fluent UI / microsoft/fluentui | React / Web Components | 微软 Fluent Design 组件体系 |
| 20 | Radix Primitives / radix-ui/primitives | React | 无样式可访问性基础组件 |
| 21 | Naive UI / tusen-ai/naive-ui | Vue 3 | Vue 3 可主题化组件库 |
| 22 | Pico CSS / picocss/pico | CSS | 语义化 HTML 的极简 CSS 框架 |
| 23 | Tremor / tremorlabs/tremor-npm | React / Tailwind CSS | Dashboard（仪表盘）和图表组件 |
| 24 | React Spectrum / adobe/react-spectrum | React | Adobe 可访问性设计系统组件 |
| 25 | Bootswatch / thomaspark/bootswatch | Bootstrap | Bootstrap 主题集合 |
| 26 | BootstrapVue / bootstrap-vue/bootstrap-vue | Vue | Bootstrap 的 Vue 组件实现 |
| 27 | PrimeVue / primefaces/primevue | Vue | 企业级 Vue 组件库，数据组件强 |
| 28 | Semantic UI React / Semantic-Org/Semantic-UI-React | React | Semantic UI 的 React 实现 |
| 29 | TW Elements / mdbootstrap/TW-Elements | Tailwind CSS | Tailwind + Material Design 组件集合 |
| 30 | Primer CSS / primer/css | CSS | GitHub Primer 设计系统 CSS 实现 |
| 31 | Evergreen / segmentio/evergreen | React | Segment 的 React UI Framework（界面框架） |
| 32 | Bootstrap Table / wenzhixin/bootstrap-table | JS / Bootstrap | 表格组件，支持多种 CSS 框架 |
| 33 | Spectre.css / picturepan2/spectre | CSS | 轻量响应式 CSS 框架 |
| 34 | Material Web / material-components/material-web | Web Components | Material Design Web Components（网页组件） |
| 35 | MudBlazor / MudBlazor/MudBlazor | Blazor | Material Design Blazor 组件库 |
| 36 | Milligram / milligram/milligram | CSS | 极简 CSS 框架 |
| 37 | shadcn-vue / unovue/shadcn-vue | Vue / Tailwind CSS | shadcn/ui 的 Vue 移植版本 |
| 38 | FAST / microsoft/fast | Web Components | 微软现代 Web Components 组件系统 |
| 39 | Base UI / mui/base-ui | React | MUI 团队的无样式可访问性组件 |
| 40 | Flowbite / themesberg/flowbite | Tailwind CSS | Tailwind CSS 组件库和前端框架 |
| 41 | NG-ZORRO / NG-ZORRO/ng-zorro-antd | Angular | Ant Design 风格 Angular 组件库 |
| 42 | Base Web / uber/baseweb | React | Uber Base Design 组件库 |
| 43 | RSuite / rsuite/rsuite | React | 企业级 React 组件套件 |
| 44 | Radix Themes / radix-ui/themes | React | 基于 Radix 的带样式组件库 |
| 45 | PrimeReact / primefaces/primereact | React | 企业级 React 组件库 |
| 46 | Nebular / akveo/nebular | Angular | 基于 Eva Design System 的 Angular UI 库 |
| 47 | Rebass / rebassjs/rebass | React | 基于 styled-system 的 React 原子组件 |
| 48 | React95 / react95-io/React95 | React | Windows 95 风格 React 组件库 |
| 49 | Metro UI / olton/metroui | HTML / CSS / JS | Metro 风格前端 UI 框架 |
| 50 | GoldenLayout / golden-layout/golden-layout | JS | 多窗口布局管理组件 |
| 51 | Charts.css / ChartsCSS/charts.css | CSS | 用 CSS 构建数据可视化组件 |
| 52 | Reka UI / unovue/reka-ui | Vue | Vue 可访问性 Headless UI 组件库 |
| 53 | Clarity / vmware-archive/clarity | Web Components / Angular | 企业级设计系统和组件库 |
| 54 | Preline UI / htmlstreamofficial/preline | Tailwind CSS | Tailwind 预制组件集合 |
| 55 | Polaris React / Shopify/polaris-react | React | Shopify Polaris 设计系统 React 实现 |
| 56 | Arco Design / arco-design/arco-design | React | 字节系企业级 React 组件库 |
| 57 | Varlet / varletjs/varlet | Vue 3 | Material Design 风格 Vue 3 组件库，兼顾桌面和移动 |
| 58 | Oat / knadh/oat | HTML / CSS / JS | 超轻量语义化 UI 库 |
| 59 | Neobrutalism Components / ekmas/neobrutalism-components | React / Tailwind CSS | 新野兽派风格组件集合 |
| 60 | Zag / chakra-ui/zag | Headless / 多框架 | 基于状态机的 Headless 组件逻辑 |
| 61 | Gluestack UI / gluestack/gluestack-ui | React / React Native | 跨 Web 与 React Native 的组件体系 |
| 62 | Searchkit / searchkit/searchkit | React / Vue | Elasticsearch / OpenSearch 搜索 UI 组件 |
| 63 | MDUI / zdhxiong/mdui | Web Components | Material Design 3 Web Components |
| 64 | MUI CSS / muicss/mui | CSS / JS | 轻量 Material Design CSS 框架 |
| 65 | Sakura / oxalorg/sakura | CSS | 极简 classless CSS（无类名 CSS）主题 |
| 66 | Radzen Blazor / radzenhq/radzen-blazor | Blazor | Blazor 企业级组件库 |
| 67 | Topcoat / topcoat/topcoat | CSS | 面向 Web App 的 CSS UI 组件 |
| 68 | Melt UI / melt-ui/melt-ui | Svelte | Svelte Headless 可访问性组件构建器 |
| 69 | Vue Bits / DavidHDev/vue-bits | Vue / Tailwind CSS | 动画与交互型 Vue 组件集合 |
| 70 | Mantine / mantinedev/mantine | React | 组件丰富的 React UI 库和 Hooks 集合 |
| 71 | shadcn/ui / shadcn-ui/ui | React / Tailwind CSS | 复制源码式组件集合，适合高度定制 |
| 72 | Headless UI / tailwindlabs/headlessui | React / Vue | Tailwind 官方 Headless UI 基础组件 |
| 73 | Blueprint / palantir/blueprint | React | 面向复杂数据密集型 PC 应用 |
| 74 | Semi Design / DouyinFE/semi-design | React | 抖音系企业级设计系统 |
| 75 | TDesign React / Tencent/tdesign-react | React | 腾讯 TDesign React 组件库 |
| 76 | TDesign Vue Next / Tencent/tdesign-vue-next | Vue 3 | 腾讯 TDesign Vue 3 组件库 |
| 77 | TDesign Web Components / Tencent/tdesign-web-components | Web Components | 腾讯 TDesign Web Components 版本 |
| 78 | Ant Design Vue / vueComponent/ant-design-vue | Vue | Ant Design 的 Vue 实现 |
| 79 | Vuesax / lusaxweb/vuesax | Vue 2 | Vue 2 组件框架，视觉风格较强 |
| 80 | Vuestic UI / epicmaxco/vuestic-ui | Vue 3 | Vue 3 可访问性组件库 |
| 81 | Carbon Design System / carbon-design-system/carbon | React / Web Components | IBM Carbon 设计系统 |
| 82 | PatternFly React / patternfly/patternfly-react | React | Red Hat 企业级设计系统组件 |
| 83 | Grommet / grommet/grommet | React | 响应式、可访问性 React 组件库 |
| 84 | Shoelace / shoelace-style/shoelace | Web Components | 框架无关 Web Components 组件库 |
| 85 | Vaadin / vaadin/web-components | Web Components | 企业级 Web Components 组件集合 |
| 86 | UI5 Web Components / SAP/ui5-webcomponents | Web Components | SAP UI5 Web Components |
| 87 | Spectrum Web Components / adobe/spectrum-web-components | Web Components | Adobe Spectrum Web Components |
| 88 | Lion / ing-bank/lion | Web Components | ING 开源的企业级 Web Components 基础库 |
| 89 | Elix / elix/elix | Web Components | 原生 Web Components 组件集合 |
| 90 | Material Components Web / material-components/material-components-web | HTML / CSS / JS | 早期 Material Design Web 组件实现 |
| 91 | Foundation Sites / foundation/foundation-sites | CSS / JS | 老牌响应式前端框架 |
| 92 | UIkit / uikit/uikit | CSS / JS | 轻量模块化前端框架 |
| 93 | Fomantic UI / fomantic/Fomantic-UI | CSS / JS | Semantic UI 社区维护分支 |
| 94 | Tachyons / tachyons-css/tachyons | CSS | Functional CSS（函数式 CSS）工具类框架 |
| 95 | Skeleton / dhg/Skeleton | CSS | 极简响应式 CSS 样板框架 |
| 96 | Pure.css / pure-css/pure | CSS | Yahoo 出品的轻量 CSS 模块集合 |
| 97 | Basscss / basscss/basscss | CSS | 低层级工具类 CSS 框架 |
| 98 | Ark UI / chakra-ui/ark | React / Solid / Vue / Svelte | Chakra 团队跨框架 Headless 组件库 |
| 99 | NextUI / nextui-org/nextui | React | HeroUI 前身，现代 React 组件库 |
| 100 | React Aria Components / adobe/react-spectrum | React | Adobe React Aria 的可访问性组件层 |

### PC 端选型观察

| 场景 | 优先候选 |
| --- | --- |
| React 企业中后台 | Ant Design、MUI、Arco Design、Semi Design、Fluent UI |
| Vue 企业中后台 | Element Plus、Naive UI、Ant Design Vue、TDesign Vue Next、PrimeVue |
| Angular 企业应用 | Angular Material、NG-ZORRO、PrimeNG、Nebular |
| Tailwind 项目 | shadcn/ui、DaisyUI、Flowbite、Preline UI、TW Elements |
| 自定义设计系统 | Radix Primitives、Base UI、Headless UI、Ark UI、Zag、Reka UI |
| Web Components | Shoelace、FAST、Material Web、Vaadin、UI5 Web Components、Spectrum Web Components |
| 数据密集型后台 | Ant Design、MUI X、PrimeReact、PrimeVue、Blueprint、RSuite |
| CSS 快速建站 | Bootstrap、Bulma、Pico CSS、Spectre.css、UIkit、Foundation |

## 跨框架 / Web Components

| 组件库 | 特点 | 适合场景 |
| --- | --- | --- |
| Ionic | 移动端体验好，支持多框架 | 混合移动应用 |
| Shoelace | Web Components（网页组件）原生组件库 | 框架无关项目 |
| Flowbite | 基于 Tailwind CSS，支持多框架版本 | Tailwind 项目 |
| DaisyUI | Tailwind CSS 插件，类名式组件 | 快速搭建页面 |

## CSS / Tailwind 方向

| 组件库 | 特点 | 适合场景 |
| --- | --- | --- |
| Tailwind UI | 官方高质量付费组件模板 | 商业产品、营销页 |
| DaisyUI | 免费、简单、主题多 | 快速原型 |
| Flowbite | 组件和模板较全 | Tailwind 项目 |
| Preline UI | Tailwind 组件集合 | 后台、营销页 |

## 移动端 / 小程序方向

### Vue 移动端

| 组件库 | 技术栈 | 特点 |
| --- | --- | --- |
| Vant | Vue 2 / Vue 3 | 国内常用的移动端组件库，适合电商、业务 H5、轻应用 |
| NutUI | Vue / Taro | 京东风格组件库，支持移动端和多端 |
| Varlet | Vue 3 | Material Design 风格，支持暗黑模式 |
| Vux | Vue 2 | 老牌微信 H5 组件库，维护活跃度相对低 |
| Mand Mobile | Vue | 金融业务场景组件较多 |
| Cube UI | Vue 2 | 滴滴开源，移动端体验较好，但生态偏旧 |

### React 移动端

| 组件库 | 技术栈 | 特点 |
| --- | --- | --- |
| Ant Design Mobile | React | 蚂蚁移动端组件库，适合金融、业务 H5、小程序风格页面 |
| Zarm | React | 众安开源，偏保险、金融业务场景 |
| React Vant | React | Vant 的 React 实现，适合喜欢 Vant 风格但使用 React 的项目 |
| Arco Design Mobile | React | 字节系移动端设计体系，风格现代 |
| Ionic React | React | 跨平台移动 App / PWA（渐进式 Web 应用）能力强 |

### 小程序 / 多端

| 组件库 | 技术栈 | 特点 |
| --- | --- | --- |
| Taro UI | Taro | 多端统一组件库，支持小程序、H5、React Native 等 |
| NutUI | Vue / Taro | 支持京东小程序、微信小程序、H5 |
| Vant Weapp | 微信小程序 | Vant 的小程序版本，微信小程序里较常见 |
| WeUI | 微信小程序 / H5 | 微信官方视觉风格，适合微信生态 |
| TDesign Miniprogram | 微信小程序 | 腾讯设计体系的小程序组件库 |
| Wux Weapp | 微信小程序 | 小程序组件较丰富，但活跃度一般 |
| ColorUI | 小程序 | 样式丰富，适合快速搭页面 |
| ThorUI | 小程序 | 商业组件较多，偏小程序业务项目 |
| Lin UI | 小程序 | 文档友好，风格简洁 |

### 跨平台 App

| 组件库 | 技术栈 | 特点 |
| --- | --- | --- |
| Ionic | Web Components / React / Vue / Angular | 跨平台能力强，适合 App、PWA、混合应用 |
| Framework7 | Vue / React / Svelte | iOS / Android 原生风格明显 |
| Onsen UI | Vue / React / Angular | 移动 App 风格组件，适合 Cordova / Capacitor |
| NativeBase | React Native | React Native 常用组件库 |
| React Native Paper | React Native | Material Design 风格，适合 RN App |
| Tamagui | React / React Native | 跨 Web 和 React Native，性能和主题能力较强 |
| Gluestack UI | React Native / Web | NativeBase 后续方向，跨端组件能力强 |
| UI Kitten | React Native | 主题系统较完整，适合 React Native 项目 |

### H5 / 轻量 CSS 组件

| 组件库 | 技术栈 | 特点 |
| --- | --- | --- |
| WeUI | H5 / 小程序 | 微信官方风格 |
| FrozenUI | H5 | 腾讯早期移动端 UI，偏旧 |
| SUI Mobile | H5 | 类 iOS 风格，维护较少 |
| MUI | H5 | DCloud 生态，适合 HBuilder / HTML5+ 项目 |
| YDUI | Vue / H5 | 移动端基础组件，维护活跃度一般 |

## 颜色主题实现方式

现代 UI 组件库的颜色主题通常不是把颜色直接写死在组件里，而是先抽象成 Design Token（设计令牌），再映射到 CSS Variables（CSS 变量）、Theme Object（主题对象）或构建工具变量中。

### 常见实现模型

| 实现方式 | 核心机制 | 代表组件库 |
| --- | --- | --- |
| Design Token | 用 primary、success、warning、text、background 等语义变量描述颜色 | Ant Design、MUI、Chakra UI、Mantine |
| CSS Variables | 通过 `--color-primary`、`--color-bg` 等 CSS 变量驱动组件样式 | shadcn/ui、DaisyUI、HeroUI、Element Plus |
| Theme Object | 使用 JavaScript 对象描述主题，再通过 ThemeProvider（主题提供器）传给组件 | MUI、Chakra UI、Mantine |
| Less / Sass 变量 | 构建阶段替换变量生成 CSS | Ant Design v4、Element UI、老版本 Bootstrap |
| Tailwind 配置 | 在 `tailwind.config.js` 中映射颜色，组件通过 class 使用 | shadcn/ui、Flowbite、DaisyUI |
| Color Algorithm | 根据主色自动生成色阶和状态色 | Ant Design、MUI、Mantine、Chakra UI |

### 主题切换逻辑

常见主题切换流程如下：

```txt
品牌色 / 基础配置
        ↓
Design Token（设计令牌）
        ↓
生成色阶、状态色、语义色
        ↓
写入 CSS Variables（CSS 变量）或 Theme Object（主题对象）
        ↓
组件读取变量
        ↓
切换主题时替换变量
```

### 明暗模式

明暗模式通常通过 class（类名）或 attribute（属性）切换：

```css
:root {
  --color-bg: #ffffff;
  --color-text: #111827;
}

[data-theme="dark"] {
  --color-bg: #0f172a;
  --color-text: #f8fafc;
}
```

```js
document.documentElement.dataset.theme = "dark";
```

也可以通过 `prefers-color-scheme`（系统颜色偏好）跟随系统主题：

```css
@media (prefers-color-scheme: dark) {
  :root {
    --color-bg: #0f172a;
    --color-text: #f8fafc;
  }
}
```

### 不同库的典型方式

| UI 库 | 主题实现方式 |
| --- | --- |
| shadcn/ui | Tailwind CSS + CSS Variables + class 切换暗色 |
| Ant Design v5 | Design Token + CSS-in-JS（CSS 写在 JS 中）+ 颜色算法 |
| MUI | ThemeProvider + Theme Object + Emotion |
| Chakra UI | Theme Object + CSS Variables |
| Mantine | Theme Object + CSS Variables |
| DaisyUI | `data-theme` + CSS Variables |
| Element Plus | CSS Variables + Sass 变量 |
| Radix UI | 不提供视觉主题，交给使用方实现 |
| Headless UI | 不提供视觉主题，通常配合 Tailwind 使用 |

## 选型建议

| 需求 | 推荐 |
| --- | --- |
| React + Tailwind | shadcn/ui |
| React 企业后台 | Ant Design 或 MUI |
| Vue 3 企业后台 | Element Plus 或 Naive UI |
| 自定义设计系统 | Radix UI |
| 快速做漂亮页面 | HeroUI / NextUI 或 Mantine |
| 数据密集型后台 | Ant Design、MUI X、PrimeReact |
| Vue 3 移动 H5 | Vant、NutUI、Varlet |
| React 移动 H5 | Ant Design Mobile、React Vant、Arco Design Mobile |
| 微信小程序 | Vant Weapp、WeUI、TDesign Miniprogram |
| Taro 多端 | NutUI、Taro UI |
| React Native App | React Native Paper、Tamagui、Gluestack UI |
| 混合 App / PWA | Ionic、Framework7 |

## 初步结论

如果项目以 React + Tailwind CSS 为主，并且希望长期保持高度定制能力，优先考虑 shadcn/ui。  
如果项目是企业中后台系统，并且需要成熟表单、表格和设计规范，优先考虑 Ant Design 或 MUI。  
如果项目以 Vue 3 为主，Element Plus 和 Naive UI 是更稳妥的选择。  
如果目标是构建自己的设计系统，Radix UI 和 Headless UI 更适合作为底层基础能力。
移动端业务项目需要优先区分 H5、小程序、React Native、混合 App 等运行环境，再选择对应组件库。  
如果要自己实现主题系统，优先使用 Design Token + CSS Variables 的方式，动态切换主题和多品牌扩展成本更低。
