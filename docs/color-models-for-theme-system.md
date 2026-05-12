# 颜色模型在主题系统中的使用

## 核心定位

HCT、CIELAB、OKLCH 都属于颜色空间 / 色彩模型。它们不应直接侵入业务组件，而应放在 Design Token（设计令牌）生成层。

推荐链路：

```txt
Seed Color（种子色 / 品牌色）
        ↓
颜色模型：OKLCH / HCT / CIELAB
        ↓
Palette（色阶）
        ↓
Semantic Token（语义令牌）
        ↓
Component Token（组件令牌）
        ↓
CSS Variables（CSS 变量）
        ↓
组件样式
```

组件最终仍然只读取稳定变量：

```css
var(--color-primary)
var(--button-primary-bg)
var(--color-text)
```

## 模型选择

| 颜色模型 | 推荐用途 | 是否适合直接写 CSS |
| --- | --- | --- |
| OKLCH | Web 组件库主题色阶、亮暗模式、CSS 原生颜色 | 是，现代浏览器支持 `oklch()` |
| HCT | Material Design 3 动态主题、从 seed color 自动生成主题 | 否，通常通过 JS 工具生成 |
| CIELAB / LCH | 色差计算、颜色质量检查、品牌色一致性校验 | 部分支持，但更适合工具层 |
| HSL / HSV / HSB | 简单手工调色、设计沟通 | 可用，但感知均匀性较弱 |
| RGB / HEX | 屏幕显示和兼容回退 | 是 |

如果目标是自研 Web 组件库，优先选择 OKLCH 作为主题色阶生成模型。

## OKLCH 用法

OKLCH 由三个维度组成：

```txt
L = Lightness（明度）
C = Chroma（彩度）
H = Hue（色相）
```

它适合生成感知更均匀的 Web 色阶。常见策略是保持 Hue 基本稳定，主要调整 Lightness，适当调整 Chroma。

示例：

```css
:root {
  --blue-1: oklch(97% 0.03 255);
  --blue-2: oklch(93% 0.06 255);
  --blue-3: oklch(86% 0.09 255);
  --blue-4: oklch(78% 0.12 255);
  --blue-5: oklch(70% 0.16 255);
  --blue-6: oklch(62% 0.20 255);
  --blue-7: oklch(55% 0.20 255);
  --blue-8: oklch(48% 0.18 255);
  --blue-9: oklch(40% 0.15 255);
  --blue-10: oklch(32% 0.12 255);
}
```

再映射为语义 token：

```css
:root {
  --color-primary-bg: var(--blue-1);
  --color-primary-bg-hover: var(--blue-2);
  --color-primary-border: var(--blue-3);
  --color-primary-hover: var(--blue-5);
  --color-primary: var(--blue-6);
  --color-primary-active: var(--blue-7);
}
```

组件只读取语义变量：

```css
.ui-button--primary {
  --button-bg: var(--color-primary);
  --button-bg-hover: var(--color-primary-hover);
  --button-bg-active: var(--color-primary-active);
  --button-text: #ffffff;
}
```

## OKLCH 状态色规则

传统写法容易手工指定状态色：

```css
.button {
  background: #1677ff;
}

.button:hover {
  background: #4096ff;
}

.button:active {
  background: #0958d9;
}
```

OKLCH 更适合把状态色变成规则：

```txt
hover：提高 Lightness，略降 Chroma
active：降低 Lightness，保持或略调 Chroma
disabled：降低 Chroma，并降低对比度
light background：提高 Lightness，降低 Chroma
```

示例：

```css
:root {
  --color-primary: oklch(62% 0.20 255);
  --color-primary-hover: oklch(70% 0.18 255);
  --color-primary-active: oklch(55% 0.20 255);
  --color-primary-disabled: oklch(82% 0.05 255);
}
```

这样不同品牌色可以复用同一套 Lightness / Chroma 规则。

## OKLCH 暗黑模式

暗黑模式不应简单反色，而应重新映射 token。

亮色模式示例：

```css
:root {
  --color-bg-page: oklch(98% 0.005 255);
  --color-bg-container: oklch(100% 0 0);
  --color-text: oklch(20% 0.01 255);

  --color-primary: oklch(62% 0.20 255);
  --color-primary-hover: oklch(70% 0.18 255);
  --color-primary-active: oklch(55% 0.20 255);
}
```

