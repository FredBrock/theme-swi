<template>
  <main class="root-theme-demo">
    <section class="root-hero">
      <div>
        <p class="root-kicker">:root + SCSS + CSS Variables</p>
        <h1>全局主题变量演示</h1>
        <p>
          这个页面直接切换 <code>document.documentElement</code> 上的
          <code>data-theme</code> 和 <code>data-density</code>，验证
          <code>src/styles/theme.scss</code> 输出的全局 CSS Variables（CSS 变量）。
        </p>
      </div>
      <div class="root-controls" aria-label="全局主题控制">
        <button class="control-button" type="button" @click="toggleTheme">
          {{ theme === 'dark' ? '切换到 Light' : '切换到 Dark' }}
        </button>
        <button class="control-button" type="button" @click="toggleDensity">
          {{ density === 'compact' ? '切换到 Comfortable' : '切换到 Compact' }}
        </button>
      </div>
    </section>

    <section class="demo-grid">
      <article class="demo-panel">
        <h2>Semantic Token</h2>
        <p>普通 SCSS class 直接读取 <code>var(--mc-color-*)</code>。</p>
        <div class="swatch-grid">
          <div v-for="token in semanticTokens" :key="token.name" class="swatch-row">
            <span class="swatch" :style="{ background: token.value }" />
            <code>{{ token.name }}</code>
            <strong>{{ token.value }}</strong>
          </div>
        </div>
      </article>

      <article class="demo-panel surface-preview">
        <h2>普通页面样式</h2>
        <p>
          这个卡片没有 Provider 包裹，只依赖 <code>:root</code> 上的变量。
        </p>
        <div class="preview-card">
          <span class="preview-badge">Global</span>
          <h3>全局变量驱动</h3>
          <p>背景、文字、边框、强调色都来自 <code>var(--*)</code>。</p>
        </div>
      </article>

      <article class="demo-panel">
        <h2>Component Token</h2>
        <p><code>UiButton</code> 继续读取 <code>var(--mc-button-*)</code>，不关心变量来自全局还是局部。</p>
        <div class="button-stack">
          <UiButton variant="primary">Primary</UiButton>
          <UiButton>Secondary</UiButton>
          <UiButton variant="danger">Danger</UiButton>
          <UiButton variant="ghost">Ghost</UiButton>
          <UiButton variant="primary" size="sm">Small</UiButton>
          <UiButton variant="primary" size="lg">Large</UiButton>
        </div>
      </article>

      <article class="demo-panel">
        <h2>局部 Provider 覆盖</h2>
        <p>局部 <code>UiConfigProvider</code> 覆盖主色，不影响页面其它区域。</p>
        <UiConfigProvider :theme="theme" :density="density" :theme-vars="localThemeVars">
          <div class="local-provider-card">
            <h3>Local Orange Theme</h3>
            <p>这里的 primary 来自局部 inline CSS Variables。</p>
            <div class="button-stack">
              <UiButton variant="primary">Local Primary</UiButton>
              <UiButton variant="ghost">Local Ghost</UiButton>
            </div>
          </div>
        </UiConfigProvider>
      </article>
    </section>
  </main>
</template>

<script lang="ts">
import Vue from 'vue';
import UiButton from '@/components/ui/UiButton.vue';
import UiConfigProvider from '@/components/ui/UiConfigProvider.vue';

type Theme = 'light' | 'dark';
type Density = 'comfortable' | 'compact';
type ThemeVars = Record<string, string>;
type TokenItem = {
  name: string;
  value: string;
};

const THEME_KEY = 'root-demo-theme';
const DENSITY_KEY = 'root-demo-density';

function getSavedValue<T extends string>(key: string, values: T[]): T | null {
  const value = window.localStorage.getItem(key);

  return values.includes(value as T) ? value as T : null;
}

