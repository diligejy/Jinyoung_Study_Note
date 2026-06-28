# Jinyoung Study Note — Claude 운영 원칙

글로벌 CLAUDE.md(6대 근본원칙) 상속. 이 파일은 Study Note 작업에 한정된 규칙만 추가한다.

## MCP 의무 사용 게이트 (하네스 원칙)

노트북 생성·수정·검증·배포 작업 시작 전 반드시 확인:

```
mcp__jupyter-book-writer__fetch_notebook
mcp__jupyter-book-writer__add_cell
mcp__jupyter-book-writer__add_cells_batch
mcp__jupyter-book-writer__validate_notebook
mcp__jupyter-book-writer__update_toc
mcp__jupyter-book-writer__deploy_and_wait
```

위 도구가 세션에 없으면 **즉시 작업 중단** 후 보고:
> "jupyter-book-writer MCP 도구가 이 세션에 없습니다. 새 세션을 열어주세요."

Python import(`from server import ...`)로 우회하는 것은 **하네스 원칙 위반**이며 금지.

## 노트북 작업 표준 흐름

1. `fetch_notebook(url)` — Colab/GitHub URL에서 원본 가져오기
2. `add_cells_batch(path, cells)` — 한국어 Study Note 셀 일괄 추가
3. `validate_notebook(path)` — 배포 전 렌더링 이슈 검증
4. `update_toc(...)` — `_toc.yml` 챕터 등록
5. 노트북 실행 후 Ctrl+S 저장 → 커밋·푸시

## 폰트·차트 표준 (2_1_2 작업에서 학습)

- 셋업 셀 순서: `%matplotlib inline` → `import numpy` → `import matplotlib` → `import matplotlib.pyplot` → `rcParams`
- `rcParams["font.family"] = "Malgun Gothic"` 필수
- 각 플롯 셀 끝 `plt.show()` 필수
- `plt.title()` 등 LaTeX 포함 문자열은 `r''` raw string

## MCP 서버 위치

`C:/Users/sjy04/Videos/jupyter-book-writer-mcp/server.py`

등록 확인: `claude mcp list` → `jupyter-book-writer: ✔ Connected`
