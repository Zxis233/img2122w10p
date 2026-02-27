#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import sys

def main():
    # 可选：传 --recursive 扫子文件夹；不传只扫当前文件夹
    recursive = "--recursive" in sys.argv

    try:
        from PIL import Image  # pillow
        import pillow_avif  # pillow-avif-plugin（只要import即可注册AVIF）
    except Exception as e:
        print("缺少依赖。请先运行：pip install pillow pillow-avif-plugin")
        print(f"详细错误：{e}")
        sys.exit(1)

    exts = {".avif", ".webp"}
    base = Path.cwd()

    files = base.rglob("*") if recursive else base.glob("*")
    bad = []

    for p in files:
        if not p.is_file():
            continue
        if p.suffix.lower() not in exts:
            continue

        try:
            with Image.open(p) as im:
                w, h = im.size
        except Exception as e:
            print(f"[无法读取] {p.name}  ({e})")
            continue

        if (w % 16) != 0 and (h % 16) != 0:
            bad.append((p, w, h))

    if not bad:
        print("未发现宽或高不能被16整除的 avif/webp 图片。")
        return

    print(f"发现 {len(bad)} 张不符合(宽%16==0 且 高%16==0) 的图片：")
    for p, w, h in sorted(bad, key=lambda x: str(x[0]).lower()):
        print(f"{p.name}\t{w}x{h}\t(w%16={w%16}, h%16={h%16})")

if __name__ == "__main__":
    main()