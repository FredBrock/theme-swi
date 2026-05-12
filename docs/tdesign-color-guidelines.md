# TDesign 颜色规范参考

## 核心模型

TDesign 的颜色规范不是简单维护固定色值，而是通过 Palette（色板）、Design Token（设计令牌）和组件变量组织主题能力。

```txt
品牌色 / 功能色 / 中性色
        ↓
Palette（色板）
        ↓
Semantic Token（语义令牌）
        ↓
Component Token（组件令牌）
        ↓
组件样式
```

## 颜色分类

| 类型 | 作用 | 典型使用 |
| --- | --- | --- |
| Brand Color（品牌色） | 表达品牌识别和主要操作 | 主按钮、链接、选中态、焦点状态 |
| Functional Color（功能色） | 表达状态和反馈 | Success、Warning、Error、Info |
| Neutral Color（中性色） | 承载文本、背景、边框和分割线 | 页面背景、容器、正文、弱文本、禁用态 |
| Auxiliary Color（辅助色） | 扩展表达和数据区分 | 图表、标签、徽标、分类信息 |
| Mask / Shadow（遮罩 / 阴影） | 表达浮层和层级 | Dialog、Drawer、Popover、Tooltip |

## 品牌色

品牌色用于关键操作和选中状态，不应大面积滥用。

常见语义变量：

```txt
--td-brand-color
--td-brand-color-hover
--td-brand-color-focus
--td-brand-color-active
--td-brand-color-disabled
--td-brand-color-light
--td-brand-color-light-hover
```

典型映射：

| 组件 / 场景 | 用法 |
| --- | --- |
| Button | primary 背景色、边框色 |
| Link | 默认链接色和 hover 色 |
| Checkbox / Radio | 选中态颜色 |
| Switch | 开启态颜色 |
| Tabs | 激活态文字和指示条 |
| Pagination | 当前页高亮 |
| Focus Ring | 焦点态辅助色 |

## 功能色

功能色表达稳定的状态语义，不应被业务随意改成无关含义。

| 类型 | 语义 | 典型场景 |
| --- | --- | --- |
| Success | 成功、完成、可用、正向反馈 | 成功提示、完成状态、进度成功 |
| Warning | 警告、风险、需要注意 | 警告提示、风险操作、待处理状态 |
| Error / Danger | 错误、失败、危险操作 | 表单校验、删除确认、失败提示 |
| Info | 普通信息、辅助说明 | 信息提示、说明内容、普通状态 |

常见语义变量：

```txt
--td-success-color
--td-success-color-hover
--td-success-color-focus
--td-success-color-active
--td-success-color-disabled
--td-success-color-light

--td-warning-color
--td-error-color
--td-info-color
```

## 中性色

中性色是企业级后台中最常用的一组颜色，决定文本、容器、边框和页面层级。

| 维度 | 常见 token | 用途 |
| --- | --- | --- |
| 文本 | `--td-text-color-primary` | 主文本、标题、重要信息 |
| 文本 | `--td-text-color-secondary` | 次级文本、描述信息 |
| 文本 | `--td-text-color-placeholder` | 占位符、提示文本 |
| 文本 | `--td-text-color-disabled` | 禁用文本 |
| 背景 | `--td-bg-color-page` | 页面底色 |
| 背景 | `--td-bg-color-container` | 卡片、表单、弹层容器 |
| 背景 | `--td-bg-color-container-hover` | 容器 hover 背景 |
| 背景 | `--td-bg-color-container-active` | 容器 active 背景 |
| 边框 | `--td-border-level-1-color` | 弱边框、分割线 |
| 边框 | `--td-border-level-2-color` | 强边框、控件边框 |
| 组件 | `--td-component-bg` | 通用组件背景 |
| 组件 | `--td-component-bg-disabled` | 禁用组件背景 |

## Palette 色阶

TDesign 通常为品牌色和功能色生成多级色阶，用于不同状态和层级。

| 色阶 | 常见用途 |
| --- | --- |
| 1-2 | 极浅背景、标签背景、弱提示背景 |
| 3-4 | focus 背景、选中弱背景、禁用背景 |
| 5 | hover 状态 |
| 6 | 默认主色 |
| 7 | active 状态 |
| 8-10 | 深色强调、深色模式映射、图表辅助 |

示例：

```txt
brand-1  极浅品牌背景
brand-2  浅品牌背景 hover
brand-3  弱选中背景
brand-4  禁用 / 辅助
brand-5  hover
brand-6  默认品牌色
brand-7  active
brand-8  深强调
brand-9  更深
brand-10 最深
```

## 语义优先

组件不应直接使用固定色值，也不应直接依赖某个色阶。组件应读取语义 token。

不推荐：

```css
.button {
  background: #0052d9;
}
```

不推荐：

```css
.button {
  background: var(--td-blue-6);
}
```

推荐：

```css
.button {
  background: var(--td-brand-color);
}

.button:hover {
  background: var(--td-brand-color-hover);
}

.button:active {
  background: var(--td-brand-color-active);
}
```

这样组件无需关心当前品牌、亮色模式或暗黑模式，只依赖稳定语义。

## 暗黑模式

