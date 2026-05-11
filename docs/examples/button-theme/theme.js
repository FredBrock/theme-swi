const THEME_KEY = 'button-demo-theme';
const DENSITY_KEY = 'button-demo-density';

const root = document.documentElement;
const themeButton = document.querySelector('[data-theme-toggle]');
const densityButton = document.querySelector('[data-density-toggle]');

function getInitialTheme() {
  const savedTheme = localStorage.getItem(THEME_KEY);

  if (savedTheme) {
    return savedTheme;
  }

  return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
}

function setTheme(theme) {
  root.dataset.theme = theme;
  localStorage.setItem(THEME_KEY, theme);

  if (themeButton) {
    themeButton.textContent = theme === 'dark' ? '切换到亮色' : '切换到暗色';
  }
}

function setDensity(density) {
  root.dataset.density = density;
  localStorage.setItem(DENSITY_KEY, density);

  if (densityButton) {
    densityButton.textContent = density === 'compact' ? '切换到舒适密度' : '切换到紧凑密度';
  }
}

setTheme(getInitialTheme());
setDensity(localStorage.getItem(DENSITY_KEY) || 'comfortable');

themeButton?.addEventListener('click', () => {
  setTheme(root.dataset.theme === 'dark' ? 'light' : 'dark');
});

densityButton?.addEventListener('click', () => {
  setDensity(root.dataset.density === 'compact' ? 'comfortable' : 'compact');
});
