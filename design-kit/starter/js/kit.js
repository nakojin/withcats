// design-kit 동작. 의존성 없음, ES 모듈.  import { sheet, toast, tabs, theme, icon } from './js/kit.js'
// 원칙: 마크업이 주인이고 JS 는 접근성(키보드·포커스·aria)과 상태만 담당한다.

/** 아이콘 HTML. 스프라이트(<symbol id="i-이름">)가 페이지에 있어야 한다. */
export const icon = (name, cls = '') => `<svg class="ic ${cls}" aria-hidden="true"><use href="#i-${name}"/></svg>`;

/* ── 바텀시트 / 다이얼로그 ──────────────────────────────────
   <dialog class="kit-sheet" id="x"> … </dialog>
   <button data-sheet-open="x">열기</button>  /  시트 안 [data-sheet-close]
   네이티브 <dialog> 가 포커스 가두기·Esc·inert 를 처리한다. 배경 클릭으로 닫기만 추가. */
export const sheet = {
  open(id) { const d = document.getElementById(id); if (d && !d.open) { d.showModal(); d.dispatchEvent(new Event('kit:open')); } },
  close(id) { const d = typeof id === 'string' ? document.getElementById(id) : id; if (d?.open) d.close(); },
  init(root = document) {
    root.addEventListener('click', (e) => {
      const o = e.target.closest('[data-sheet-open]'); if (o) { e.preventDefault(); sheet.open(o.dataset.sheetOpen); return; }
      const c = e.target.closest('[data-sheet-close]'); if (c) { sheet.close(c.closest('dialog')); return; }
      // 배경(::backdrop) 클릭: 이벤트 타깃이 dialog 자신이면 바깥을 누른 것
      if (e.target instanceof HTMLDialogElement && e.target.classList.contains('kit-sheet')) sheet.close(e.target);
    });
  },
};

/* ── 토스트 ────────────────────────────────────────────────
   toast('저장했어요', { icon: 'check', duration: 2400 })
   스크린리더에는 aria-live 로 읽힌다. 최대 3개까지 쌓이고 오래된 것부터 사라진다. */
let toastHost;
export function toast(message, { icon: ic = '', duration = 2400 } = {}) {
  if (!toastHost) {
    toastHost = document.createElement('div');
    toastHost.className = 'kit-toasts'; toastHost.setAttribute('role', 'status'); toastHost.setAttribute('aria-live', 'polite');
    document.body.appendChild(toastHost);
  }
  const el = document.createElement('div');
  el.className = 'kit-toast';
  el.innerHTML = (ic ? icon(ic) : '') + `<span></span>`;
  el.querySelector('span').textContent = message;          // 메시지는 항상 텍스트로 (XSS 방지)
  toastHost.appendChild(el);
  while (toastHost.children.length > 3) toastHost.firstElementChild.remove();
  const leave = () => { el.classList.add('is-leaving'); el.addEventListener('animationend', () => el.remove(), { once: true }); setTimeout(() => el.remove(), 400); };
  setTimeout(leave, duration);
  el.addEventListener('click', leave);
  return el;
}

/* ── 탭 (WAI-ARIA Tabs 패턴) ───────────────────────────────
   <div class="kit-tabs" role="tablist"><button role="tab" aria-controls="p1">…</button></div>
   <div role="tabpanel" id="p1">…</div>
   화살표 ←/→, Home/End 로 이동. 선택 시 'kit:tab' 이벤트. */
export function tabs(list) {
  const items = [...list.querySelectorAll('[role="tab"]')];
  const select = (t, focus = true) => {
    items.forEach((x) => {
      const on = x === t;
      x.setAttribute('aria-selected', on); x.tabIndex = on ? 0 : -1;
      const p = document.getElementById(x.getAttribute('aria-controls')); if (p) p.hidden = !on;
    });
    if (focus) t.focus();
    list.dispatchEvent(new CustomEvent('kit:tab', { detail: { tab: t } }));
  };
  items.forEach((t) => t.addEventListener('click', () => select(t)));
  list.addEventListener('keydown', (e) => {
    const i = items.indexOf(document.activeElement); if (i < 0) return;
    const next = { ArrowRight: i + 1, ArrowLeft: i - 1, Home: 0, End: items.length - 1 }[e.key];
    if (next === undefined) return;
    e.preventDefault(); select(items[(next + items.length) % items.length]);
  });
  select(items.find((t) => t.getAttribute('aria-selected') === 'true') || items[0], false);
}

/* ── 토글 칩 (aria-pressed) ── */
export function toggles(root = document) {
  root.addEventListener('click', (e) => {
    const c = e.target.closest('[aria-pressed]'); if (!c) return;
    const group = c.closest('[data-single]');      // 단일 선택 그룹
    if (group) group.querySelectorAll('[aria-pressed]').forEach((x) => x.setAttribute('aria-pressed', x === c));
    else c.setAttribute('aria-pressed', c.getAttribute('aria-pressed') !== 'true');
  });
}

/* ── 테마 (라이트/다크/시스템) ── */
export const theme = {
  get() { try { return localStorage.getItem('kit-theme') || 'system'; } catch { return 'system'; } },
  set(v) {
    if (v === 'system') document.documentElement.removeAttribute('data-theme'); else document.documentElement.dataset.theme = v;
    try { localStorage.setItem('kit-theme', v); } catch {}
  },
  init() { const v = theme.get(); if (v !== 'system') document.documentElement.dataset.theme = v; },
};

/** 전부 켜기 */
export function initKit() {
  theme.init(); sheet.init(); toggles();
  document.querySelectorAll('[role="tablist"]').forEach(tabs);
}
