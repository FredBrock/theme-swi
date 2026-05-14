<template>
  <main class="mcu-page">
    <section class="mcu-panel">
      <h1>Material Color Utilities Validator</h1>
      <p>Validate seed color -> HCT -> scheme, and run quantize + score on sample pixels.</p>

      <div class="mcu-controls">
        <label>
          Seed Hex
          <input v-model="seedHex" type="text" placeholder="#4285F4" />
        </label>
        <label>
          Seed ARGB
          <input v-model="seedArgbText" type="text" placeholder="0xff4285f4" />
        </label>
        <button type="button" @click="applyArgbInput">Use ARGB Input</button>
        <button type="button" @click="generateTheme">Generate</button>
      </div>

      <p v-if="error" class="mcu-error">{{ error }}</p>
    </section>

    <section class="mcu-grid">
      <article class="mcu-card">
        <h2>Seed + HCT</h2>
        <div class="swatch" :style="{ background: result.seedHex }" />
        <p><strong>seedHex:</strong> {{ result.seedHex }}</p>
        <p><strong>seedArgb:</strong> {{ result.seedArgb }}</p>
        <p><strong>hue:</strong> {{ result.hctHue }}</p>
        <p><strong>chroma:</strong> {{ result.hctChroma }}</p>
        <p><strong>tone:</strong> {{ result.hctTone }}</p>
      </article>

      <article class="mcu-card">
        <h2>Light Scheme</h2>
        <div class="chips">
          <div v-for="item in lightRoleColors" :key="item.name" class="chip-row">
            <span class="chip" :style="{ background: item.hex }" />
            <code>{{ item.name }}</code>
            <strong>{{ item.hex }}</strong>
          </div>
        </div>
      </article>

      <article class="mcu-card">
        <h2>Quantize + Score</h2>
        <p>Sample pixels from current seed hue.</p>
        <div class="chips">
          <div v-for="hex in result.scoredHexes" :key="hex" class="chip-row">
            <span class="chip" :style="{ background: hex }" />
            <strong>{{ hex }}</strong>
          </div>
        </div>
      </article>
    </section>
  </main>
</template>

<script lang="ts">
import Vue from 'vue';
import {
  Hct,
  QuantizerCelebi,
  Score,
  argbFromHex,
  hexFromArgb,
  themeFromSourceColor,
} from '@material/material-color-utilities';

type RoleColor = { name: string; hex: string };

type DemoResult = {
  seedHex: string;
  seedArgb: string;
  hctHue: string;
  hctChroma: string;
  hctTone: string;
  lightRoles: RoleColor[];
  scoredHexes: string[];
};

function toArgbText(value: number): string {
  return `0x${(value >>> 0).toString(16).padStart(8, '0')}`;
}

export default Vue.extend({
  name: 'MaterialColorUtilitiesDemo',
  data() {
    return {
      seedHex: '#4285F4',
      seedArgbText: '0xff4285f4',
      error: '',
      result: {
        seedHex: '#4285f4',
        seedArgb: '0xff4285f4',
        hctHue: '0.00',
        hctChroma: '0.00',
        hctTone: '0.00',
        lightRoles: [],
        scoredHexes: [],
      } as DemoResult,
    };
  },
  computed: {
    lightRoleColors(): RoleColor[] {
      return this.result.lightRoles;
    },
  },
  mounted() {
    this.generateTheme();
  },
  methods: {
    applyArgbInput() {
      const parsed = Number(this.seedArgbText);

      if (!Number.isFinite(parsed) || parsed < 0) {
        this.error = 'Invalid ARGB. Example: 0xff4285f4';
        return;
      }

      this.seedHex = hexFromArgb(parsed >>> 0);
      this.error = '';
    },
    generateTheme() {
      try {
        const seedArgb = argbFromHex(this.seedHex);
        const hct = Hct.fromInt(seedArgb);
        const theme = themeFromSourceColor(seedArgb);
        const light = theme.schemes.light;

        const lightRoles: RoleColor[] = [
          { name: 'primary', hex: hexFromArgb(light.primary) },
          { name: 'onPrimary', hex: hexFromArgb(light.onPrimary) },
          { name: 'primaryContainer', hex: hexFromArgb(light.primaryContainer) },
          { name: 'onPrimaryContainer', hex: hexFromArgb(light.onPrimaryContainer) },
          { name: 'secondary', hex: hexFromArgb(light.secondary) },
          { name: 'surface', hex: hexFromArgb(light.surface) },
        ];

        const samplePixels = this.buildSamplePixels(seedArgb);
        const quantized = QuantizerCelebi.quantize(samplePixels, 128);
        const scored = Score.score(quantized, { desired: 6 });

        this.result = {
          seedHex: hexFromArgb(seedArgb),
          seedArgb: toArgbText(seedArgb),
          hctHue: hct.hue.toFixed(2),
          hctChroma: hct.chroma.toFixed(2),
          hctTone: hct.tone.toFixed(2),
          lightRoles,
          scoredHexes: scored.map((argb) => hexFromArgb(argb)),
        };
        this.error = '';
      } catch (err) {
        this.error = `Generate failed: ${String(err)}`;
      }
    },
    buildSamplePixels(seedArgb: number): number[] {
      const hctSeed = Hct.fromInt(seedArgb);
      const tones = [95, 85, 75, 65, 55, 45, 35, 25];
      const pixels: number[] = [];

      tones.forEach((tone) => {
        for (let i = 0; i < 12; i += 1) {
          const hue = hctSeed.hue + i * 2.4;
          const color = Hct.from(hue, Math.max(16, hctSeed.chroma * 0.8), tone).toInt();
          pixels.push(color);
        }
      });

      return pixels;
    },
  },
});
</script>

<style scoped lang="scss">
.mcu-page {
  max-width: 1080px;
  margin: 0 auto;
  padding: 24px;
  text-align: left;
}

.mcu-panel {
  background: #f5f7fb;
  border: 1px solid #d9e0ee;
  border-radius: 12px;
  padding: 20px;
}

.mcu-controls {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 12px;
  align-items: end;
  margin-top: 12px;
}

label {
  display: grid;
  gap: 6px;
  font-weight: 600;
}

input,
button {
  height: 40px;
  border-radius: 8px;
  border: 1px solid #b7c5e0;
  padding: 0 10px;
  font-size: 14px;
}

button {
  cursor: pointer;
  background: #1f3d7a;
  color: #fff;
}

.mcu-error {
  color: #b00020;
  margin-top: 10px;
}

.mcu-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 12px;
  margin-top: 14px;
}

.mcu-card {
  border: 1px solid #d9e0ee;
  border-radius: 12px;
  padding: 16px;
  background: #fff;
}

.swatch {
  height: 56px;
  border-radius: 10px;
  border: 1px solid #d3dbe9;
  margin: 10px 0;
}

.chips {
  display: grid;
  gap: 8px;
}

.chip-row {
  display: grid;
  grid-template-columns: 22px 1fr auto;
  align-items: center;
  gap: 8px;
}

.chip {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  border: 1px solid #d3dbe9;
}
</style>