暗黑模式示例：

```css
[data-theme='dark'] {
  --color-bg-page: oklch(16% 0.01 255);
  --color-bg-container: oklch(22% 0.01 255);
  --color-text: oklch(92% 0.01 255);

  --color-primary: oklch(68% 0.18 255);
  --color-primary-hover: oklch(76% 0.16 255);
  --color-primary-active: oklch(60% 0.18 255);
}
```

注意点：

| 规则 | 说明 |
| --- | --- |
| primary 通常更亮 | 暗色背景上需要更高可见性 |
| 背景避免纯黑 | 深灰背景更舒适，层级更容易建立 |
| 文本避免纯白 | 降低刺眼感，保留层级 |
| 边框低对比但可见 | 避免暗色模式中边界消失 |

## HCT 用法

HCT 通常表示 Hue / Chroma / Tone，是 Material Design 3 动态色使用的颜色模型。

它适合从一个 seed color（种子色）生成完整主题。

```txt
Seed Color（种子色）
        ↓
HCT 分析 Hue / Chroma / Tone
        ↓
Tonal Palette（色调色板）
        ↓
Material color roles（颜色角色）
        ↓
Light / Dark Theme
```

Material Design 3 常见 color roles：

```txt
primary
onPrimary
primaryContainer
onPrimaryContainer

secondary
onSecondary
secondaryContainer
onSecondaryContainer

surface
onSurface
background
onBackground
error
onError
outline
```

概念示例：

```ts
const seed = '#6750A4';

const theme = createMaterialTheme(seed);

const cssVars = {
  '--color-primary': theme.schemes.light.primary,
  '--color-on-primary': theme.schemes.light.onPrimary,
  '--color-primary-container': theme.schemes.light.primaryContainer,
  '--color-on-primary-container': theme.schemes.light.onPrimaryContainer,
};
```

HCT 适合：

| 场景 | 说明 |
| --- | --- |
| 动态主题 | 从用户选择色或品牌色生成主题 |
| Material You | Android / Material Design 3 动态色 |
| 自动生成亮暗主题 | 按 Tone 映射浅色和深色角色 |
| 控制可读性 | Tone 更适合做文本和背景关系 |

如果组件库不是 Material 风格，可以借鉴 HCT 的动态主题生成思路，但不必完整照搬 Material color roles。

## CIELAB / LCH 用法

CIELAB 更适合做颜色质量校验，而不是直接作为日常组件样式写法。

常见用途：

```txt
计算两个颜色差异是否足够明显
检查品牌色转换后是否偏色
检查生成色阶是否均匀
做视觉回归中的颜色差异判断
```

CIELAB 常用于 Delta E（色差）计算。

```txt
Delta E 越小，两个颜色越接近
Delta E 越大，两个颜色差异越明显
```

伪代码：

```ts
const diff = deltaE('#1677ff', '#4096ff');

if (diff < 8) {
  console.warn('hover 色和 default 色差异可能不明显');
}
```

CIELAB / LCH 更适合：

| 场景 | 说明 |
| --- | --- |
| 设计工具 | 检查颜色差异和色阶均匀性 |
| token 生成脚本 | 生成后做质量校验 |
| 品牌色管理 | 检查转换和输出是否偏色 |
| 视觉回归 | 判断颜色差异是否超出阈值 |

## 与 HSL / RGB 的区别

HSL / HSV / HSB 直观，但感知均匀性较弱。

```css
hsl(60 100% 50%)
hsl(240 100% 50%)
```

这两个颜色 Lightness 都是 50%，但黄色在人眼中明显比蓝色更亮。

HCT / OKLCH / CIELAB 的价值在于更接近人眼感知。

| 问题 | HSL / RGB 的问题 | HCT / OKLCH / CIELAB 的价值 |
| --- | --- | --- |
| 生成色阶 | 手工调色不稳定 | 按感知明度生成更自然 |
| 暗黑模式 | 简单反色效果差 | 重新映射 Tone / Lightness |
| 多品牌 | 每个品牌手调成本高 | 用算法从 seed color 生成 |
| 状态色 | hover / active 主观 | 基于色阶和明度规则推导 |
| a11y | 对比度容易不足 | 更容易控制文本和背景关系 |

## 当前项目落地方式

当前项目已有：

```txt
UiConfigProvider
        ↓
themeVars
        ↓
CSS Variables
        ↓
UiButton 读取 var(--*)
```

