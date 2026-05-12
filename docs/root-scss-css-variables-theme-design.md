# :root + SCSS + CSS Variables 主题变量设计

## 核心思路

`:root + SCSS + CSS Variables` 的推荐分工是：

```txt
SCSS map / function / mixin
        ↓ 编译生成
:root / [data-theme='dark'] / [data-brand='xxx']
        ↓ 输出 CSS Variables（CSS 变量）
组件样式读取 var(--*)
```

核心原则：

```txt
SCSS 负责组织和生成
CSS Variables 负责运行时读取和切换
组件只读语义变量，不直接写死颜色
```

这种方式适合当前项目继续扩展自研组件库：全局默认主题放在 `:root`，局部主题覆盖继续交给 `UiConfigProvider`。

## Token 分层

建议分成四层：

```txt
Primitive Token（原始令牌）
        ↓
Semantic Token（语义令牌）
        ↓
Component Token（组件令牌）
        ↓
Component CSS（组件样式）
```

| 层级 | 作用 | 示例 |
| --- | --- | --- |
| Primitive Token | 原始色阶、尺寸、字体、圆角 | `blue-50`、`gray-900`、`spacing-4` |
| Semantic Token | 面向 UI 语义 | `color-primary`、`color-bg-page`、`color-text-primary` |
| Component Token | 面向具体组件 | `button-primary-bg`、`input-border-focus` |
| Component CSS | 组件最终使用变量 | `background: var(--button-primary-bg)` |

组件不要直接读取 primitive token。比如不要在组件里写 `var(--blue-500)`，应读取 `var(--color-primary)` 或 `var(--button-primary-bg)`。

## 推荐目录结构

当前项目可以新增：

```txt
src/styles/
  tokens/
    _primitive.scss
    _semantic.scss
    _components.scss
    _themes.scss
  theme.scss
  global.scss
```

| 文件 | 作用 |
| --- | --- |
| `_primitive.scss` | 定义基础色阶、间距、字号等原始 token |
| `_semantic.scss` | 定义 light / dark 的语义 token 映射 |
| `_components.scss` | 定义 Button、Input、Card 等组件 token |
| `_themes.scss` | 定义 mixin，把 SCSS map 输出成 CSS Variables |
| `theme.scss` | 输出 `:root`、`[data-theme='dark']`、`[data-density='compact']` |
| `global.scss` | 全局 reset、body 背景、字体等 |

## Primitive Token

Primitive Token 是基础资产，不直接给组件使用。

```scss
$palette-blue: (
  50: #e6f4ff,
  100: #bae0ff,
  200: #91caff,
  300: #69b1ff,
  400: #4096ff,
  500: #1677ff,
  600: #0958d9,
  700: #003eb3,
  800: #002c8c,
  900: #001d66,
);

$palette-gray: (
  0: #ffffff,
  50: #f9fafb,
  100: #f3f4f6,
  200: #e5e7eb,
  300: #d1d5db,
  500: #6b7280,
  700: #374151,
  900: #111827,
);

$spacing: (
  1: 4px,
  2: 8px,
  3: 12px,
  4: 16px,
  5: 20px,
  6: 24px,
);

$radius: (
  sm: 4px,
  md: 8px,
  lg: 12px,
  full: 999px,
);
```

## Semantic Token

Semantic Token 表达颜色、背景、文本、边框等 UI 语义。

亮色主题示例：

```scss
$theme-light: (
  color-primary: #1677ff,
  color-primary-hover: #4096ff,
  color-primary-active: #0958d9,
  color-primary-bg: #e6f4ff,
  color-primary-border: #91caff,

  color-success: #52c41a,
  color-warning: #faad14,
  color-error: #ff4d4f,
  color-info: #1677ff,

  color-text-primary: rgba(0, 0, 0, 0.88),
  color-text-secondary: rgba(0, 0, 0, 0.65),
  color-text-tertiary: rgba(0, 0, 0, 0.45),
  color-text-disabled: rgba(0, 0, 0, 0.25),

  color-bg-page: #f5f5f5,
  color-bg-container: #ffffff,
  color-bg-elevated: #ffffff,
  color-bg-disabled: rgba(0, 0, 0, 0.04),

  color-border: #d9d9d9,
  color-border-secondary: #f0f0f0,
  color-split: rgba(5, 5, 5, 0.06),

  shadow-color: rgba(0, 0, 0, 0.12),
);
```

暗黑主题示例：

