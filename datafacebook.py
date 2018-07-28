from urllib import request

url = 'https://www.facebook.com/profile.php?id=100011698513746'
resp = request.urlopen(url).read().decode('utf-8')
print(resp)