export default Vue.extend({
  name: 'RootThemeDemo',
  components: {
    UiButton,
    UiConfigProvider,
  },
  data() {
    return {
      theme: 'light' as Theme,
      density: 'comfortable' as Density,
      localThemeVars: {
        colorPrimary: '#d44700',
        colorPrimaryHover: '#ff8c61',
        colorPrimaryActive: '#aa3700',
        colorPrimaryBg: '#fffbff',
        colorPrimaryBorder: '#ffb59b',
        buttonPrimaryBg: 'var(--mc-color-primary)',
        buttonPrimaryBgHover: 'var(--mc-color-primary-hover)',
        buttonPrimaryBgActive: 'var(--mc-color-primary-active)',
        buttonPrimaryBorder: 'var(--mc-color-primary)',
      } as ThemeVars,
    };
  },
  computed: {
    semanticTokens(): TokenItem[] {
      return [
        { name: '--mc-color-primary', value: 'var(--mc-color-primary)' },
        { name: '--mc-color-primary-hover', value: 'var(--mc-color-primary-hover)' },
        { name: '--mc-color-primary-active', value: 'var(--mc-color-primary-active)' },
        { name: '--mc-color-bg', value: 'var(--mc-color-bg)' },
        { name: '--mc-color-surface', value: 'var(--mc-color-surface)' },
        { name: '--mc-color-text', value: 'var(--mc-color-text)' },
        { name: '--mc-color-border', value: 'var(--mc-color-border)' },
      ];
    },
  },
  mounted() {
    this.theme = getSavedValue<Theme>(THEME_KEY, ['light', 'dark']) || 'light';
    this.density = getSavedValue<Density>(DENSITY_KEY, ['comfortable', 'compact']) || 'comfortable';
    this.applyRootAttrs();
  },
  beforeDestroy() {
    document.documentElement.removeAttribute('data-theme');
    document.documentElement.removeAttribute('data-density');
  },
  methods: {
    toggleTheme() {
      this.theme = this.theme === 'dark' ? 'light' : 'dark';
      window.localStorage.setItem(THEME_KEY, this.theme);
      this.applyRootAttrs();
    },
    toggleDensity() {
      this.density = this.density === 'compact' ? 'comfortable' : 'compact';
      window.localStorage.setItem(DENSITY_KEY, this.density);
      this.applyRootAttrs();
    },
    applyRootAttrs() {
      document.documentElement.dataset.theme = this.theme;
      document.documentElement.dataset.density = this.density;
    },
  },
});
</script>

<style lang="scss">
.root-theme-demo {
  min-height: calc(100vh - 81px);
  padding: 48px 20px;
  background: var(--mc-color-bg);
  color: var(--mc-color-text);
  text-align: left;
}

.root-hero,
.demo-panel {
  max-width: 1120px;
  margin: 0 auto;
  border: 1px solid var(--mc-color-border);
  border-radius: 20px;
  background: var(--mc-color-surface);
}

.root-hero {
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto;
  gap: 24px;
  align-items: center;
  padding: 30px;
}

.root-kicker {
  margin: 0 0 10px;
  color: var(--mc-color-primary);
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.root-hero h1,
.demo-panel h2,
.preview-card h3,
.local-provider-card h3 {
  margin: 0;
  color: var(--mc-color-text);
}

.root-hero h1 {
  font-size: 34px;
  line-height: 1.15;
}

.root-hero p,
.demo-panel p,
.preview-card p,
.local-provider-card p {
  color: var(--mc-color-text-muted);
  line-height: 1.7;
}

.root-controls,
.button-stack {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.control-button {
  min-height: var(--mc-button-height-md);
  padding: 0 var(--mc-button-padding-x-md);
  border: 1px solid var(--mc-color-primary);
  border-radius: var(--mc-radius-md);
  background: var(--mc-color-primary);
  color: var(--mc-button-primary-text);
  font: inherit;
  font-weight: 700;
  cursor: pointer;
}

.control-button:hover {
  background: var(--mc-color-primary-hover);
}

.demo-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 20px;
  max-width: 1120px;
  margin: 20px auto 0;
}

.demo-panel {
  display: grid;
  gap: 18px;
  padding: 24px;
}

.swatch-grid {
  display: grid;
  gap: 10px;
}

.swatch-row {
  display: grid;
  grid-template-columns: 32px minmax(180px, 1fr) minmax(120px, auto);
  gap: 12px;
  align-items: center;
  padding: 10px;
  border: 1px solid var(--mc-color-border);
  border-radius: 12px;
}

.swatch {
  width: 28px;
  height: 28px;
  border: 1px solid var(--mc-color-border);
  border-radius: 999px;
}

.swatch-row code,
.swatch-row strong {
  color: var(--mc-color-text);
}

.preview-card,
.local-provider-card {
  display: grid;
  gap: 10px;
  padding: 22px;
  border: 1px solid var(--mc-color-primary-border);
  border-radius: 16px;
  background: var(--mc-color-primary-bg);
}

.preview-badge {
  width: max-content;
  padding: 4px 10px;
  border-radius: 999px;
  background: var(--mc-color-primary);
  color: var(--mc-button-primary-text);
  font-size: 12px;
  font-weight: 700;
}

@media (max-width: 860px) {
  .root-theme-demo {
    padding: 32px 16px;
  }

  .root-hero,
  .demo-grid {
    grid-template-columns: 1fr;
  }

  .root-hero h1 {
    font-size: 28px;
  }

  .swatch-row {
    grid-template-columns: 32px 1fr;
  }

  .swatch-row strong {
    grid-column: 2;
  }
}
</style>
