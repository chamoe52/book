# 중고 교재 장터

대학 전공서적과 자격증 교재를 정리해서 판매하는 한 페이지 사이트입니다.

**🔗 판매 페이지:** https://cyun0407-blip.github.io/book/

- 직거래(학교/근처) 및 택배 가능
- 문의: 카카오톡 오픈채팅

## 폴더 구조
- `docs/index.html` — 판매 페이지 (이 파일 하나로 동작)
- `docs/img/` — 웹용으로 최적화한 책 사진 (풀사이즈 + 썸네일)
- `docs/optimize_images.py` — 원본 사진을 웹용으로 압축하는 스크립트

## 가격·책 정보 고치기
`docs/index.html` 안의 `const CATS = [ ... ]` 부분에서 제목·가격·상태를 바꾸면 됩니다.
수정 후 저장 → `git add . && git commit -m "수정" && git push` 하면 몇 분 안에 사이트에 반영됩니다.

## 사진 다시 만들기 (선택)
원본 사진(`KakaoTalk_*.jpg`)을 바꾼 뒤:

```bash
python docs/optimize_images.py
```
