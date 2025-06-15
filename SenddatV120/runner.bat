@echo off
setlocal enabledelayedexpansion

for /L %%i in (67,1,240) do (
    senddat -b192 "Output%%i.txt" com2

    rem Check if the loop counter is divisible by 5
    set /a mod=%%i %% 5
    if !mod! == 0 (
        echo Pausing for 5 seconds...
        timeout /t 5 /nobreak >nul
    )
)

endlocal
