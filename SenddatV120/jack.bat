@echo off
set "parent_dir=C:\Users\jrfcr\Downloads\pdf2png"

rem Move files from subdirectories to parent directory
for /r "%parent_dir%" %%f in (*) do move "%%f" "%parent_dir%"

rem Remove empty subdirectories
for /d /r "%parent_dir%" %%d in (*) do rd "%%d"