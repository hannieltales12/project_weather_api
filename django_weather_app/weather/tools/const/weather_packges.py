

class WeatherPackage:
    """Pacote de utilizadades utilizadas no projeto
    """

    URL_CONSULTA = 'http://sinda.crn.inpe.br/PCD/SITE/novo/site/cidades.php?uf=RN'


    HEADERS_SITE_CONSULTA = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Upgrade-Insecure-Requests': '1',
        'Host': 'sinda.crn.inpe.br'
    }
