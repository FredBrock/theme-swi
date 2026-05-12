<template>
  <UiConfigProvider class="hct-palette-shell" :theme-vars="selectedPalette.themeVars">
    <main class="hct-palette-demo">
      <section class="hct-hero">
        <div>
          <p class="hct-kicker">Material HCT Tonal Palette</p>
          <h1 class="hct-title">{{ selectedPalette.seed }} 色阶颜色面板</h1>
          <p class="hct-text">
            由 <code>scripts/create_hct_theme_vars.py</code> 调用 Material Color Utilities 生成。
            HCT 信息：Hue {{ selectedPalette.hct.hue }} / Chroma {{ selectedPalette.hct.chroma }} / Tone {{ selectedPalette.hct.tone }}。
          </p>
          <div class="seed-selector" aria-label="选择 seed color">
            <button
              v-for="palette in palettes"
              :key="palette.seed"
              class="seed-option"
              :class="{ 'seed-option--active': palette.seed === selectedSeed }"
              type="button"
              @click="selectedSeed = palette.seed"
            >
              <span class="seed-option__swatch" :style="{ background: palette.seed }" />
              <span>{{ palette.name }}</span>
              <code>{{ palette.seed }}</code>
            </button>
          </div>
        </div>
        <div class="hct-preview" :style="previewStyle">
          <span>Primary</span>
          <strong>{{ selectedPalette.themeVars.colorPrimary }}</strong>
        </div>
      </section>

      <section class="hct-card" aria-label="HCT tone 色阶">
        <div class="hct-card__header">
          <h2>HCT Tone 色阶</h2>
          <p>Material 3 通过 tone 映射 light / dark theme，而不是简单反色。</p>
        </div>

        <div class="tone-grid">
          <article
            v-for="tone in selectedTones"
            :key="tone.tone"
            class="tone-card"
            :style="{ background: tone.hex, color: tone.textColor }"
          >
            <span class="tone-card__label">Tone {{ tone.tone }}</span>
            <strong>{{ tone.hex }}</strong>
          </article>
        </div>
      </section>

      <section class="hct-card" aria-label="Token 映射">
        <div class="hct-card__header">
          <h2>Token 映射</h2>
          <p>将 HCT tone 映射成当前自研组件可用的 semantic token 和 component token。</p>
        </div>

        <div class="token-list">
          <div v-for="token in tokenRows" :key="token.name" class="token-row">
            <span class="token-swatch" :style="{ background: token.value }" />
            <code>{{ token.name }}</code>
            <strong>{{ token.value }}</strong>
            <span>{{ token.usage }}</span>
          </div>
        </div>
      </section>

      <section class="hct-card" aria-label="按钮效果">
        <div class="hct-card__header">
          <h2>组件效果</h2>
          <p><code>UiButton</code> 只读取 <code>var(--button-*)</code>，不关心 HCT 生成细节。</p>
        </div>
        <div class="hct-actions">
          <UiButton variant="primary">Primary</UiButton>
          <UiButton variant="ghost">Ghost</UiButton>
          <UiButton>Secondary</UiButton>
        </div>
      </section>
    </main>
  </UiConfigProvider>
</template>

<script lang="ts">
import Vue from 'vue';
import UiButton from '@/components/ui/UiButton.vue';
import UiConfigProvider from '@/components/ui/UiConfigProvider.vue';

type Tone = {
  tone: number;
  hex: string;
  textColor: string;
};

type HctInfo = {
  hue: number;
  chroma: number;
  tone: number;
};

type TokenRow = {
  name: string;
  value: string;
  usage: string;
};

type ThemeVars = Record<string, string>;

type Palette = {
  name: string;
  seed: string;
  hct: HctInfo;
  tones: Record<string, string>;
  themeVars: ThemeVars;
};

const toneSteps = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 99, 100];

