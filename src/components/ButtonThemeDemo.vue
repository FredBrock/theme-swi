<template>
  <UiConfigProvider class="button-theme-shell" :theme="theme" :density="density" :theme-vars="brandThemeVars">
    <main class="button-theme-demo">
      <section class="demo-card">
        <h1 class="demo-title">CSS Variables + SCSS + ConfigProvider 按钮组件</h1>
        <p class="demo-text">
          自研 <code>UiConfigProvider</code> 负责输出 CSS Variables（CSS 变量），
          <code>UiButton</code> 只读取 token（设计令牌）并通过 props 控制变体和尺寸。
        </p>
        <div class="demo-actions">
          <UiButton variant="primary" @click="toggleTheme">
            {{ themeButtonText }}
          </UiButton>
          <UiButton @click="toggleDensity">
            {{ densityButtonText }}
          </UiButton>
        </div>
      </section>

      <section class="demo-card" aria-label="按钮变体">
        <p class="demo-text">变体</p>
        <div class="demo-actions">
          <UiButton variant="primary">Primary</UiButton>
          <UiButton>Secondary</UiButton>
          <UiButton variant="danger">Danger</UiButton>
          <UiButton variant="ghost">Ghost</UiButton>
          <UiButton disabled>Disabled</UiButton>
          <UiButton variant="primary" loading>Loading</UiButton>
        </div>
      </section>

      <section class="demo-card" aria-label="按钮尺寸">
        <p class="demo-text">尺寸</p>
        <div class="demo-actions">
          <UiButton variant="primary" size="sm">Small</UiButton>
          <UiButton variant="primary">Medium</UiButton>
          <UiButton variant="primary" size="lg">Large</UiButton>
        </div>
      </section>

      <section class="demo-card" aria-label="局部品牌变量覆盖">
        <p class="demo-text">局部品牌变量覆盖</p>
        <UiConfigProvider :theme="theme" :density="density" :theme-vars="dangerThemeVars">
          <div class="demo-actions">
            <UiButton variant="primary">局部 Primary</UiButton>
            <UiButton variant="ghost">局部 Ghost</UiButton>
          </div>
        </UiConfigProvider>
      </section>
    </main>
  </UiConfigProvider>
</template>

<script lang="ts">
import Vue from 'vue';
import UiButton from '@/components/ui/UiButton.vue';
import UiConfigProvider from '@/components/ui/UiConfigProvider.vue';

type Theme = 'light' | 'dark';
type Density = 'comfortable' | 'compact';
type ThemeVars = Record<string, string>;

const THEME_KEY = 'button-demo-theme';
const DENSITY_KEY = 'button-demo-density';

function getSavedValue<T extends string>(key: string, values: T[]): T | null {
  const value = window.localStorage.getItem(key);

  return values.includes(value as T) ? value as T : null;
}

function getPreferredTheme(): Theme {
  if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
    return 'dark';
  }

  return 'light';
}

export default Vue.extend({
  name: 'ButtonThemeDemo',
  components: {
    UiButton,
    UiConfigProvider,
  },
  data() {
    return {
      theme: 'light' as Theme,
      density: 'comfortable' as Density,
      brandThemeVars: {
        colorPrimary: '#2563eb',
        buttonPrimaryBg: 'var(--mc-color-primary)',
        buttonPrimaryBorder: 'var(--mc-color-primary)',
      } as ThemeVars,
      dangerThemeVars: {
        colorPrimary: '#dc2626',
        colorPrimaryHover: '#b91c1c',
        colorPrimaryActive: '#991b1b',
        buttonPrimaryBg: 'var(--mc-color-primary)',
        buttonPrimaryBgHover: 'var(--mc-color-primary-hover)',
        buttonPrimaryBgActive: 'var(--mc-color-primary-active)',
        buttonPrimaryBorder: 'var(--mc-color-primary)',
      } as ThemeVars,
    };
  },
  computed: {
    themeButtonText(): string {
      return this.theme === 'dark' ? '切换到亮色' : '切换到暗色';
    },
    densityButtonText(): string {
      return this.density === 'compact' ? '切换到舒适密度' : '切换到紧凑密度';
    },
  },
  mounted() {
    this.theme = getSavedValue<Theme>(THEME_KEY, ['light', 'dark']) || getPreferredTheme();
    this.density = getSavedValue<Density>(DENSITY_KEY, ['comfortable', 'compact']) || 'comfortable';
  },
  methods: {
    toggleTheme() {
      this.theme = this.theme === 'dark' ? 'light' : 'dark';
      window.localStorage.setItem(THEME_KEY, this.theme);
    },
    toggleDensity() {
      this.density = this.density === 'compact' ? 'comfortable' : 'compact';
      window.localStorage.setItem(DENSITY_KEY, this.density);
    },
  },
});
</script>

<style lang="scss">
.button-theme-shell {
  min-height: calc(100vh - 81px);
}

.button-theme-demo {
  display: grid;
  gap: 24px;
  max-width: 760px;
  margin: 0 auto;
  padding: 48px 20px;
  text-align: left;
}

.demo-card {
  display: grid;
  gap: 16px;
  padding: 24px;
  border: 1px solid var(--mc-color-border);
  border-radius: var(--mc-radius-md);
  background: var(--mc-color-surface);
}

.demo-title {
  margin: 0;
  font-size: 28px;
  line-height: 1.2;
}

.demo-text {
  margin: 0;
  color: var(--mc-color-text-muted);
}

.demo-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

@media (max-width: 640px) {
  .button-theme-demo {
    padding: 32px 16px;
  }

  .demo-card {
    padding: 20px;
  }
}
</style>
