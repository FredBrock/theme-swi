# AGENTS.md

## 仓库结构

- 当前是一个 documentation-only workspace（仅文档工作区）：根目录只有 `docs/`，没有 package manifest（包清单）、build config（构建配置）、test config（测试配置）、CI workflows（持续集成工作流）或 source code（源码）。
- 后续指令应保持精简；在仓库中出现可执行配置之前，不要臆造命令。

## 文档

- 主要调研文件位于 `docs/`：
  - `docs/ui-component-libraries-research.md`
  - `docs/design-systems-research.md`
- 这些文件是关于 UI component libraries（界面组件库）、theme systems（主题系统）和 Design System（设计系统）选型的 Markdown（标记文档）调研笔记。
- 更新调研内容时，优先追加简洁且已验证的章节，或更新现有表格，避免重复创建高度相似的列表。

## 验证

- 当前没有仓库本地的 build（构建）、lint（代码检查）、formatter（格式化）、typecheck（类型检查）或 test（测试）命令可运行。
- 对于文档编辑，通过阅读已修改的 Markdown（标记文档），并手动检查 links（链接）和 names（名称）来验证。
