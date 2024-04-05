@echo off

REM Activating virtual env
call "D:\CodePlayground\automation\env\Scripts\activate.bat"

REM running python script
python "D:\CodePlayground\automation\automation.py"

REM deactivate env
deactivate

@REM after that schedule a cron job 