暗黑模式不是简单反转颜色，而是重新映射语义 token。

```css
:root {
  --td-bg-color-page: #f3f3f3;
  --td-bg-color-container: #ffffff;
  --td-text-color-primary: rgba(0, 0, 0, 0.9);
  --td-border-level-1-color: #e7e7e7;
}

[data-theme='dark'] {
  --td-bg-color-page: #111111;
  --td-bg-color-container: #1f1f1f;
  --td-text-color-primary: rgba(255, 255, 255, 0.9);
  --td-border-level-1-color: #3d3d3d;
}
```

组件保持同一套写法：

```css
.card {
  background: var(--td-bg-color-container);
  color: var(--td-text-color-primary);
  border-color: var(--td-border-level-1-color);
}
```

## 使用原则

| 原则 | 说明 |
| --- | --- |
| 语义优先 | 组件使用 `brand-color`、`text-color-primary`，不要直接写色值 |
| 状态完整 | 主要颜色需要 default、hover、active、disabled、focus、light |
| 层级明确 | 页面背景、容器背景、边框、文本要区分层级 |
| 克制使用品牌色 | 品牌色只用于关键操作和选中态 |
| 功能色语义稳定 | success / warning / error 不要随业务随意改变含义 |
| 暗黑模式单独映射 | 不通过简单反色实现暗黑模式 |
| 组件 token 可覆盖 | Button、Input、Table 等组件应能独立调整颜色 |

## 自研组件库参考实现

当前项目可以借鉴 TDesign 的分层方式，将主题变量组织为 SCSS map，再输出 CSS Variables（CSS 变量）。

亮色主题示例：

```scss
$light-theme: (
  brand-color: #0052d9,
  brand-color-hover: #366ef4,
  brand-color-active: #003cab,
  brand-color-disabled: #b5c7ff,
  brand-color-light: #f2f3ff,

  success-color: #00a870,
  warning-color: #ed7b2f,
  error-color: #d54941,

  text-color-primary: rgba(0, 0, 0, 0.9),
  text-color-secondary: rgba(0, 0, 0, 0.6),
  text-color-placeholder: rgba(0, 0, 0, 0.4),
  text-color-disabled: rgba(0, 0, 0, 0.26),

  bg-color-page: #f3f3f3,
  bg-color-container: #ffffff,
  bg-color-container-hover: #f3f3f3,
  bg-color-container-active: #eeeeee,

  border-level-1-color: #e7e7e7,
  border-level-2-color: #dcdcdc,

  button-primary-bg: var(--brand-color),
  button-primary-bg-hover: var(--brand-color-hover),
  button-primary-bg-active: var(--brand-color-active),
  button-primary-text: #ffffff,
);
```

暗黑主题示例：

```scss
$dark-theme: (
  brand-color: #4582e6,
  brand-color-hover: #699ef5,
  brand-color-active: #2667d4,
  brand-color-disabled: #173463,
  brand-color-light: #1b2f51,

  success-color: #48c79c,
  warning-color: #e8935c,
  error-color: #e66a6a,

  text-color-primary: rgba(255, 255, 255, 0.9),
  text-color-secondary: rgba(255, 255, 255, 0.55),
  text-color-placeholder: rgba(255, 255, 255, 0.35),
  text-color-disabled: rgba(255, 255, 255, 0.22),

  bg-color-page: #111111,
  bg-color-container: #1f1f1f,
  bg-color-container-hover: #2c2c2c,
  bg-color-container-active: #383838,

  border-level-1-color: #3d3d3d,
  border-level-2-color: #4a4a4a,

  button-primary-bg: var(--brand-color),
  button-primary-bg-hover: var(--brand-color-hover),
  button-primary-bg-active: var(--brand-color-active),
  button-primary-text: #ffffff,
);
```

组件中只读取语义变量：

```scss
.ui-button--primary {
  --button-bg: var(--button-primary-bg);
  --button-bg-hover: var(--button-primary-bg-hover);
  --button-bg-active: var(--button-primary-bg-active);
  --button-text: var(--button-primary-text);
}
```

## 与其他体系对比

| 体系 | 颜色主题特点 |
| --- | --- |
| TDesign | CSS Variables + Design Token，强调跨框架、多端统一 |
| Vant 4 | CSS Variables + ConfigProvider，适合 Vue 移动端组件主题 |
| Ant Design v5 | Seed Token + Map Token + Alias Token + CSS-in-JS，颜色算法强 |
| Element Plus | CSS Variables + Sass 变量，Vue 生态友好 |
| Carbon | token 严谨，企业级和可访问性强 |

## 结论

TDesign 颜色规范最值得借鉴的不是具体色值，而是：

| 能力 | 价值 |
| --- | --- |
| 色阶完整 | 支撑 hover、active、focus、disabled、light 等状态 |
| 语义清晰 | 组件不依赖具体颜色，方便换肤和多品牌 |
| 层级完整 | 文本、背景、边框、容器都有稳定分层 |
| 暗黑模式可映射 | 通过重定义 token 实现，不修改组件样式 |
| 组件解耦 | 组件只读取 component token，主题系统负责赋值 |
| 多品牌可扩展 | 替换 token 即可切换品牌视觉 |
