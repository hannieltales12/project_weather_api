import requests
import re

from weather.models import WeatherData
from weather.tools.const.weather_packges import WeatherPackage



class LandingStepWeatherPage():
    """Etapa de extração bruta dos dados da página do clima de RN
    """

    def __init__(self):
        self.url = WeatherPackage.URL_CONSULTA

    def execute(self):
        """Função principal para realizar a extração dos dados da página
        """
        lista_id = self._get_page()

        for id in lista_id:
            self._get_station(id)

    def _get_page(self) -> list:
        """Função básica para obter conteudo da pagina completa

        Returns:
            lista_id (list): Lista de ids referente as estações extraídas da página
        """

        session = requests.Session()

        response = session.get(self.url, headers=WeatherPackage.HEADERS_SITE_CONSULTA)

        page_content = response.text

        regex_station = re.compile(r"tabela\.php\?id=(\d+).+?>([^<]+)</a></td><td>\s*<a.+?>([^<]+)</a></td><td>([^<]+)</td>")

        matches = regex_station.findall(page_content)

        lista_station = [{'id': m[0], 'estacao': m[2], 'municipio': m[3]} for m in matches]

        lista_id = []

        for station in lista_station:

            lista_id.append(station.get('id'))

            WeatherData.objects.create(
                cidade=station.get('municipio'),
                estacao=station.get('estacao'),
                id=station.get('id'),
                latidude='0',
                logintude='0'
            )

        return lista_id

    def _get_station(self, id_station: str) -> None:
        """Função para obter as estações da pagina pelo id

        Args:
            id_station (str): id da estação obtida do site

        Returns:
            page_content(str): conteudo da estação"""

        session = requests.Session()

        response = session.get(self.url.format(id_station), headers=WeatherPackage.HEADERS_SITE_CONSULTA)

        page_content = response.text

        regex_station = re.compile(r"<td>(-?\d+°\d+'\d+,?\d*''?)</td><td>(-?\d+°\d+'\d+,?\d*''?)</td>")

        match = regex_station.search(page_content)

        if match:

            latitude = match.group(1)
            longitude = match.group(2)

            WeatherData.objects.filter(id=id_station).update(latidude=latitude, logintude=longitude)

        else:

            WeatherData.objects.filter(id=id_station).update(latidude='0', logintude='0')