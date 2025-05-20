@echo off
REM stage everything
git add .

REM commit with the *entire* argument string as message
git commit -m "%*"

REM pull down any upstream changes first (rebase to keep linear history)
git pull --rebase origin main

REM push back up
git push origin main
