# Workshop IoT

## Python klient

Přihlašovací údaje:

-   stránka [https://iotdomu.cz](https://iotdomu.cz)
-   api_key `qUOm0nOReG0fjos1WfGUUpJuucktj9`
-   userName `test`
-   password `test`

```python
import requests
import time

api_key = "YOUR_SECRET_API_KEY"

def send_action(action: str):
    return requests.post(f"{action}&api_key={api_key}")


action1 = "some_action_url"
action2 = "some_action_url"

r = send_action(action1)
print("status code: ",r.status_code)
print("response obj:",r)

time.sleep(4)
r = send_action(action2)
```

> Pokud po spuštění dostáváte chybu `ModuleNotFoundError: No module named 'requests'`, tak nejprve je potřeba modul nainstalovat spuštěním příkazu:
> `pip install requests`
