# Vant 4 颜色主题规范参考

## 核心模型

Vant 4 的颜色主题以 CSS Variables（CSS 变量）为基础，并通过 ConfigProvider（全局配置组件）支持全局或局部主题覆盖。

```txt
业务品牌 token
        ↓
Vant themeVars
        ↓
CSS Variables（--van-*）
        ↓
Vant 组件样式
        ↓
全局主题 / 局部主题 / 暗黑模式
```

Vant 4 不再主要依赖 Less 编译期变量，而是倾向于运行时可覆盖的 CSS Variables。

## 颜色变量类型

| 类型 | 作用 | 示例 |
| --- | --- | --- |
| 品牌色 | 表达主要操作和品牌识别 | `--van-primary-color` |
| 功能色 | 表达成功、警告、危险等状态 | `--van-success-color`、`--van-danger-color` |
| 文本色 | 表达文本层级 | `--van-text-color`、`--van-text-color-2` |
| 背景色 | 表达页面和容器背景 | `--van-background`、`--van-background-2` |
| 交互色 | 表达 active、disabled 等交互状态 | `--van-active-color`、`--van-disabled-opacity` |
| 组件变量 | 控制具体组件视觉 | `--van-button-primary-background` |

## 全局颜色变量

常见全局变量如下：

```css
:root {
  --van-primary-color: #1989fa;
  --van-success-color: #07c160;
  --van-danger-color: #ee0a24;
  --van-warning-color: #ff976a;

  --van-text-color: #323233;
  --van-text-color-2: #646566;
  --van-text-color-3: #969799;
  --van-active-color: #f2f3f5;
  --van-active-opacity: 0.6;
  --van-disabled-opacity: 0.5;

  --van-background: #f7f8fa;
  --van-background-2: #ffffff;
}
```

这些变量会被 Button、Cell、Form、Popup、Tabbar 等组件复用。

## 组件颜色变量

Vant 4 的组件样式通常由组件级 CSS Variables 控制。以 Button 为例：

```css
:root {
  --van-button-primary-color: #ffffff;
  --van-button-primary-background: var(--van-primary-color);
  --van-button-primary-border-color: var(--van-primary-color);

  --van-button-success-color: #ffffff;
  --van-button-success-background: var(--van-success-color);
  --van-button-success-border-color: var(--van-success-color);

  --van-button-danger-color: #ffffff;
  --van-button-danger-background: var(--van-danger-color);
  --van-button-danger-border-color: var(--van-danger-color);
}
```

组件内部只读取变量：

```css
.van-button--primary {
  color: var(--van-button-primary-color);
  background: var(--van-button-primary-background);
  border-color: var(--van-button-primary-border-color);
}
```

## ConfigProvider 主题配置

Vant 4 推荐使用 `ConfigProvider` 的 `theme-vars` 覆盖主题变量。

```vue
<template>
  <van-config-provider :theme-vars="themeVars">
    <van-button type="primary">主要按钮</van-button>
    <van-button type="success">成功按钮</van-button>
  </van-config-provider>
</template>

<script setup lang="ts">
const themeVars = {
  primaryColor: '#2563eb',
  successColor: '#16a34a',
  dangerColor: '#dc2626',
  warningColor: '#f59e0b',

  buttonPrimaryBackground: '#2563eb',
  buttonPrimaryBorderColor: '#2563eb',
};
</script>
```

命名转换规则：

```txt
CSS Variable: --van-primary-color
themeVars: primaryColor

CSS Variable: --van-button-primary-background
themeVars: buttonPrimaryBackground
```

即去掉 `--van-` 前缀，并将 kebab-case（短横线命名）转换为 camelCase（小驼峰命名）。

## 全局覆盖方式

如果主题固定，也可以直接在全局样式中覆盖 CSS Variables。

```css
:root {
  --van-primary-color: #2563eb;
  --van-success-color: #16a34a;
  --van-danger-color: #dc2626;
  --van-warning-color: #f59e0b;

  --van-button-primary-background: var(--van-primary-color);
  --van-button-primary-border-color: var(--van-primary-color);
}
```