const palettes: Palette[] = [
  {
    name: 'Ocean Cyan',
    seed: '#00FEFF',
    hct: { hue: 197.04, chroma: 58.8, tone: 90.83 },
    tones: {
      0: '#000000',
      10: '#002020',
      20: '#003737',
      30: '#004f50',
      40: '#006a6a',
      50: '#008585',
      60: '#00a1a2',
      70: '#00bebf',
      80: '#00dcdd',
      90: '#00fbfc',
      95: '#adffff',
      99: '#f1fffe',
      100: '#ffffff',
    },
    themeVars: {
      colorPrimaryBg: '#f1fffe',
      colorPrimaryBgHover: '#adffff',
      colorPrimaryBorder: '#00dcdd',
      colorPrimaryHover: '#00bebf',
      colorPrimary: '#008585',
      colorPrimaryActive: '#006a6a',
      buttonPrimaryBg: 'var(--color-primary)',
      buttonPrimaryBgHover: 'var(--color-primary-hover)',
      buttonPrimaryBgActive: 'var(--color-primary-active)',
      buttonPrimaryText: '#ffffff',
    },
  },
  {
    name: 'Signal Blue',
    seed: '#006EFF',
    hct: { hue: 269.24, chroma: 73.56, tone: 49.94 },
    tones: {
      0: '#000000',
      10: '#001946',
      20: '#002c70',
      30: '#00419d',
      40: '#0057cd',
      50: '#016eff',
      60: '#588cff',
      70: '#86a9ff',
      80: '#b1c5ff',
      90: '#d9e2ff',
      95: '#eef0ff',
      99: '#fefbff',
      100: '#ffffff',
    },
    themeVars: {
      colorPrimaryBg: '#fefbff',
      colorPrimaryBgHover: '#eef0ff',
      colorPrimaryBorder: '#b1c5ff',
      colorPrimaryHover: '#86a9ff',
      colorPrimary: '#016eff',
      colorPrimaryActive: '#0057cd',
      buttonPrimaryBg: 'var(--color-primary)',
      buttonPrimaryBgHover: 'var(--color-primary-hover)',
      buttonPrimaryBgActive: 'var(--color-primary-active)',
      buttonPrimaryText: '#ffffff',
    },
  },
  {
    name: 'Ant Blue',
    seed: '#1677FF',
    hct: { hue: 267.58, chroma: 71.14, tone: 52.49 },
    tones: {
      0: '#000000',
      10: '#001a43',
      20: '#002d6c',
      30: '#004398',
      40: '#0059c7',
      50: '#0070f7',
      60: '#528dff',
      70: '#83aaff',
      80: '#afc6ff',
      90: '#d9e2ff',
      95: '#edf0ff',
      99: '#fefbff',
      100: '#ffffff',
    },
    themeVars: {
      colorPrimaryBg: '#fefbff',
      colorPrimaryBgHover: '#edf0ff',
      colorPrimaryBorder: '#afc6ff',
      colorPrimaryHover: '#83aaff',
      colorPrimary: '#0070f7',
      colorPrimaryActive: '#0059c7',
      buttonPrimaryBg: 'var(--color-primary)',
      buttonPrimaryBgHover: 'var(--color-primary-hover)',
      buttonPrimaryBgActive: 'var(--color-primary-active)',
      buttonPrimaryText: '#ffffff',
    },
  },
  {
    name: 'Growth Green',
    seed: '#16A34A',
    hct: { hue: 150.63, chroma: 64.35, tone: 58.84 },
    tones: {
      0: '#000000',
      10: '#002109',
      20: '#003914',
      30: '#005320',
      40: '#006e2d',
      50: '#008a3b',
      60: '#1ca64d',
      70: '#43c265',
      80: '#62df7d',
      90: '#7ffc97',
      95: '#c5ffc8',
      99: '#f6fff1',
      100: '#ffffff',
    },
    themeVars: {
      colorPrimaryBg: '#f6fff1',
      colorPrimaryBgHover: '#c5ffc8',
      colorPrimaryBorder: '#62df7d',
      colorPrimaryHover: '#43c265',
      colorPrimary: '#008a3b',
      colorPrimaryActive: '#006e2d',
      buttonPrimaryBg: 'var(--color-primary)',
      buttonPrimaryBgHover: 'var(--color-primary-hover)',
      buttonPrimaryBgActive: 'var(--color-primary-active)',
      buttonPrimaryText: '#ffffff',
    },
  },
  {
    name: 'Royal Purple',
    seed: '#7C3AED',
    hct: { hue: 301.88, chroma: 78.88, tone: 43.4 },
    tones: {
      0: '#000000',
      10: '#25005a',
      20: '#3f008e',
      30: '#5a00c6',
      40: '#732ee4',
      50: '#8d4fff',
      60: '#a476ff',
      70: '#bb9aff',
      80: '#d2bbff',
      90: '#eaddff',
      95: '#f7edff',
      99: '#fffbff',
      100: '#ffffff',
    },
    themeVars: {
      colorPrimaryBg: '#fffbff',
      colorPrimaryBgHover: '#f7edff',
      colorPrimaryBorder: '#d2bbff',
      colorPrimaryHover: '#bb9aff',
      colorPrimary: '#8d4fff',
      colorPrimaryActive: '#732ee4',
      buttonPrimaryBg: 'var(--color-primary)',
      buttonPrimaryBgHover: 'var(--color-primary-hover)',
      buttonPrimaryBgActive: 'var(--color-primary-active)',
      buttonPrimaryText: '#ffffff',
    },
  },
  {
    name: 'Alert Red',
    seed: '#FF3246',
    hct: { hue: 19.75, chroma: 96.08, tone: 56.07 },
    tones: {
      0: '#000000',
      10: '#410007',
      20: '#680011',
      30: '#92001c',
      40: '#bf0027',
      50: '#e81e39',
      60: '#ff535a',
      70: '#ff8887',
      80: '#ffb3b1',
      90: '#ffdad8',
      95: '#ffedeb',
      99: '#fffbff',
      100: '#ffffff',
    },
    themeVars: {
      colorPrimaryBg: '#fffbff',
      colorPrimaryBgHover: '#ffedeb',
      colorPrimaryBorder: '#ffb3b1',
      colorPrimaryHover: '#ff8887',
      colorPrimary: '#e81e39',
      colorPrimaryActive: '#bf0027',
      buttonPrimaryBg: 'var(--color-primary)',
      buttonPrimaryBgHover: 'var(--color-primary-hover)',
      buttonPrimaryBgActive: 'var(--color-primary-active)',
      buttonPrimaryText: '#ffffff',
    },
  },
  {
    name: 'Ink Neutral',
    seed: '#12161B',
    hct: { hue: 251.79, chroma: 6.98, tone: 7.06 },
    tones: {
      0: '#000000',
      10: '#181c21',
      20: '#2d3136',
      30: '#43474d',
      40: '#5b5f65',
      50: '#74777e',
      60: '#8d9197',
      70: '#a8abb2',
      80: '#c3c6cd',
      90: '#e0e2ea',
      95: '#eef1f8',
      99: '#fdfcff',
      100: '#ffffff',
    },
    themeVars: {
      colorPrimaryBg: '#fdfcff',
      colorPrimaryBgHover: '#eef1f8',
      colorPrimaryBorder: '#c3c6cd',
      colorPrimaryHover: '#a8abb2',
      colorPrimary: '#74777e',
      colorPrimaryActive: '#5b5f65',
      buttonPrimaryBg: 'var(--color-primary)',
      buttonPrimaryBgHover: 'var(--color-primary-hover)',
      buttonPrimaryBgActive: 'var(--color-primary-active)',
      buttonPrimaryText: '#ffffff',
    },
  },
  {
    name: 'Spark Orange',
    seed: '#FF611E',
    hct: { hue: 37.94, chroma: 79.57, tone: 61.57 },
    tones: {
      0: '#000000',
      10: '#380d00',
      20: '#5c1a00',
      30: '#822800',
      40: '#aa3700',
      50: '#d44700',
      60: '#f95d1a',
      70: '#ff8c61',
      80: '#ffb59b',
      90: '#ffdbcf',
      95: '#ffede8',
      99: '#fffbff',
      100: '#ffffff',
    },
    themeVars: {
      colorPrimaryBg: '#fffbff',
      colorPrimaryBgHover: '#ffede8',
      colorPrimaryBorder: '#ffb59b',
      colorPrimaryHover: '#ff8c61',
      colorPrimary: '#d44700',
      colorPrimaryActive: '#aa3700',
      buttonPrimaryBg: 'var(--color-primary)',
      buttonPrimaryBgHover: 'var(--color-primary-hover)',
      buttonPrimaryBgActive: 'var(--color-primary-active)',
      buttonPrimaryText: '#ffffff',
    },
  },
];

