# Ant Design 颜色规范参考

## 来源

参考 Ant Design 官方色彩规范：https://ant.design/docs/spec/colors-cn

Ant Design 将色彩体系拆成两个层面：系统级色彩体系和产品级色彩体系。

```txt
系统级色彩体系
        ↓
产品级色彩体系
        ↓
Design Token（设计令牌）
        ↓
组件 Token
        ↓
组件样式
```

## 核心结构

| 层级 | 作用 | 内容 |
| --- | --- | --- |
| 系统级色彩体系 | 提供稳定、可复用的基础色彩资产 | 基础色板、中性色板、数据可视化色板 |
| 产品级色彩体系 | 将系统颜色映射到真实业务语义 | 品牌色、功能色、中性色 |
| 企业级色彩应用原则 | 约束颜色使用方式 | 克制、信息传递、操作引导、交互反馈 |

这套结构适合企业级中后台，因为它不仅定义颜色值，还明确颜色来源、生成方式、使用语义和业务边界。

## 色彩模型

Ant Design 设计团队倾向使用 HSB 色彩模型。

| 维度 | 含义 | 价值 |
| --- | --- | --- |
| Hue | 色相 | 控制颜色类别 |
| Saturation | 饱和度 | 控制颜色鲜艳程度 |
| Brightness | 明度 | 控制颜色明暗关系 |

HSB 更便于设计师在调整颜色时形成心理预期，也便于团队沟通 hover、active、disabled 等状态色的变化规律。

对组件库的启发：

```txt
不要手工拍脑袋定义 hover / active 色
应通过色阶、颜色算法或可解释规则生成状态色
```

## 系统级色彩体系

Ant Design 系统级色彩体系包括三类：

| 色板 | 作用 |
| --- | --- |
| 基础色板 | 提供品牌色、功能色、辅助色的来源 |
| 中性色板 | 支撑文本、背景、边框、分割线等信息层级 |
| 数据可视化色板 | 服务图表、分类数据和可视化表达 |

## 基础色板

Ant Design 基础色板包含 12 个主色，每个主色衍生 10 个色阶，共 120 个颜色。

| 中文名 | Token | 语义感受 |
| --- | --- | --- |
| 薄暮 | red | 斗志、奔放 |
| 火山 | volcano | 醒目、澎湃 |
| 日暮 | orange | 温暖、欢快 |
| 青柠 | lime | 自然、生机 |
| 金盏花 | gold | 活力、积极 |
| 日出 | yellow | 出生、阳光 |
| 极光绿 | green | 健康、创新 |
| 明青 | cyan | 希望、坚强 |
| 拂晓蓝 | blue | 包容、科技、普惠 |
| 极客蓝 | geekblue | 探索、钻研 |
| 酱紫 | purple | 优雅、浪漫 |
| 法式洋红 | magenta | 明快、感性 |

典型色阶：

```txt
blue-1
blue-2
blue-3
blue-4
blue-5
blue-6
blue-7
blue-8
blue-9
blue-10
```

Ant Design 建议从浅到深的第 6 个颜色作为主色。当前品牌主色是：

```txt
#1677ff
```

## 色板生成工具

Ant Design 提供 `@ant-design/colors` 供代码侧使用色板。

```bash
npm install @ant-design/colors
```

```ts
import { blue } from '@ant-design/colors';

console.log(blue);
// ['#E6F4FF', '#BAE0FF', '#91CAFF', '#69B1FF', '#4096FF', '#1677FF', '#0958D9', '#003EB3', '#002C8C', '#001D66']

console.log(blue.primary);
// '#1677FF'
```

这说明 Ant Design 的色板不是静态色值表，而是具备算法生成能力。

## 色阶用途

Ant Design 官方色彩规范强调通过主色生成完整衍生色。落到组件库时，可按以下方式理解色阶用途：

| 色阶 | 常见用途 |
| --- | --- |
| 1-2 | 浅背景、弱提示背景、Tag 背景 |
| 3-4 | 辅助背景、hover 背景、边框弱强调 |
| 5 | hover 状态 |
| 6 | default 主色 |
| 7 | active 状态 |
| 8-10 | 深色强调、深背景、暗色模式映射 |

自研组件库不一定要完全复制色阶映射，但需要保证 default、hover、active、focus、disabled、light background 都来自同一套可解释规则。

## 产品级色彩体系

产品级色彩体系把系统色板映射到真实产品语义中。

| 类型 | 作用 | 典型场景 |
| --- | --- | --- |
| 品牌色 | 表达产品特性和传播理念 | 关键行动点、操作状态、重要信息高亮、图形化 |
| 功能色 | 表达明确状态和反馈 | 成功、出错、失败、提醒、链接 |
| 中性色 | 构建信息层级 | 文本、背景、边框、分割线、禁用态 |