| 方式 | 适合场景 | 注意点 |
| --- | --- | --- |
| 全局 CSS 覆盖 | 固定品牌主题 | 不适合复杂局部主题 |
| ConfigProvider | 动态主题、局部主题、多品牌 | 需要维护 `themeVars` 映射 |
| 暗黑模式 theme | 明暗模式切换 | 需要同时考虑业务自定义变量 |

## 暗黑模式

Vant 4 支持通过 `ConfigProvider` 的 `theme` 属性开启暗黑模式。

```vue
<template>
  <van-config-provider theme="dark">
    <van-cell title="标题" value="内容" />
    <van-button type="primary">按钮</van-button>
  </van-config-provider>
</template>
```

动态切换：

```vue
<template>
  <van-config-provider :theme="theme">
    <van-button type="primary" @click="toggleTheme">
      {{ theme === 'dark' ? '切换到亮色' : '切换到暗色' }}
    </van-button>
  </van-config-provider>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const theme = ref<'light' | 'dark'>('light');

function toggleTheme() {
  theme.value = theme.value === 'dark' ? 'light' : 'dark';
}
</script>
```

如果业务有自定义品牌色，需要分别定义亮色和暗色变量：

```ts
const lightThemeVars = {
  primaryColor: '#2563eb',
  textColor: '#111827',
  background: '#f9fafb',
  background2: '#ffffff',
  buttonPrimaryBackground: '#2563eb',
  buttonPrimaryBorderColor: '#2563eb',
};

const darkThemeVars = {
  primaryColor: '#60a5fa',
  textColor: '#f8fafc',
  background: '#0f172a',
  background2: '#111827',
  buttonPrimaryBackground: '#60a5fa',
  buttonPrimaryBorderColor: '#60a5fa',
};
```

## 多品牌主题

多品牌主题可以把 `themeVars` 抽象成品牌配置。

```ts
const brandThemes = {
  blue: {
    primaryColor: '#2563eb',
    buttonPrimaryBackground: '#2563eb',
    buttonPrimaryBorderColor: '#2563eb',
  },
  green: {
    primaryColor: '#16a34a',
    buttonPrimaryBackground: '#16a34a',
    buttonPrimaryBorderColor: '#16a34a',
  },
  purple: {
    primaryColor: '#7c3aed',
    buttonPrimaryBackground: '#7c3aed',
    buttonPrimaryBorderColor: '#7c3aed',
  },
};
```

使用时根据当前品牌传入：

```vue
<van-config-provider :theme-vars="brandThemes[currentBrand]">
  <van-button type="primary">品牌按钮</van-button>
</van-config-provider>
```

## 局部主题

`ConfigProvider` 可以包裹局部区域，因此同一页面可以出现不同主题作用域。

```vue
<template>
  <van-button type="primary">默认主题按钮</van-button>

  <van-config-provider :theme-vars="dangerThemeVars">
    <van-button type="primary">局部危险主题按钮</van-button>
  </van-config-provider>
</template>

<script setup lang="ts">
const dangerThemeVars = {
  primaryColor: '#dc2626',
  buttonPrimaryBackground: '#dc2626',
  buttonPrimaryBorderColor: '#dc2626',
};
</script>
```

局部主题适合：

| 场景 | 示例 |
| --- | --- |
| 业务模块品牌化 | 不同频道、不同商户、不同活动页 |
| 状态强化 | 危险区域、营销区域、会员区域 |
| 嵌入式页面 | 第三方嵌入、微前端子应用 |

## 推荐 token 分层

在企业项目中，不建议直接把 Vant 变量散落在业务代码里。建议先定义业务 token，再映射到 Vant `themeVars`。

```txt
Primitive Token（原始令牌）
        ↓
Semantic Token（语义令牌）
        ↓
Vant themeVars
        ↓
--van-* CSS Variables
        ↓
Vant 组件
```

示例：

```ts
const brandTokens = {
  colorBrandPrimary: '#2563eb',
  colorBrandSuccess: '#16a34a',
  colorBrandDanger: '#dc2626',
};

const vantThemeVars = {
  primaryColor: brandTokens.colorBrandPrimary,
  successColor: brandTokens.colorBrandSuccess,
  dangerColor: brandTokens.colorBrandDanger,

  buttonPrimaryBackground: brandTokens.colorBrandPrimary,
  buttonPrimaryBorderColor: brandTokens.colorBrandPrimary,
};
```

