Write-Host "🚀 Launching FedMed Hackathon System..." -ForegroundColor Green

# 1. Start Server (New Window)
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd 'F:\Devpost(Hackathon)\Fedmed Project'; python src/server.py"
Start-Sleep -Seconds 5

# 2. Start Hospital A
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd 'F:\Devpost(Hackathon)\Fedmed Project'; python src/client.py 0"

# 3. Start Hospital B
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd 'F:\Devpost(Hackathon)\Fedmed Project'; python src/client.py 1"

# 4. Start Dashboard
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd 'F:\Devpost(Hackathon)\Fedmed Project'; streamlit run src/dashboard.py"