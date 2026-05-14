# 主题切换实现方式调研

## 调研目的

分析主流 UI component libraries（界面组件库）和 Design System（设计系统）的 theme switching（主题切换）实现方式，重点关注颜色主题、Light / Dark Mode（明暗模式）、Design Token（设计令牌）、CSS Variables（CSS 变量）和运行时切换机制。

## 核心模型

主流主题系统通常遵循以下链路：

```txt
品牌配置 / 用户偏好
        ↓
Design Token（设计令牌）
        ↓
语义色、状态色、色阶、排版、圆角、阴影
        ↓
Theme Object（主题对象）或 CSS Variables（CSS 变量）
        ↓
组件读取 theme / token / var(--*)
        ↓
切换 light / dark / brand 时替换变量或主题对象
```

## 常见实现方式

| 实现方式 | 核心机制 | 优点 | 代价 | 代表库 |
| --- | --- | --- | --- | --- |
| ThemeProvider + Theme Object | React / Vue context（上下文）提供主题对象，组件读取 theme | API 灵活，适合组件级覆盖 | 切换时可能触发较多运行时样式计算 | MUI、Chakra UI、Mantine |
| CSS Variables | 将 token 输出为 `--color-*`，组件用 `var(--*)` | 切换快，适合多主题和 SSR（服务端渲染） | 需要设计变量命名和作用域策略 | shadcn/ui、DaisyUI、HeroUI、Element Plus |
| CSS-in-JS | JS 中根据 theme 生成 className 和 CSS | 和组件状态结合紧密 | 有运行时成本，SSR 需额外处理 | MUI v5、Ant Design v5、Emotion、Styled Components |
| Data Attribute / Class | 通过 `[data-theme="dark"]` 或 `.dark` 覆盖变量 | 简单、直观、易持久化 | 复杂多品牌时变量组织要清晰 | DaisyUI、Tailwind、shadcn/ui |
| Build-time Variables | Less / Sass 编译期替换变量 | 产物稳定，运行时简单 | 动态切换困难，需要多份 CSS 或重新编译 | Ant Design v4、Element UI |
| Color Algorithm | 基于 seed color（种子颜色）生成色阶和状态色 | 主题扩展一致性好 | 算法复杂，需要保证对比度 | Ant Design、MUI、Mantine、Chakra UI |
| Headless + 外部样式 | 组件只提供行为和可访问性，主题交给业务 | 设计自由度最高 | 需要自建视觉规范 | Radix UI、Headless UI、Base UI、Ark UI |

## MUI 主题切换

MUI 主要有两套方式：传统 `ThemeProvider` 方式和现代 `CssVarsProvider` 方式。

### ThemeProvider 方式

```tsx
import { createTheme, ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';

const theme = createTheme({
  palette: {
    mode: 'dark',
  },
});

export function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <AppContent />
    </ThemeProvider>
  );
}
```

核心点：

| 机制 | 说明 |
| --- | --- |
| `createTheme` | 创建包含 `palette`、`typography`、`spacing`、`shape`、`components` 的主题对象 |
| `ThemeProvider` | 通过 context（上下文）把主题传给组件树 |
| `palette.mode` | 控制 `light` / `dark` 默认颜色 token |
| `CssBaseline` | 根据主题设置全局基础样式，如 `body` 背景色和文本色 |
| `sx` / `styled` | 读取 `theme.palette.*` 并由 Emotion 生成 CSS |

切换流程：

```txt
mode 状态变化
        ↓
重新 createTheme
        ↓
ThemeProvider 接收新 theme
        ↓
组件重新读取 theme.palette
        ↓
Emotion 生成或更新样式
```

### CssVarsProvider 方式

```tsx
import {
  CssVarsProvider,
  useColorScheme,
} from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';

function ModeSwitcher() {
  const { mode, setMode } = useColorScheme();

  return (
    <button onClick={() => setMode(mode === 'dark' ? 'light' : 'dark')}>
      切换主题
    </button>
  );
}

export function App() {
  return (
    <CssVarsProvider>
      <CssBaseline />
      <ModeSwitcher />
    </CssVarsProvider>
  );
}
```

