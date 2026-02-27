rem for %%a in (*.png *.jpg) do ffmpeg -hwaccel nvdec -i "%%a" -c:v libwebp -q:v 60 "new/%%~na.webp"

for %%a in (*.png *.jpg) do (
    ffmpeg  -hide_banner -i "%%a" -c:v libwebp -q:v 60 "%%~na.webp"
    del "%%a"
)
