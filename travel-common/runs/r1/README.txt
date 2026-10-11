Round 1 (v2.0 1회차) 작업 폴더. 81곳 / 27묶음(batchNN.json).
흐름: collect(Sonnet, prompts/collect.md) -> python3 -I r1/pipe.py collected <agent> NN  (scratchpad 에서 실행)
      -> verify(Opus, prompts/verify.md, 입력 r1/verify_inNN.json) -> python3 -I r1/pipe.py verified <agent> NN
      -> cd wt4 && python3 -I travel-common/tools/merge_run.py . r1-bNN 2026-10-11 ../r1/collectedNN.json ../r1/verifiedNN.json [../r1/fixNN.json]
LEDGER.tsv 에 에이전트 id 와 상태를 기록한다. 동시 실행은 수집+검증 합쳐 10개 안팎.