CSS Variables 模式下，MUI 会生成类似变量：

```css
:root {
  --mui-palette-primary-main: #1976d2;
  --mui-palette-background-default: #fff;
  --mui-palette-text-primary: rgba(0, 0, 0, 0.87);
}

[data-mui-color-scheme="dark"] {
  --mui-palette-primary-main: #90caf9;
  --mui-palette-background-default: #121212;
  --mui-palette-text-primary: #fff;
}
```

核心点：

| 机制 | 说明 |
| --- | --- |
| `CssVarsProvider` | 提供 CSS Variables 版本的主题上下文 |
| `useColorScheme` | 管理 `light`、`dark`、`system` 等颜色模式 |
| `data-mui-color-scheme` | 通过 attribute（属性）切换变量作用域 |
| `--mui-*` | 组件样式读取的 CSS 变量 |

### MUI 小结

| 方式 | 适合场景 |
| --- | --- |
| `ThemeProvider` | 普通项目、传统 MUI v5 代码、主题对象定制 |
| `CssVarsProvider` | 多主题、SSR、防止闪烁、现代 token 化主题系统 |

## Ant Design 主题切换

Ant Design v5 使用 Design Token + CSS-in-JS + 颜色算法。

```tsx
import { ConfigProvider, theme } from 'antd';

export function App({ dark }: { dark: boolean }) {
  return (
    <ConfigProvider
      theme={{
        algorithm: dark ? theme.darkAlgorithm : theme.defaultAlgorithm,
        token: {
          colorPrimary: '#1677ff',
          borderRadius: 6,
        },
      }}
    >
      <AppContent />
    </ConfigProvider>
  );
}
```

核心点：

| 机制 | 说明 |
| --- | --- |
| `ConfigProvider` | 全局配置入口，提供主题 token |
| Seed Token（种子令牌） | `colorPrimary`、`borderRadius` 等原始输入 |
| Map Token（映射令牌） | 根据算法生成色阶、尺寸、状态变量 |
| Alias Token（别名令牌） | 面向组件和业务语义的 token |
| `theme.darkAlgorithm` | 暗色主题算法 |
| CSS-in-JS | 运行时按 token 注入组件样式 |

切换流程：

```txt
dark 状态变化
        ↓
ConfigProvider.theme.algorithm 切换
        ↓
Ant Design 重新计算 token
        ↓
CSS-in-JS 注入新样式
        ↓
组件视觉更新
```

## shadcn/ui 主题切换

shadcn/ui 本身不是传统 npm 组件库，而是复制源码到项目中。它常见主题方式是 Tailwind CSS + CSS Variables + `.dark` class。

```css
:root {
  --background: 0 0% 100%;
  --foreground: 222.2 84% 4.9%;
  --primary: 222.2 47.4% 11.2%;
  --primary-foreground: 210 40% 98%;
}

.dark {
  --background: 222.2 84% 4.9%;
  --foreground: 210 40% 98%;
  --primary: 210 40% 98%;
  --primary-foreground: 222.2 47.4% 11.2%;
}
```

Tailwind 配置中映射变量：

```js
export default {
  theme: {
    extend: {
      colors: {
        background: 'hsl(var(--background))',
        foreground: 'hsl(var(--foreground))',
        primary: {
          DEFAULT: 'hsl(var(--primary))',
          foreground: 'hsl(var(--primary-foreground))',
        },
      },
    },
  },
};
```

切换流程：

```txt
用户切换 dark
        ↓
给 html 或 body 添加 .dark
        ↓
CSS Variables 被覆盖
        ↓
Tailwind class 使用的新变量生效
```

特点：

| 特点 | 说明 |
| --- | --- |
| HSL token | 方便配合 Tailwind 的透明度语法，如 `bg-primary/80` |
| 复制源码 | 主题和组件样式可以完全按项目修改 |
| Radix UI | 组件行为和可访问性由 Radix 提供，视觉由 Tailwind 和 CSS 变量决定 |

## Chakra UI 主题切换

Chakra UI 使用 Theme Object + CSS Variables + Color Mode（颜色模式）。

