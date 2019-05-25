echo Called000000000000000
python ./auto_connect_network.py
@echo off
set INTERVAL= 3600
timeout %INTERVAL%
:Again
echo Called000000000000000
python ./auto_connect_network.py
timeout %INTERVAL%
goto Again