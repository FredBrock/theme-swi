# AGENTS.md

## 项目实况

- 这是 Vue 2 + Vue CLI 5 + TypeScript 项目，不是 documentation-only workspace（仅文档工作区）。入口是 `src/main.ts`，挂载 `App.vue`，并接入 `src/router/index.ts` 和 `src/store/index.ts`。
- 包管理以 pnpm 为准：仓库有 `pnpm-lock.yaml`，`.npmrc` 设置了 `shamefully-hoist=true` 和 `strict-peer-dependencies=false`。
- `@/*` 路径别名指向 `src/*`，见 `tsconfig.json`；单测中也使用该别名。

## 常用命令

- 安装依赖：`pnpm install`
- 本地开发：`pnpm run serve`
- 生产构建：`pnpm run build`
- 单元测试：`pnpm run test:unit`
- 代码检查并自动修复：`pnpm run lint`
- 运行单个 Jest 测试文件可用 Vue CLI 透传参数，例如：`pnpm run test:unit -- tests/unit/example.spec.ts`

## 代码与测试

- Vue 单文件组件使用 Vue 2 Options API（`Vue.extend`）和 `<script lang="ts">`；样式已有 SCSS（`<style lang="scss">` / `scoped lang="scss"`）。
- Router 使用 Vue Router 3，当前是 `history` mode（历史模式），base 来自 `process.env.BASE_URL`。
- Vuex 3 store 当前只有空的 `state/getters/mutations/actions/modules`，不要假设已有业务状态模型。
- Jest 配置来自 `@vue/cli-plugin-unit-jest/presets/typescript-and-babel`；测试文件位于 `tests/unit/**/*.spec.ts`，使用 `@vue/test-utils` v1。

## 文档与示例

- `docs/` 不是唯一工作区，但包含主题系统调研：`ui-component-libraries-research.md`、`design-systems-research.md`、`theme-switching-implementation-research.md`。
- `docs/examples/button-theme/` 是独立的 CSS Variables + SCSS 主题切换示例；同时保留源 `styles.scss` 和可直接浏览器预览的 `styles.css`。
- 更新调研文档时，优先更新现有表格或追加已验证的小节，避免创建重复清单。

## 组件库与设计系统视角

- 处理组件库、theme system（主题系统）或 design system（设计系统）任务时，以资深 Web 组件库开发者视角评估方案。
- 优先关注组件 API 边界、Design Token（设计令牌）分层、CSS Variables（CSS 变量）主题切换、暗黑模式、多品牌扩展、无障碍访问（a11y）、国际化、测试和文档交付。
- 输出建议应结构化且可落地；必要时给出组件 API、token 示例、样式方案取舍或工程化验证步骤。

## 验证约束

- 没有单独的 `typecheck`、formatter（格式化）或 CI workflow（持续集成工作流）配置；不要臆造 `pnpm typecheck`、`pnpm format` 等命令。
- 代码改动优先跑相关命令：`pnpm run test:unit`、`pnpm run lint`、必要时 `pnpm run build`。
- 仅改 Markdown（标记文档）时，通过阅读修改内容并手动检查 links（链接）和 names（名称）验证即可。
