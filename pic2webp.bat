for %%a in (*.png *.jpg) do ffmpeg -hwaccel nvdec -i "%%a" -c:v libwebp -q:v 60 "new/%%~na.webp"