可以增加颜色生成层：

```txt
Seed Color（品牌种子色）
        ↓
OKLCH / HCT 生成 palette
        ↓
生成 themeVars
        ↓
传给 UiConfigProvider
        ↓
UiButton 读取 CSS Variables
```

业务使用方式保持简单：

```vue
<template>
  <UiConfigProvider :theme="theme" :theme-vars="themeVars">
    <UiButton variant="primary">Primary</UiButton>
  </UiConfigProvider>
</template>
```

示例 themeVars：

```ts
const themeVars = {
  colorPrimary: 'oklch(62% 0.20 255)',
  colorPrimaryHover: 'oklch(70% 0.18 255)',
  colorPrimaryActive: 'oklch(55% 0.20 255)',

  buttonPrimaryBg: 'var(--color-primary)',
  buttonPrimaryBgHover: 'var(--color-primary-hover)',
  buttonPrimaryBgActive: 'var(--color-primary-active)',
};
```

组件中仍然只写：

```scss
.ui-button--primary {
  --button-bg: var(--button-primary-bg);
  --button-bg-hover: var(--button-primary-bg-hover);
  --button-bg-active: var(--button-primary-bg-active);
}
```

## 工程实现建议

不要一开始就在运行时做复杂颜色计算。建议分阶段推进。

| 阶段 | 做法 | 价值 |
| --- | --- | --- |
| 第一阶段 | 手写 OKLCH token | 不引入依赖，快速验证设计方向 |
| 第二阶段 | 封装 `generateThemeVars(seedColor)` | 支持多品牌和动态主题 |
| 第三阶段 | 构建期生成 `tokens.css` / `tokens.ts` | 稳定输出，适合组件库发布 |
| 第四阶段 | 加入对比度和 Delta E 校验 | 提升 a11y 和颜色质量 |

第一阶段示例：

```css
:root {
  --color-primary: #1677ff;
  --color-primary: oklch(62% 0.20 255);
  --color-primary-hover: #4096ff;
  --color-primary-hover: oklch(70% 0.18 255);
  --color-primary-active: #0958d9;
  --color-primary-active: oklch(55% 0.20 255);
}
```

第二阶段示例：

```ts
type ThemeVars = Record<string, string>;

function createPrimaryThemeVars(hue: number): ThemeVars {
  return {
    colorPrimaryBg: `oklch(97% 0.03 ${hue})`,
    colorPrimaryBgHover: `oklch(93% 0.06 ${hue})`,
    colorPrimaryHover: `oklch(70% 0.18 ${hue})`,
    colorPrimary: `oklch(62% 0.20 ${hue})`,
    colorPrimaryActive: `oklch(55% 0.20 ${hue})`,

    buttonPrimaryBg: 'var(--color-primary)',
    buttonPrimaryBgHover: 'var(--color-primary-hover)',
    buttonPrimaryBgActive: 'var(--color-primary-active)',
    buttonPrimaryText: '#ffffff',
  };
}
```

第三阶段目录建议：

```txt
tokens/source.json
        ↓
scripts/build-tokens.ts
        ↓
src/styles/tokens.css
src/tokens/index.ts
```

第四阶段质量检查：

```txt
文本和背景对比度是否达标
hover 和 default 是否有足够色差
disabled 是否足够弱化
暗黑模式是否刺眼
不同品牌主题是否保持一致层级
```

## 浏览器兼容

OKLCH 是现代 CSS 能力。如果需要兼容旧浏览器，应提供 fallback（回退值）。

```css
:root {
  --color-primary: #1677ff;
  --color-primary: oklch(62% 0.20 255);
}
```

不支持 `oklch()` 的浏览器会使用前一个有效值。

## 结论

| 模型 | 最适合的角色 |
| --- | --- |
| OKLCH | Web 主题色阶生成、CSS Variables、暗黑模式、多品牌 |
| HCT | Material Design 3 动态主题、从 seed color 自动生成 light / dark |
| CIELAB / LCH | 色差计算、色阶质量检查、品牌色一致性校验 |

对当前自研组件库，推荐优先采用：

```txt
短期：继续使用 SCSS map + CSS Variables
中期：用 OKLCH 定义或生成主题色阶
长期：加入 HCT 动态主题生成和 CIELAB / Delta E 质量校验
```