```tsx
import { ChakraProvider, extendTheme } from '@chakra-ui/react';

const theme = extendTheme({
  config: {
    initialColorMode: 'system',
    useSystemColorMode: true,
  },
  colors: {
    brand: {
      500: '#3182ce',
    },
  },
});

export function App() {
  return (
    <ChakraProvider theme={theme}>
      <AppContent />
    </ChakraProvider>
  );
}
```

核心点：

| 机制 | 说明 |
| --- | --- |
| `ChakraProvider` | 提供主题上下文 |
| `extendTheme` | 扩展 colors、fonts、components 等 token |
| `ColorModeScript` | 初始化颜色模式，减少首屏闪烁 |
| `useColorMode` | 运行时切换 light / dark |
| CSS Variables | Chakra 将主题 token 输出为 CSS 变量 |

## Mantine 主题切换

Mantine 使用 `MantineProvider`、主题对象和颜色方案管理。

```tsx
import { MantineProvider } from '@mantine/core';

export function App() {
  return (
    <MantineProvider
      defaultColorScheme="auto"
      theme={{
        primaryColor: 'blue',
      }}
    >
      <AppContent />
    </MantineProvider>
  );
}
```

核心点：

| 机制 | 说明 |
| --- | --- |
| `MantineProvider` | 全局主题入口 |
| `defaultColorScheme` | 支持 `light`、`dark`、`auto` |
| `theme.colors` | 常用 10 阶颜色数组 |
| CSS Variables | Mantine 将主题值输出为 CSS 变量 |
| hooks | 通过 hooks（钩子函数）切换和读取颜色模式 |

## DaisyUI 主题切换

DaisyUI 是 Tailwind CSS 插件，主题切换主要依赖 `data-theme`。

```html
<html data-theme="dark">
  <body>
    <button class="btn btn-primary">Button</button>
  </body>
</html>
```

核心点：

| 机制 | 说明 |
| --- | --- |
| `data-theme` | 主题作用域入口 |
| CSS Variables | DaisyUI 为每个主题生成变量 |
| 预设主题 | 内置大量主题，如 `light`、`dark`、`cupcake` 等 |
| Tailwind class | 组件通过 `btn`、`card`、`alert` 等 class 使用主题变量 |

切换流程：

```txt
document.documentElement.setAttribute('data-theme', 'dark')
        ↓
匹配对应主题变量
        ↓
所有 DaisyUI 组件更新颜色
```

## Element Plus 主题切换

Element Plus 使用 CSS Variables + Sass 变量。运行时主题切换通常通过覆盖 CSS 变量实现。

```css
:root {
  --el-color-primary: #409eff;
  --el-bg-color: #ffffff;
  --el-text-color-primary: #303133;
}

html.dark {
  --el-bg-color: #141414;
  --el-text-color-primary: #e5eaf3;
}
```

核心点：

| 机制 | 说明 |
| --- | --- |
| `--el-*` | Element Plus 主题变量前缀 |
| Sass 变量 | 编译期自定义默认主题 |
| CSS Variables | 运行时覆盖颜色和组件变量 |
| `.dark` | 常见暗色模式 class |

## Radix UI / Headless UI 主题切换

Radix UI 和 Headless UI 主要提供无样式组件，不直接规定主题系统。

| 库 | 主题职责 |
| --- | --- |
| Radix UI | 提供行为、状态属性、ARIA（可访问性）和键盘交互 |
| Headless UI | 提供无样式交互组件，视觉由 Tailwind 或业务 CSS 决定 |
| Base UI / Ark UI | 类似 Headless 方案，主题由使用方实现 |

常见组合：

```txt
Headless 组件
        ↓
data-state / data-disabled / aria-* 状态属性
        ↓
Tailwind / CSS Modules / CSS Variables 编写视觉样式
        ↓
.dark 或 [data-theme] 切换变量
```

## 关键工程问题

## 从图片到主题色的实现分层（cheat sheet 解读）

这套分层适合补充到 Color Algorithm（颜色算法）实践中，尤其适用于 Material You（Material 你）风格的动态主题。

### 1) 从图片提取候选主题色

