@echo off
echo Adding remote repository...
git remote add origin https://github.com/heroncosmo/testess.git

echo Pushing to GitHub...
git push -u origin main

echo Done!
pause
