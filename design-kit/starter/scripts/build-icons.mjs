// Lucide → SVG 스프라이트(icons/icons.svg). 실행: npm run icons
// 아이콘 추가: 아래 ICONS 에 이름 추가 (https://lucide.dev/icons 에서 검색)
// 페이지에는 스프라이트를 <body> 바로 아래 인라인으로 넣는다 → <svg class="ic"><use href="#i-이름"/></svg>
import { readFileSync, writeFileSync, copyFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const src = join(root, 'node_modules/lucide-static/icons');

const ICONS = [
  // 내비게이션
  'house', 'search', 'menu', 'x', 'chevron-left', 'chevron-right', 'chevron-down', 'arrow-left', 'arrow-up-right', 'external-link',
  // 사용자·상태
  'user', 'settings', 'bell', 'log-in', 'log-out',
  // 행동
  'plus', 'minus', 'check', 'pencil', 'trash-2', 'copy', 'link', 'download', 'upload', 'share-2', 'filter', 'sliders-horizontal', 'refresh-cw',
  // 피드백
  'info', 'circle-alert', 'circle-check', 'triangle-alert', 'circle', 'loader',
  // 콘텐츠·커머스
  'heart', 'star', 'bookmark', 'shopping-cart', 'tag', 'image', 'calendar', 'clock', 'map-pin',
  // 게임성
  'trophy', 'award', 'flame', 'sparkles', 'gift', 'zap', 'crown', 'book-open',
  // 테마
  'sun', 'moon',
];

const symbols = ICONS.map((name) => {
  const svg = readFileSync(join(src, name + '.svg'), 'utf8');
  const inner = svg.replace(/<!--[\s\S]*?-->/g, '').replace(/^[\s\S]*?<svg[^>]*>/, '').replace(/<\/svg>\s*$/, '')
    .split('\n').map((l) => l.trim()).filter(Boolean).join('');
  return `<symbol id="i-${name}" viewBox="0 0 24 24">${inner}</symbol>`;
}).join('\n');

const sprite = `<svg xmlns="http://www.w3.org/2000/svg" width="0" height="0" style="position:absolute" aria-hidden="true">\n<!-- Lucide (ISC) https://lucide.dev -->\n${symbols}\n</svg>\n`;
writeFileSync(join(root, 'icons/icons.svg'), sprite);
// 빌드 도구 없이 쓰는 페이지용: import { SPRITE } from './icons/icons.inline.js'
writeFileSync(join(root, 'icons/icons.inline.js'), `// 자동 생성(npm run icons). 직접 수정 금지.\nexport const SPRITE = ${JSON.stringify(sprite)};\n`);
copyFileSync(join(root, 'node_modules/lucide-static/LICENSE'), join(root, 'icons/LICENSE-lucide.txt'));
console.log(`icons: ${ICONS.length} → icons/icons.svg, icons/icons.inline.js`);