```txt
Wallpaper（壁纸）
        ↓
Quantize（颜色量化）
        ↓
Score（颜色评分）
        ↓
Top Seed Color（高质量种子色）
```

| 步骤 | 作用 | 工程价值 |
| --- | --- | --- |
| Quantize（颜色量化） | 把图片压缩为 N 个代表色 | 降噪并降低颜色空间复杂度，避免直接在海量像素上做主题决策 |
| Score（颜色评分） | 对候选色按主题适配性排序并去重 | 提高可用性，避免只按“出现频率”选色导致灰暗或脏色入选 |

说明：cheat sheet 中提到的 Celebi / Wu / WSMeans 属于量化与聚类链路中的实现细节；在组件库层面可抽象为“先量化，再评分”。

### 2) 给定一个颜色，生成可用主题

```txt
Seed Color（种子色）
        ↓
HCT（Hue/Chroma/Tone）
        ↓
Palettes（色调色板）
        ↓
Scheme（语义角色配色）
        ↓
Component Tokens（组件令牌）
```

| 层级 | 输入/输出 | 适用场景 | 风险与成本 |
| --- | --- | --- | --- |
| Scheme（语义配色） | 输入色板，输出 `primary`、`surface`、`onPrimary` 等角色色 | 最推荐给业务与组件直接消费 | 一致性最好，灵活性相对受约束 |
| Palettes（色板） | 输入 seed，输出多条 tonal palettes（按 tone 的色阶） | 设计系统搭建、品牌扩展 | 需要定义 tone 分布与对比规则 |
| HCT（颜色模型） | 输入任意色，输出 hue/chroma/tone 可控表示 | 动态主题算法、亮暗模式自动生成 | 需要色彩工程理解与测试验证 |
| Blend（颜色混合） | 在 HCT 空间插值或调和 hue | 动画、渐变、品牌色协调 | 误用会导致语义漂移或品牌识别弱化 |

### 3) 抽象层级选择建议

| 层级倾向 | 结论 |
| --- | --- |
| 高层（Scheme） | 易用、稳定、设计语言一致性强；默认优先 |
| 中层（Palettes） | 适合设计系统维护者做可控扩展 |
| 底层（HCT / Blend） | 灵活但复杂，适合算法和基础设施层，不建议业务组件直接依赖 |

落地建议：

```txt
业务组件只消费语义 token（如 --color-primary）
算法层负责 Quantize / Score / HCT / Blend
通过 CSS Variables 承载最终主题值
```

这样可以同时获得：动态主题能力、可维护性、跨品牌扩展能力和组件 API 稳定性。

### 首屏闪烁

主题切换常见问题是页面先按 light 渲染，再切到 dark，产生 FOUC（样式闪烁）。常见解决方案：

| 方案 | 说明 |
| --- | --- |
| 内联初始化脚本 | 在 React 渲染前读取 `localStorage` 或系统偏好并设置 class / attribute |
| SSR 注入主题属性 | 服务端直接输出 `class="dark"` 或 `data-theme` |
| 使用库内脚本 | Chakra `ColorModeScript`、MUI `CssVarsProvider` 相关初始化能力 |

### 持久化

常见持久化策略：

| 策略 | 说明 |
| --- | --- |
| `localStorage` | 保存用户手动选择的主题 |
| cookie | SSR 场景可让服务端读取主题 |
| system | 使用 `prefers-color-scheme` 跟随系统 |
| per-brand config | 多品牌系统中按租户或域名加载主题 |

### 多品牌主题

多品牌主题通常不只切 `light` / `dark`，还要切 brand（品牌）：

```txt
brand-a-light
brand-a-dark
brand-b-light
brand-b-dark
```

推荐用语义 token，而不是组件直接引用品牌色：

```css
:root {
  --color-brand: #2563eb;
  --color-surface: #ffffff;
  --color-text: #111827;
  --button-bg: var(--color-brand);
}
```

## 选型建议

