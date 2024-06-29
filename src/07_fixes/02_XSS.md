
# XSS
Dieses keyword "safe" muss in der tasks.html entfernt werden:
    "<td>{{ todo[1] | safe }}</td>" wird zu: 
    "<td>{{ todo[1] }}</td>"
![alt text](image.png)
