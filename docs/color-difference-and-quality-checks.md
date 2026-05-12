# 色差与颜色质量校验

## 核心概念

色差和质量校验用于判断一组颜色是否可用、是否一致、是否可感知、是否符合无障碍访问（a11y）要求。

```txt
色差 = 两个颜色在人眼感知上的差异有多大
质量校验 = 检查一组颜色 token 是否适合真实 UI 使用
```

它不是只靠主观判断“看起来差不多”，而是用规则和算法检查 Design Token（设计令牌）的可靠性。

## 色差是什么

色差用于衡量两个颜色之间的视觉差异。

例如：

```txt
#1677ff 和 #4096ff
```

它们都属于蓝色，但一个更深，一个更亮。色差就是衡量它们“看起来差多少”。

常见色差指标是 Delta E，也写作 `ΔE`。

| Delta E | 人眼感知 |
| --- | --- |
| `< 1` | 几乎不可察觉 |
| `1 - 2` | 很难察觉 |
| `2 - 5` | 可以察觉，但差异较小 |
| `5 - 10` | 差异明显 |
| `> 10` | 差异很明显 |

在组件库中，色差常用于检查：

```txt
hover 色和 default 色是否区分明显
active 色是否比 default 有足够反馈
disabled 色是否明显弱化
相邻色阶是否变化均匀
不同品牌主题的层级是否一致
```

## 为什么不用 RGB 差值

RGB 数值差异不等于人眼感知差异。

例如：

```css
hsl(60 100% 50%)
hsl(240 100% 50%)
```

这两个颜色的 Lightness 都是 50%，但黄色看起来明显比蓝色更亮。

因此色差通常不直接使用 RGB 距离，而是基于更接近人眼感知的颜色空间：

```txt
CIELAB
OKLab
OKLCH
```

## Delta E

Delta E 是基于感知颜色空间计算颜色差异的方法。

| 名称 | 说明 |
| --- | --- |
| ΔE76 | 最早版本，计算简单 |
| ΔE94 | 改进视觉感知权重 |
| ΔE2000 | 更准确，常用于专业色彩管理 |
| OKLab distance | 现代 Web 主题系统中也可用于近似感知差异 |

概念流程：

```txt
把颜色转换到 Lab / OKLab 空间
        ↓
计算两个颜色之间的距离
        ↓
得到色差值
```

伪代码：

```ts
const diff = deltaE('#1677ff', '#4096ff');

if (diff < 5) {
  console.warn('hover 色和 default 色差异可能不明显');
}
```

## 质量校验是什么

质量校验不是只看单个颜色是否好看，而是检查一组颜色 token 是否能支撑真实 UI。

| 校验项 | 检查什么 |
| --- | --- |
| 色差校验 | 状态色、相邻色阶是否有足够差异 |
| 对比度校验 | 文本和背景是否符合 WCAG |
| 色阶均匀性 | 从浅到深是否平滑、不跳变 |
| 语义一致性 | success / warning / error 是否符合用户认知 |
| 暗黑模式适配 | 暗色背景下是否刺眼、发灰或不可读 |
| 禁用态可识别性 | disabled 是否明显不可交互，但仍可读 |
| 品牌一致性 | 多品牌主题是否保持相似视觉层级 |
| 组件状态完整性 | default / hover / active / focus / disabled 是否齐全 |
| 数据可视化可区分性 | 图表颜色之间是否能区分 |
| 色盲友好性 | 红绿、蓝紫等组合是否容易混淆 |

## 色差与对比度的区别

色差和对比度不是一回事。

| 项目 | 色差 Delta E | 对比度 Contrast Ratio |
| --- | --- | --- |
| 关注点 | 两个颜色看起来差多少 | 文本和背景是否读得清 |
| 常用空间 | Lab / OKLab | 相对亮度 |
| 典型用途 | hover 和 default 差异、色阶均匀性 | 文本可读性、a11y |
| 结果形式 | 差异值 | 比值，如 `4.5:1` |
| 标准来源 | 色彩科学经验 | WCAG |

使用建议：

```txt
hover 色和 default 色：更适合用色差判断是否有明显反馈
按钮文字和按钮背景：必须用对比度判断是否可读
```

## WCAG 对比度要求

文本和背景应使用 WCAG Contrast Ratio（对比度）检查。

| 内容 | 最低要求 |
| --- | --- |
| 正文文本 | `4.5:1` |
| 大字号文本 | `3:1` |
| 非文本 UI 图形 / 控件边界 | `3:1` |
| AAA 正文文本 | `7:1` |

例如按钮需要检查：

```txt
白色文字 #ffffff
蓝色背景 #1677ff
```

是否满足：

```txt
contrast(#ffffff, #1677ff) >= 4.5:1
```

## Button 校验示例

以 Button（按钮）为例，需要检查每个状态。

| 状态 | 校验 |
| --- | --- |
| default | 文本 / 背景对比度是否达标 |
| hover | 和 default 是否有足够色差 |
| active | 和 default / hover 是否有清晰差异 |
| focus | focus ring 和背景是否可见 |
| disabled | 是否弱化，但文字仍可读 |
| danger | 是否符合危险语义，文字对比度是否达标 |
| dark mode | 所有状态在暗色背景下是否可读 |

Primary Button token 示例：