## 品牌色

Ant Design 的品牌色取自基础色板蓝色，第 6 色为主色。

```txt
colorPrimary: #1677ff
```

建议映射为一组完整语义 token：

```ts
const primaryTokens = {
  colorPrimaryBg: '#e6f4ff',
  colorPrimaryBgHover: '#bae0ff',
  colorPrimaryBorder: '#91caff',
  colorPrimaryBorderHover: '#69b1ff',
  colorPrimaryHover: '#4096ff',
  colorPrimary: '#1677ff',
  colorPrimaryActive: '#0958d9',
  colorPrimaryTextHover: '#4096ff',
  colorPrimaryText: '#1677ff',
  colorPrimaryTextActive: '#0958d9',
};
```

## 功能色

功能色代表稳定的信息和状态语义。Ant Design 强调一套产品体系下功能色应尽量保持一致，避免过多自定义干扰用户认知。

| 功能 | 建议 token | 语义 |
| --- | --- | --- |
| Success | `colorSuccess` | 成功、完成、正向反馈 |
| Warning | `colorWarning` | 警告、提醒、风险 |
| Error | `colorError` | 错误、失败、危险操作 |
| Info | `colorInfo` | 普通信息、辅助说明 |
| Link | `colorLink` | 可点击文本或跳转 |

## 中性色

Ant Design 的中性色大量用于文字，同时覆盖背景、边框、分割线等场景。官方强调中性色定义需要考虑深色背景、浅色背景和 WCAG 2.0 标准。

| 场景 | 浅色背景 | 深色背景 |
| --- | --- | --- |
| 标题字体 | `#000000E0` | `#FFFFFFD9` |
| 一级文本 | `#000000E0` | `#FFFFFFD9` |
| 二级文本 | `#000000A6` | `#FFFFFFA6` |
| 禁用字体 | `#00000040` | `#FFFFFF40` |
| 一级边框 | `#D9D9D9` | `#424242` |
| 分割线 | `#0505050F` | `#FDFDFD1F` |
| 布局背景 | `#F5F5F5` | `#000000` |

透明度表达层级是 Ant Design 中性色的重要特征，例如 `#000000E0` 等价于黑色约 88% 不透明度。

## 数据可视化色板

Ant Design 的数据可视化色板基于基础色板和中性色板，并融合 AntV 的原则。

UI 组件颜色和数据可视化颜色应区分使用：

| 用途 | 颜色来源 |
| --- | --- |
| 组件状态 | 品牌色、功能色、中性色 |
| 图表分类 | 数据可视化色板 |
| 业务状态 | 功能色或业务语义色 |
| 装饰插画 | 基础色板可更灵活使用 |

## 企业级色彩使用原则

Ant Design 对企业级产品的色彩态度是克制。颜色主要服务于：

```txt
信息传递
操作引导
交互反馈
```

应避免：

| 问题 | 影响 |
| --- | --- |
| 大面积使用高饱和颜色 | 干扰阅读和操作效率 |
| 品牌色滥用 | 削弱关键操作识别 |
| 功能色语义混乱 | 增加用户认知成本 |
| 图表色和状态色冲突 | 造成信息误读 |
| 弱文本对比度不足 | 影响可读性和 a11y（无障碍访问） |

## 与 Ant Design v5 Token 的关系

Ant Design v5 的主题体系可理解为：

```txt
Seed Token（种子令牌）
        ↓
Map Token（梯度令牌）
        ↓
Alias Token（别名令牌）
        ↓
Component Token（组件令牌）
```

示例：

```ts
const seedToken = {
  colorPrimary: '#1677ff',
};

const mapToken = {
  colorPrimaryBg: '#e6f4ff',
  colorPrimaryHover: '#4096ff',
  colorPrimary: '#1677ff',
  colorPrimaryActive: '#0958d9',
};

const aliasToken = {
  colorText: 'rgba(0, 0, 0, 0.88)',
  colorTextSecondary: 'rgba(0, 0, 0, 0.65)',
  colorBorder: '#d9d9d9',
  colorBgLayout: '#f5f5f5',
};

const buttonToken = {
  primaryColor: '#fff',
  primaryBg: 'var(--color-primary)',
  primaryHoverBg: 'var(--color-primary-hover)',
};
```

## 自研组件库参考实现

当前项目可以将 Ant Design 的颜色思想映射为 SCSS map + CSS Variables（CSS 变量）。

亮色主题示例：

