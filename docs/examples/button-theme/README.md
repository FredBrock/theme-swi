# CSS Variables + SCSS 按钮组件示例

这个示例演示如何用 SCSS（Sass 样式语法）组织 Design Token（设计令牌），再输出 CSS Variables（CSS 变量）实现按钮组件主题切换。

## 文件说明

| 文件 | 作用 |
| --- | --- |
| `styles.scss` | 源 SCSS，包含 light / dark 主题 token、密度 token 和按钮样式 |
| `styles.css` | 已展开的 CSS，便于直接用浏览器打开示例 |
| `theme.js` | 切换 `data-theme` 和 `data-density`，并用 `localStorage` 持久化 |
| `index.html` | 按钮组件用法示例 |

## 实现思路

```txt
SCSS map 定义主题 token
        ↓
SCSS mixin 生成 CSS Variables
        ↓
按钮组件只读取 var(--*)
        ↓
JS 切换 data-theme / data-density
        ↓
按钮颜色、尺寸和状态自动更新
```

## 支持能力

| 能力 | 实现方式 |
| --- | --- |
| 亮色 / 暗色 | `data-theme="light"` / `data-theme="dark"` |
| 舒适 / 紧凑密度 | `data-density="comfortable"` / `data-density="compact"` |
| 按钮变体 | `ui-button--primary`、`ui-button--danger`、`ui-button--ghost` |
| 按钮尺寸 | `ui-button--sm`、默认、`ui-button--lg` |
| 禁用状态 | `disabled` 或 `aria-disabled="true"` |
| 首屏防闪烁 | `index.html` 中的内联初始化脚本先于 CSS 执行 |

## 关键约束

- 组件样式不要直接写死颜色，优先读取组件级变量，如 `--button-primary-bg`。
- 主题切换只修改根节点属性，不重写组件 class。
- 这个仓库当前没有构建配置，所以同时保留 `styles.scss` 和可直接预览的 `styles.css`。