```txt
button-primary-bg: color-primary
button-primary-bg-hover: color-primary-hover
button-primary-bg-active: color-primary-active
button-primary-text: #ffffff
```

需要校验：

```txt
contrast(button-primary-text, button-primary-bg) >= 4.5
contrast(button-primary-text, button-primary-bg-hover) >= 4.5
contrast(button-primary-text, button-primary-bg-active) >= 4.5

deltaE(color-primary, color-primary-hover) >= 阈值
deltaE(color-primary, color-primary-active) >= 阈值
```

## 色阶质量校验

如果生成一组色阶：

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

需要检查：

```txt
是否从浅到深单调变化
相邻色阶是否差异太小
某一步是否突然跳变
中间主色是否足够稳定
浅色背景是否过淡到不可见
深色阶是否过黑、脏或偏色
```

可用规则：

```txt
Lightness 应从高到低稳定变化
相邻 Delta E 不应过小
相邻 Delta E 不应突然过大
Chroma 不应在浅色或深色处失控
```

伪代码：

```ts
const palette = [
  '#e6f4ff',
  '#bae0ff',
  '#91caff',
  '#69b1ff',
  '#4096ff',
  '#1677ff',
  '#0958d9',
  '#003eb3',
  '#002c8c',
  '#001d66',
];

for (let i = 1; i < palette.length; i++) {
  const diff = deltaE(palette[i - 1], palette[i]);

  if (diff < 4) {
    console.warn(`色阶 ${i} 和 ${i + 1} 差异过小`);
  }

  if (diff > 18) {
    console.warn(`色阶 ${i} 和 ${i + 1} 跳变过大`);
  }
}
```

## 暗黑模式质量校验

暗黑模式常见问题：

```txt
背景纯黑，视觉过硬
主色太暗，看不清
主色太亮，刺眼
边框太弱，容器边界消失
文本透明度太低，阅读困难
hover / active 状态差异不明显
阴影在暗色背景下失效
```

需要检查：

| 校验项 | 目标 |
| --- | --- |
| 文本 / 背景对比度 | 可读 |
| 容器 / 页面背景差异 | 能分层 |
| 边框 / 背景对比度 | 能识别边界 |
| primary / dark background | 主色可见但不刺眼 |
| hover / active 差异 | 有交互反馈 |
| disabled | 弱化但不完全消失 |

## 多品牌主题质量校验

多品牌主题不能只检查颜色是否符合品牌，还要检查视觉层级是否一致。

例如：

```txt
blue theme 的 primary 很强
green theme 的 primary 偏淡
purple theme 的 hover 和 default 几乎没区别
red theme 的 active 太重，像 error
```

应检查：

```txt
主色视觉强度是否接近
hover / active 差异是否接近
文字对比度是否都达标
浅背景是否都有可见边界
暗黑模式是否都可读
```

OKLCH / HCT 的价值在于能更好地控制感知明度和彩度，从而让不同品牌主题保持相近层级。

## 常见阈值建议

这些阈值不是绝对标准，但适合作为组件库初始规则。

| 校验 | 建议阈值 |
| --- | --- |
| 正文文本对比度 | `>= 4.5:1` |
| 大字号文本对比度 | `>= 3:1` |
| UI 控件边界对比度 | `>= 3:1` |
| hover 和 default 色差 | Delta E `>= 4` |
| active 和 default 色差 | Delta E `>= 6` |
| 相邻色阶 Delta E | 约 `4 - 18` |
| disabled 文本对比度 | 可低于正文，但不应完全不可读 |
| focus ring 对比度 | 建议 `>= 3:1` |

实际阈值需要结合具体视觉风格和产品场景调整。

## 当前项目落地思路

当前项目已有：

```txt
UiConfigProvider
        ↓
themeVars
        ↓
UiButton
        ↓
CSS Variables
```

后续可以增加 token 检查脚本：

```txt
themeVars
        ↓
解析颜色
        ↓
检查 contrast
        ↓
检查 Delta E
        ↓
输出 warning / error
```

建议优先检查：

```txt
buttonPrimaryText vs buttonPrimaryBg
buttonPrimaryText vs buttonPrimaryBgHover
buttonPrimaryText vs buttonPrimaryBgActive

colorPrimary vs colorPrimaryHover
colorPrimary vs colorPrimaryActive

colorText vs colorBgContainer
colorBorder vs colorBgContainer
```

伪代码：

```ts
validateTheme({
  colorText: '#111827',
  colorBgContainer: '#ffffff',
  colorPrimary: '#1677ff',
  colorPrimaryHover: '#4096ff',
  colorPrimaryActive: '#0958d9',
  buttonPrimaryText: '#ffffff',
  buttonPrimaryBg: '#1677ff',
});
```

输出示例：

```txt
PASS contrast(buttonPrimaryText, buttonPrimaryBg): 4.8
PASS deltaE(colorPrimary, colorPrimaryHover): 8.2
WARN deltaE(colorPrimary, colorPrimaryActive): 3.1，active 状态差异可能不明显
```

## 结论

| 概念 | 作用 |
| --- | --- |
| 色差 | 判断两个颜色是否看得出差异 |
| 对比度 | 判断文字和背景是否读得清 |
| 质量校验 | 综合检查色阶、状态、暗黑模式、多品牌和 a11y |

对组件库主题系统来说，建议将色差和质量校验放在 token 生成或发布检查阶段，而不是放进组件运行时。