| 目标 | 推荐实现 |
| --- | --- |
| 简单明暗模式 | `.dark` class + CSS Variables |
| Tailwind 项目 | shadcn/ui 风格：CSS Variables + Tailwind token 映射 |
| React 企业后台 | MUI `CssVarsProvider` 或 Ant Design `ConfigProvider` |
| Vue 企业后台 | Element Plus CSS Variables 或 Naive UI / TDesign 的主题配置 |
| 自研 Design System | Design Token + CSS Variables + Headless 组件 |
| 多品牌 / 多租户 | Token 分层 + CSS Variables + brand attribute |
| SSR 项目 | 初始化脚本或服务端注入主题属性，避免首屏闪烁 |

## 初步结论

现代主题切换的主流方向是 Design Token（设计令牌）+ CSS Variables（CSS 变量）+ class / data attribute（类名 / 数据属性）切换。Theme Object（主题对象）仍然适合组件库 API 和组件级覆盖，但最终越来越多库会把 token 输出为 CSS Variables，以降低运行时切换成本并改善 SSR 体验。

如果目标是自研主题系统，建议优先采用：

```txt
Design Token
        ↓
CSS Variables
        ↓
[data-theme] / .dark / [data-brand]
        ↓
Headless UI 或自研组件读取语义变量
```

## 各组件库的颜色算法能力对比

本节聚焦“是否能从 seed color（种子色）自动推导主题色”，并区分两类能力：

- 算法中心化：有较完整、明确的官方颜色生成管线。
- 规则推导 + 可配置：提供推导规则和配置项，但不强制单一算法路径。

| 组件库 / 设计系统 | 算法定位 | 典型能力 | 工程侧建议 |
| --- | --- | --- | --- |
| Material Design 3（Material You） | 算法中心化 | `HCT -> Tonal Palette -> Scheme Roles`，支持动态主题与亮暗自动映射 | 适合“从单个种子色生成整套语义主题”的场景 |
| Ant Design v5 | 算法中心化 | `Seed Token -> Map Token -> Alias Token`，`defaultAlgorithm` / `darkAlgorithm` | 适合企业后台，需要稳定主题一致性与 API 化配置 |
| MUI | 规则推导 + 可配置 | `augmentColor`、`tonalOffset`、`contrastText` 推导，支持 `ThemeProvider` / `CssVarsProvider` | 适合已有 MUI 体系项目，逐步 token 化改造 |
| Mantine | 规则推导 + 可配置 | `primaryShade`、variant 规则、`autoContrast`，围绕色阶生成状态色 | 适合需要快速定制品牌色阶和组件变体 |
| Chakra UI | 规则推导 + 可配置 | semantic tokens（语义令牌）+ color mode（颜色模式）+ 主题扩展 | 适合以语义 token 驱动的中大型业务应用 |
| shadcn/ui | 主题机制为主（算法外置） | `Tailwind + CSS Variables`，可接入 OKLCH/HCT 生成结果 | 适合自研设计规范，算法由业务侧控制 |
| DaisyUI | 主题机制为主（算法外置） | 预设主题 + `data-theme` 切换，变量覆盖成本低 | 适合快速多主题切换，算法通常由外部工具补齐 |
| Element Plus | 主题机制为主（算法外置） | `--el-*` CSS Variables + Sass，运行时可覆盖 | 适合 Vue 后台改造，算法建议在 token 构建层实现 |

### 术语说明：规则推导 + 可配置

“规则推导 + 可配置”不是“没有算法”，而是：

- 有默认推导规则：如 hover/active 状态色、对比文本色、浅深色阶映射。
- 规则参数可调：如主色阶、对比阈值、tonal 偏移、语义 token 映射。
- 不强制唯一算法管线：可接入项目自己的 Design Token（设计令牌）策略与品牌规范。

### 选型建议（按颜色算法诉求）

| 诉求 | 推荐优先级 |
| --- | --- |
| 单种子色自动生成完整 light/dark 主题 | Material You > Ant Design v5 > MUI/Mantine/Chakra |
| 需要高度品牌化、可深度定制 token | MUI/Mantine/Chakra/shadcn（配合自建算法层） |
| Vue 生态中平衡工程成本与可维护性 | Element Plus（变量承载）+ 外部算法层（如 HCT/OKLCH 生成） |
