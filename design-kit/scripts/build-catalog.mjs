// resources/catalog.json → resources/catalog.md. 실행: node scripts/build-catalog.mjs
// 목록 수정은 JSON 에서만 한다. MD 는 매번 다시 만든다.
import { readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const dir = join(dirname(fileURLToPath(import.meta.url)), '../resources');
const { updated, note, categories, items } = JSON.parse(readFileSync(join(dir, 'catalog.json'), 'utf8'));

const cell = (s) => String(s).replace(/\|/g, '\\|');
const link = (i) => `[${cell(i.name)}](https://github.com/${i.repo})`;
const PICK = { 3: '★★★', 2: '★★', 1: '★' };
const STATUS = { active: '', reference: ' · 참고용' };

const out = [
  '# 웹프론트 디자인·UI/UX 자료 100선',
  '',
  `> 자동 생성 파일 — \`catalog.json\` 을 고치고 \`node scripts/build-catalog.mjs\` 실행. 기준일 ${updated}.`,
  `> ${note}`,
  '',
  '## 기본 탑재 권장 (★★★)',
  '',
  '| # | 자료 | 분류 | 라이선스 | 쓰임 |',
  '|---|---|---|---|---|',
  ...items.filter((i) => i.pick === 3).map((i) =>
    `| ${i.id} | ${link(i)} | ${categories.find((c) => c.id === i.cat).name} | ${cell(i.license)} | ${cell(i.use)} |`),
  '',
  '## 목차',
  '',
  ...categories.map((c) => `- **${c.id}. ${c.name}** (${items.filter((i) => i.cat === c.id).length}) — ${c.why}`),
  '',
];

for (const c of categories) {
  out.push(`## ${c.id}. ${c.name}`, '', `_${c.why}_`, '',
    '| # | 자료 | 라이선스 | ★ GitHub | 추천 | 쓰임 |', '|---|---|---|---|---|---|');
  for (const i of items.filter((x) => x.cat === c.id))
    out.push(`| ${i.id} | ${link(i)} | ${cell(i.license)} | ${i.stars} | ${PICK[i.pick]}${STATUS[i.status] ?? ''} | ${cell(i.use)} |`);
  out.push('');
}
out.push('추천: ★★★ 기본 탑재 권장 · ★★ 상황별 1순위 · ★ 참고·학습용. "참고용"은 유지보수가 멈췄지만 구현 방식을 배울 가치가 있는 저장소.', '');

writeFileSync(join(dir, 'catalog.md'), out.join('\n'));
console.log(`catalog.md: ${items.length} items, ${categories.length} categories`);
