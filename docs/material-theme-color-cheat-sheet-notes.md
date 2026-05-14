# Material Theme Color Cheat Sheet 解析

## 文档目的

将 `public/cheat_sheet.png` 的内容结构化为可落地的 theme system（主题系统）说明，便于在组件库和 Design System（设计系统）中复用。

## 一、从图片提取主题色

目标：`I want good colors for theming...`

### 1) Quantize（颜色量化）

- 定义：将 wallpaper（壁纸）压缩为 `N colors`（N 个代表色）。
- 过程：图中提到 `Celebi`、`Wu`、`WSMeans`（量化/聚类算法链路）。
- 作用：把高维像素信息降维为候选颜色集合。

### 2) Score（颜色评分）

- 定义：对候选颜色按 suitability for theming（主题适配性）排序。
- 过程：先做 quantize buckets（分桶，例如 128 colors），再去重与排序。
- 作用：避免“只按出现频率选色”，提高主题可读性与可用性。

### 输入与输出

```txt
from a picture（来自图片） -> Quantize
from a set of colors（来自颜色集合） -> Score
```

## 二、给定一个颜色，生成完整主题能力

目标：`Given a color, give me a...`

### 1) Scheme（语义配色方案）

- 定义：role names（角色名，如 `primary`）到颜色的映射。
- 输出：`Color scheme`（可直接消费的语义主题色）。
- 特点：高层抽象，易用，能确保 consistent design language（一致设计语言）。

### 2) Palettes（色板）

- `Tonal Palette`（单色相多明度/色调的色阶集合）。
- `Core Palette`（生成 Material Color Scheme 所需的多组 tonal palettes）。
- 输出：一组可满足 contrast（对比度）要求的颜色集合。

### 3) HCT（Hue Chroma Tone）

- 含义：
  - `Hue`（色相）
  - `Chroma`（彩度/色彩丰富度）
  - `Tone`（明度/亮度感）
- 特性：基于 `CAM16 x L*`，并考虑 viewing conditions（观察条件）。
- 作用：为动态主题生成提供更接近感知一致性的颜色基础。

### 4) Blend（颜色混合/调和）

- 定义：color interpolation in HCT（在 HCT 空间做颜色插值）。
- 用途：harmonizing（色彩协调）、animations（动画过渡）、gradients（渐变）。
- 结果：可将一个颜色的 hue 向主题 hue 方向偏移，实现视觉统一。

## 三、抽象层级与工程取舍

图中给出从高层到低层的梯度：

- 高层：very easy to use（易用），ensures consistent design language（一致性更好）。
- 低层：requires full understanding（需完整色彩系统认知），工作量更高、风险更大。

对应建议：

- 业务与组件消费层优先使用 `Scheme`。
- 设计系统维护层可下探到 `Palettes`。
- 算法/基础设施层再使用 `HCT` 与 `Blend`。

## 四、推荐落地链路（组件库视角）

```txt
Image（图片）
  -> Quantize（候选色提取）
  -> Score（候选色排序）
  -> Seed Color（种子色）
  -> HCT（感知色彩建模）
  -> Tonal/Core Palettes（色板）
  -> Scheme（语义角色色）
  -> CSS Variables（主题变量）
  -> Components（组件消费）
```

## 五、对当前仓库的实现建议

- 变量分层：`seed -> palette -> semantic -> component`（种子层 -> 色板层 -> 语义层 -> 组件层）。
- 运行时切换：通过 `[data-theme]` 或 `.dark` 覆盖 `CSS Variables`。
- 组件约束：组件仅消费语义变量（如 `--color-primary`、`--color-surface`），不直接依赖 HCT 参数。
- 质量保障：对文本/背景对比度进行自动校验，避免动态生成后可读性下降。

## 六、关键信息速记

- `Quantize`：从图片得到“候选色”。
- `Score`：从候选色得到“更适合主题的种子色”。
- `Scheme`：从色板得到“可直接使用的语义主题”。
- `Palettes`：提供满足对比度和层级关系的色阶基础。
- `HCT`：提供感知友好的底层颜色参数化能力。
- `Blend`：提供主题调和与动态过渡能力。