export default Vue.extend({
  name: 'HctPaletteDemo',
  components: {
    UiButton,
    UiConfigProvider,
  },
  data() {
    return {
      selectedSeed: '#006EFF',
      palettes,
    };
  },
  computed: {
    selectedPalette(): Palette {
      return this.palettes.find(palette => palette.seed === this.selectedSeed) || this.palettes[0];
    },
    selectedTones(): Tone[] {
      return toneSteps.map(tone => {
        const hex = this.selectedPalette.tones[String(tone)];

        return {
          tone,
          hex,
          textColor: tone < 60 ? '#ffffff' : this.selectedPalette.tones['10'],
        };
      });
    },
    previewStyle(): Record<string, string> {
      return {
        background: this.selectedPalette.themeVars.colorPrimary,
        boxShadow: `0 20px 48px ${this.selectedPalette.themeVars.colorPrimary}40`,
      };
    },
    tokenRows(): TokenRow[] {
      return [
        { name: 'colorPrimaryBg', value: this.selectedPalette.themeVars.colorPrimaryBg, usage: '弱背景 / 容器强调' },
        { name: 'colorPrimaryBgHover', value: this.selectedPalette.themeVars.colorPrimaryBgHover, usage: '浅色 hover 背景' },
        { name: 'colorPrimaryBorder', value: this.selectedPalette.themeVars.colorPrimaryBorder, usage: '边框 / focus 辅助' },
        { name: 'colorPrimaryHover', value: this.selectedPalette.themeVars.colorPrimaryHover, usage: '主按钮 hover' },
        { name: 'colorPrimary', value: this.selectedPalette.themeVars.colorPrimary, usage: '主按钮 default' },
        { name: 'colorPrimaryActive', value: this.selectedPalette.themeVars.colorPrimaryActive, usage: '主按钮 active' },
      ];
    },
  },
});
</script>

