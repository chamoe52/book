"""책 사진 27장을 웹용으로 최적화한다.
원본(KakaoTalk_*.jpg)은 건드리지 않고 site/img, site/img/thumb 에 압축본 생성.
- 풀사이즈(라이트박스용): 긴 변 1400px, JPEG q82
- 썸네일(카드용): 긴 변 760px, JPEG q80
- EXIF 회전 정보 반영
"""
import os
import glob
from PIL import Image, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))      # 이 스크립트가 있는 폴더(docs)
SRC_DIR = os.path.abspath(os.path.join(HERE, ".."))    # 원본 카톡 사진이 있는 상위 폴더
OUT_DIR = os.path.join(HERE, "img")
THUMB_DIR = os.path.join(OUT_DIR, "thumb")
os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(THUMB_DIR, exist_ok=True)

srcs = sorted(glob.glob(os.path.join(SRC_DIR, "KakaoTalk_*.jpg")))
print(f"source images: {len(srcs)}")

total_before = 0
total_after = 0
for idx, path in enumerate(srcs):
    total_before += os.path.getsize(path)
    name = f"p{idx:02d}.jpg"
    with Image.open(path) as im:
        im = ImageOps.exif_transpose(im)  # 휴대폰 회전 반영
        if im.mode != "RGB":
            im = im.convert("RGB")

        full = im.copy()
        full.thumbnail((1400, 1400), Image.LANCZOS)
        full_path = os.path.join(OUT_DIR, name)
        full.save(full_path, "JPEG", quality=82, optimize=True, progressive=True)

        thumb = im.copy()
        thumb.thumbnail((760, 760), Image.LANCZOS)
        thumb_path = os.path.join(THUMB_DIR, name)
        thumb.save(thumb_path, "JPEG", quality=80, optimize=True, progressive=True)

    a = os.path.getsize(full_path) + os.path.getsize(thumb_path)
    total_after += a
    print(f"  {os.path.basename(path)} -> {name}  ({os.path.getsize(full_path)//1024}KB + {os.path.getsize(thumb_path)//1024}KB)")

print(f"\nTOTAL before: {total_before/1024/1024:.1f} MB")
print(f"TOTAL after : {total_after/1024/1024:.1f} MB  (full+thumb)")