```scss
$light-theme: (
  color-primary-bg: #e6f4ff,
  color-primary-bg-hover: #bae0ff,
  color-primary-border: #91caff,
  color-primary-border-hover: #69b1ff,
  color-primary-hover: #4096ff,
  color-primary: #1677ff,
  color-primary-active: #0958d9,
  color-primary-text-hover: #4096ff,
  color-primary-text: #1677ff,
  color-primary-text-active: #0958d9,

  color-success: #52c41a,
  color-warning: #faad14,
  color-error: #ff4d4f,
  color-info: #1677ff,

  color-text: rgba(0, 0, 0, 0.88),
  color-text-secondary: rgba(0, 0, 0, 0.65),
  color-text-tertiary: rgba(0, 0, 0, 0.45),
  color-text-disabled: rgba(0, 0, 0, 0.25),

  color-border: #d9d9d9,
  color-split: rgba(5, 5, 5, 0.06),
  color-bg-layout: #f5f5f5,
  color-bg-container: #ffffff,

  button-primary-bg: var(--color-primary),
  button-primary-bg-hover: var(--color-primary-hover),
  button-primary-bg-active: var(--color-primary-active),
  button-primary-text: #ffffff,
);
```

暗黑主题示例：

```scss
$dark-theme: (
  color-primary-bg: #111a2c,
  color-primary-bg-hover: #112545,
  color-primary-border: #15325b,
  color-primary-border-hover: #15417e,
  color-primary-hover: #3c89e8,
  color-primary: #1668dc,
  color-primary-active: #1554ad,

  color-text: rgba(255, 255, 255, 0.85),
  color-text-secondary: rgba(255, 255, 255, 0.65),
  color-text-tertiary: rgba(255, 255, 255, 0.45),
  color-text-disabled: rgba(255, 255, 255, 0.25),

  color-border: #424242,
  color-split: rgba(253, 253, 253, 0.12),
  color-bg-layout: #000000,
  color-bg-container: #141414,

  button-primary-bg: var(--color-primary),
  button-primary-bg-hover: var(--color-primary-hover),
  button-primary-bg-active: var(--color-primary-active),
  button-primary-text: #ffffff,
);
```

组件只读取 component token：

```scss
.ui-button--primary {
  --button-bg: var(--button-primary-bg);
  --button-bg-hover: var(--button-primary-bg-hover);
  --button-bg-active: var(--button-primary-bg-active);
  --button-text: var(--button-primary-text);
}
```

## 迁移到当前项目

当前项目已有 `UiConfigProvider + UiButton`，可以这样承接 Ant Design 颜色规范：

```txt
Ant Design 色阶和语义 token
        ↓
UiConfigProvider themeVars
        ↓
CSS Variables
        ↓
UiButton / 后续自研组件
```

示例：

```ts
const themeVars = {
  colorPrimary: '#1677ff',
  colorPrimaryHover: '#4096ff',
  colorPrimaryActive: '#0958d9',
  buttonPrimaryBg: 'var(--color-primary)',
  buttonPrimaryBgHover: 'var(--color-primary-hover)',
  buttonPrimaryBgActive: 'var(--color-primary-active)',
  buttonPrimaryText: '#ffffff',
};
```

## 与其他体系对比

| 体系 | 颜色设计特点 |
| --- | --- |
| Ant Design | 色板算法强，系统级色板 + 产品级语义，适合企业中后台 |
| TDesign | CSS Variables + Design Token，强调跨框架、多端统一 |
| Vant 4 | CSS Variables + ConfigProvider，适合移动端 / H5 Vue 组件 |
| Carbon | 中性色和可访问性约束严谨，适合复杂企业系统 |
| Material Design | 颜色角色和动态色体系完整，适合跨平台产品 |

## 结论

Ant Design 颜色规范最值得借鉴的是：

| 能力 | 价值 |
| --- | --- |
| 系统级 / 产品级分层 | 区分颜色资产和业务语义 |
| 12 色基础色板 | 覆盖企业中后台常见颜色需求 |
| 第 6 色主色原则 | 给品牌主色选择提供稳定规则 |
| 颜色生成算法 | 状态色可推导，减少主观色值 |
| 中性色透明度体系 | 支撑文本层级、边框、分割线和深浅色模式 |
| 数据可视化色板分离 | 避免图表颜色和状态颜色冲突 |
| 克制使用原则 | 保证企业级产品的信息效率和操作效率 |

对当前自研组件库，建议重点采用：

```txt
基础色板 / 中性色板 / 数据可视化色板分离
品牌色 / 功能色 / 中性色分层
主色第 6 色原则
hover / active / bg / border 由色阶生成
组件只读取 semantic token 或 component token
暗黑模式重新映射 token
```