<style lang="scss">
.hct-palette-shell {
  min-height: calc(100vh - 81px);
}

.hct-palette-demo {
  display: grid;
  gap: 24px;
  max-width: 1100px;
  margin: 0 auto;
  padding: 48px 20px;
  text-align: left;
}

.hct-hero,
.hct-card {
  border: 1px solid var(--color-border);
  border-radius: 18px;
  background: var(--color-surface);
}

.hct-hero {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 220px;
  gap: 24px;
  align-items: stretch;
  padding: 28px;
}

.hct-kicker {
  margin: 0 0 10px;
  color: var(--color-primary);
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.hct-title {
  margin: 0;
  color: var(--color-text);
  font-size: 34px;
  line-height: 1.15;
}

.hct-text {
  max-width: 700px;
  margin: 16px 0 0;
  color: var(--color-text-muted);
  line-height: 1.7;
}

.seed-selector {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 22px;
}

.seed-option {
  display: inline-grid;
  grid-template-columns: 18px auto auto;
  gap: 8px;
  align-items: center;
  padding: 8px 10px;
  border: 1px solid var(--color-border);
  border-radius: 999px;
  background: var(--color-surface);
  color: var(--color-text);
  font: inherit;
  font-size: 13px;
  cursor: pointer;
}

.seed-option--active {
  border-color: var(--color-primary);
  background: var(--color-primary-bg);
  color: var(--color-primary-active);
}

.seed-option__swatch {
  width: 18px;
  height: 18px;
  border: 1px solid rgba(0, 0, 0, 0.12);
  border-radius: 999px;
}

.seed-option code {
  color: inherit;
  font-size: 12px;
  opacity: 0.72;
}

.hct-preview {
  display: grid;
  align-content: end;
  min-height: 180px;
  padding: 18px;
  border-radius: 14px;
  color: #ffffff;
}

.hct-preview span {
  font-size: 13px;
  opacity: 0.85;
}

.hct-preview strong {
  margin-top: 4px;
  font-size: 24px;
}

.hct-card {
  display: grid;
  gap: 20px;
  padding: 24px;
}

.hct-card__header h2 {
  margin: 0;
  font-size: 22px;
}

.hct-card__header p {
  margin: 8px 0 0;
  color: var(--color-text-muted);
}

.tone-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
  gap: 12px;
}

.tone-card {
  display: grid;
  align-content: space-between;
  min-height: 120px;
  padding: 14px;
  border: 1px solid rgba(0, 32, 32, 0.12);
  border-radius: 14px;
}

.tone-card__label {
  font-size: 13px;
  font-weight: 700;
}

.tone-card strong {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', monospace;
  font-size: 16px;
}

.token-list {
  display: grid;
  overflow: hidden;
  border: 1px solid var(--color-border);
  border-radius: 14px;
}

.token-row {
  display: grid;
  grid-template-columns: 36px minmax(180px, 1fr) 120px minmax(160px, 1fr);
  gap: 14px;
  align-items: center;
  padding: 12px 14px;
  border-bottom: 1px solid var(--color-border);
}

.token-row:last-child {
  border-bottom: 0;
}

.token-swatch {
  width: 28px;
  height: 28px;
  border: 1px solid var(--color-border);
  border-radius: 999px;
}

.token-row code {
  color: var(--color-text);
}

.token-row strong {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', monospace;
}

.token-row span:last-child {
  color: var(--color-text-muted);
}

.hct-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

@media (max-width: 760px) {
  .hct-palette-demo {
    padding: 32px 16px;
  }

  .hct-hero {
    grid-template-columns: 1fr;
    padding: 22px;
  }

  .hct-title {
    font-size: 28px;
  }

  .token-row {
    grid-template-columns: 32px 1fr;
  }

  .token-row strong,
  .token-row span:last-child {
    grid-column: 2;
  }

  .seed-option {
    grid-template-columns: 18px 1fr;
  }

  .seed-option code {
    grid-column: 2;
  }
}
</style>
