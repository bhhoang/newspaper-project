import requests

url = "https://static.wikia.nocookie.net/oshi_no_ko/images/b/b0/AiHoshino.png/revision/latest?cb=20210820021211"

# request then save the image
r = requests.get(url, allow_redirects=True)
open('test.png', 'wb').write(r.content)