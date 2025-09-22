import urllib
import urllib.request

try:
    site = urllib.request.urlopen(str(input('Cole a url do site aqui: ')))

except:
    print('Não foi possivel acessar esse site')

else:
    print('Site acessado com sucesso')
