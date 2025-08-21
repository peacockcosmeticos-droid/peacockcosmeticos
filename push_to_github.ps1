Write-Host "Pushing to GitHub..." -ForegroundColor Green

# Push to GitHub
try {
    git push -u origin master
    Write-Host "Successfully pushed to GitHub!" -ForegroundColor Green
} catch {
    Write-Host "Error pushing to GitHub: $_" -ForegroundColor Red
}

Write-Host "Press any key to continue..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