这种方式可以避免业务代码直接绑定 Vant 的变量命名，后续替换组件库或扩展自研组件更容易。

## 常用颜色变量清单

| 变量 | 用途 |
| --- | --- |
| `primaryColor` | 主品牌色 |
| `successColor` | 成功色 |
| `dangerColor` | 危险 / 错误色 |
| `warningColor` | 警告色 |
| `textColor` | 主文本色 |
| `textColor2` | 次级文本色 |
| `textColor3` | 弱文本 / 占位文本色 |
| `activeColor` | 点击反馈背景色 |
| `activeOpacity` | 点击反馈透明度 |
| `disabledOpacity` | 禁用透明度 |
| `background` | 页面背景 |
| `background2` | 容器背景 |

Button 常用变量：

| 变量 | 用途 |
| --- | --- |
| `buttonPrimaryColor` | primary 按钮文字色 |
| `buttonPrimaryBackground` | primary 按钮背景色 |
| `buttonPrimaryBorderColor` | primary 按钮边框色 |
| `buttonSuccessBackground` | success 按钮背景色 |
| `buttonSuccessBorderColor` | success 按钮边框色 |
| `buttonDangerBackground` | danger 按钮背景色 |
| `buttonDangerBorderColor` | danger 按钮边框色 |
| `buttonDefaultHeight` | 默认按钮高度 |
| `buttonSmallHeight` | 小按钮高度 |
| `buttonLargeHeight` | 大按钮高度 |
| `buttonBorderRadius` | 按钮圆角 |

## 迁移到自研组件库

当前项目是 Vue 2 + Vue CLI 5 + TypeScript，而 Vant 4 面向 Vue 3。因此当前项目不适合直接引入 Vant 4，但可以迁移它的主题模型。

可迁移思路：

| Vant 4 | 自研组件实现 |
| --- | --- |
| `van-config-provider` | `UiConfigProvider` |
| `theme` | `theme="light" / "dark"` |
| `themeVars` | camelCase token 对象 |
| `--van-*` | `--color-*`、`--button-*` 等自研 CSS Variables |
| Vant 组件读取变量 | 自研组件读取 `var(--*)` |

自研示例：

```vue
<UiConfigProvider :theme="theme" :theme-vars="themeVars">
  <UiButton variant="primary">主要按钮</UiButton>
</UiConfigProvider>
```

对应变量转换：

```ts
const themeVars = {
  colorPrimary: '#2563eb',
  buttonPrimaryBg: 'var(--color-primary)',
  buttonPrimaryBorder: 'var(--color-primary)',
};
```

输出为：

```css
--color-primary: #2563eb;
--button-primary-bg: var(--color-primary);
--button-primary-border: var(--color-primary);
```

## 与其他体系对比

| 体系 | 颜色主题特点 |
| --- | --- |
| Vant 4 | CSS Variables + ConfigProvider，适合 Vue 3 移动端和 H5 组件主题 |
| TDesign | CSS Variables + Design Token，强调跨框架、多端统一 |
| Ant Design v5 | Seed Token + Map Token + Alias Token + CSS-in-JS，颜色算法强 |
| Element Plus | CSS Variables + Sass 变量，Vue 生态友好 |
| Naive UI | Theme Object + Vue Provider，运行时主题能力强 |

## 结论

Vant 4 颜色主题最值得借鉴的是：

| 能力 | 价值 |
| --- | --- |
| CSS Variables | 支持运行时主题切换，不需要重新构建 |
| ConfigProvider | 支持全局主题和局部主题作用域 |
| themeVars 命名规则 | 让 JS 配置和 CSS Variables 建立稳定映射 |
| 暗黑模式 | 通过 `theme="dark"` 切换组件整体视觉 |
| 组件级变量 | Button、Cell、Form 等组件可以单独覆盖 |
| 业务 token 映射 | 避免业务直接绑定组件库内部变量 |

对当前自研组件库而言，推荐保留这条链路：

```txt
业务 token
        ↓
UiConfigProvider themeVars
        ↓
CSS Variables
        ↓
UiButton / 后续自研组件
```