```scss
$theme-dark: (
  color-primary: #1668dc,
  color-primary-hover: #3c89e8,
  color-primary-active: #1554ad,
  color-primary-bg: #111a2c,
  color-primary-border: #15325b,

  color-success: #49aa19,
  color-warning: #d89614,
  color-error: #dc4446,
  color-info: #1668dc,

  color-text-primary: rgba(255, 255, 255, 0.85),
  color-text-secondary: rgba(255, 255, 255, 0.65),
  color-text-tertiary: rgba(255, 255, 255, 0.45),
  color-text-disabled: rgba(255, 255, 255, 0.25),

  color-bg-page: #000000,
  color-bg-container: #141414,
  color-bg-elevated: #1f1f1f,
  color-bg-disabled: rgba(255, 255, 255, 0.08),

  color-border: #424242,
  color-border-secondary: #303030,
  color-split: rgba(253, 253, 253, 0.12),

  shadow-color: rgba(0, 0, 0, 0.45),
);
```

暗黑模式不要简单反色，应重新映射 semantic token。

## Component Token

Component Token 把通用语义映射到具体组件。

以 Button 为例：

```scss
$component-tokens: (
  button-height-sm: 32px,
  button-height-md: 40px,
  button-height-lg: 48px,

  button-padding-x-sm: 12px,
  button-padding-x-md: 16px,
  button-padding-x-lg: 20px,

  button-font-size-sm: 14px,
  button-font-size-md: 14px,
  button-font-size-lg: 16px,

  button-radius: var(--radius-md),

  button-primary-bg: var(--color-primary),
  button-primary-bg-hover: var(--color-primary-hover),
  button-primary-bg-active: var(--color-primary-active),
  button-primary-text: #ffffff,
  button-primary-border: var(--color-primary),

  button-secondary-bg: var(--color-bg-container),
  button-secondary-bg-hover: var(--color-bg-page),
  button-secondary-bg-active: var(--color-border-secondary),
  button-secondary-text: var(--color-text-primary),
  button-secondary-border: var(--color-border),

  button-danger-bg: var(--color-error),
  button-danger-bg-hover: #ff7875,
  button-danger-bg-active: #d9363e,
  button-danger-text: #ffffff,
  button-danger-border: var(--color-error),
);
```

这样如果 Button 的 primary 不想等于全局 `color-primary`，只需要改 `button-primary-bg`，组件 CSS 不需要变化。

## 输出 CSS Variables

通用 mixin：

```scss
@mixin emit-css-vars($tokens) {
  @each $name, $value in $tokens {
    --#{$name}: #{$value};
  }
}
```

输出主题：

```scss
:root,
[data-theme='light'] {
  color-scheme: light;

  @include emit-css-vars($theme-light);
  @include emit-css-vars($component-tokens);
}

[data-theme='dark'] {
  color-scheme: dark;

  @include emit-css-vars($theme-dark);
  @include emit-css-vars($component-tokens);
}
```

密度覆盖：

```scss
[data-density='compact'] {
  --button-height-sm: 28px;
  --button-height-md: 34px;
  --button-height-lg: 40px;

  --button-padding-x-sm: 10px;
  --button-padding-x-md: 12px;
  --button-padding-x-lg: 16px;
}
```

品牌覆盖：

```scss
[data-brand='ocean'] {
  --color-primary: #008585;
  --color-primary-hover: #00bebf;
  --color-primary-active: #006a6a;
  --color-primary-bg: #f1fffe;
  --color-primary-border: #00dcdd;
}

[data-brand='orange'] {
  --color-primary: #d44700;
  --color-primary-hover: #ff8c61;
  --color-primary-active: #aa3700;
  --color-primary-bg: #fffbff;
  --color-primary-border: #ffb59b;
}
```

## 全局样式使用

`body`、页面背景、默认文本色读取 semantic token：

```scss
html,
body {
  margin: 0;
  min-height: 100%;
}

body {
  background: var(--color-bg-page);
  color: var(--color-text-primary);
  font-family: var(--font-family);
}
```

基础全局变量：

```scss
:root {
  --font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-family-code: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;

  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;

  --motion-duration-fast: 120ms;
  --motion-duration-mid: 160ms;
  --motion-ease-out: cubic-bezier(0.215, 0.61, 0.355, 1);
}
```

## 组件使用方式

组件不关心主题，只读取 component token。

```scss
.ui-button {
  --button-bg: var(--button-secondary-bg);
  --button-bg-hover: var(--button-secondary-bg-hover);
  --button-bg-active: var(--button-secondary-bg-active);
  --button-text: var(--button-secondary-text);
  --button-border: var(--button-secondary-border);

  height: var(--button-height-md);
  padding: 0 var(--button-padding-x-md);
  border: 1px solid var(--button-border);
  border-radius: var(--button-radius);
  background: var(--button-bg);
  color: var(--button-text);
}

.ui-button:hover:not(:disabled) {
  background: var(--button-bg-hover);
}

.ui-button:active:not(:disabled) {
  background: var(--button-bg-active);
}

.ui-button--primary {
  --button-bg: var(--button-primary-bg);
  --button-bg-hover: var(--button-primary-bg-hover);
  --button-bg-active: var(--button-primary-bg-active);
  --button-text: var(--button-primary-text);
  --button-border: var(--button-primary-border);
}

.ui-button--danger {
  --button-bg: var(--button-danger-bg);
  --button-bg-hover: var(--button-danger-bg-hover);
  --button-bg-active: var(--button-danger-bg-active);
  --button-text: var(--button-danger-text);
  --button-border: var(--button-danger-border);
}
```

主题切换只改变量，不改组件 class。

## 命名规范

推荐统一使用：

```txt
--color-*
--font-*
--size-*
--radius-*
--shadow-*
--motion-*
--z-index-*
--button-*
--input-*
--card-*
--table-*
```

| 类型 | 命名示例 |
| --- | --- |
| 语义色 | `--color-primary` |
| 状态色 | `--color-primary-hover` |
| 背景 | `--color-bg-page` |
| 容器 | `--color-bg-container` |
| 文本 | `--color-text-primary` |
| 边框 | `--color-border` |
| 组件 token | `--button-primary-bg` |
| 尺寸 | `--button-height-md` |
| 圆角 | `--radius-md` |
| 动效 | `--motion-duration-fast` |

避免混用：

```txt
--primary-color 和 --color-primary 混用
--btn-bg 和 --button-bg 混用
组件直接使用 --blue-500
```

## :root 与 UiConfigProvider 共存

当前项目已有 `UiConfigProvider`。推荐分工：

```txt
:root
负责默认全局主题

[data-theme='dark']
负责全局暗黑主题

UiConfigProvider
负责局部覆盖、多品牌、演示区域或组件局部主题
```

CSS Variables 有天然级联能力：组件优先读取最近作用域的变量，局部没有定义时回退到 `:root`。

示意：

```html
<html data-theme="light">
  <body>
    <div id="app">
      <section class="normal-page"></section>

      <div class="ui-config-provider" style="--color-primary: #d44700;">
        局部橙色主题
      </div>
    </div>
  </body>
</html>
```

## 当前项目落地建议

建议按以下步骤演进：

| 步骤 | 内容 |
| --- | --- |
| 1 | 新增 `src/styles/theme.scss`，输出 `:root`、`[data-theme='dark']`、`[data-density='compact']` |
| 2 | 在 `src/main.ts` 引入 `@/styles/theme.scss` |
| 3 | 从 `UiConfigProvider.vue` 中迁出默认 SCSS map，保留局部覆盖能力 |
| 4 | `UiButton.vue` 保持读取 `var(--button-*)` 不变 |
| 5 | HCT 页面生成的 `themeVars` 作为局部覆盖示例 |

演进后结构：

```txt
全局默认主题：src/styles/theme.scss
局部主题覆盖：UiConfigProvider themeVars
组件消费变量：UiButton / Input / Card
```

## 推荐最终链路

```txt
src/styles/tokens/_primitive.scss
        ↓
src/styles/tokens/_semantic.scss
        ↓
src/styles/tokens/_components.scss
        ↓
src/styles/theme.scss
        ↓
:root / [data-theme] / [data-brand] / [data-density]
        ↓
UiButton / Input / Card 读取 var(--*)
```

同时保留 JS 层局部覆盖：

```txt
UiConfigProvider
        ↓
themeVars camelCase
        ↓
inline CSS Variables
        ↓
局部主题覆盖
```

## 结论

`:root + SCSS + CSS Variables` 的最佳实践是：

```txt
SCSS map 管理 token
mixin 输出 CSS Variables
:root 放默认 light theme
[data-theme='dark'] 放暗黑 theme
[data-brand] 放品牌覆盖
[data-density] 放密度覆盖
组件只读 var(--component-token)
UiConfigProvider 只做局部覆盖
```

这套方式兼容当前已有的 `UiConfigProvider`、`UiButton`、HCT 色阶生成和 `themeVars`，后续可以自然扩展到 Input、Card、Table、Dialog、Form、多品牌主题和暗黑模式。
