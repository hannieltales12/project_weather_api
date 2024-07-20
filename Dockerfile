FROM python:3.12.3-alpine3.18
LABEL mantainer="hannieltales@gmail.com"

# gravar arquivos de bytecode (.pyc) no disco. 1 = Não, 0 = Sim
ENV PYTHONDONTWRITEBYTECODE 1

# Define que a saída do Python será exibida imediatamente no console ou em
# outros dispositivos de saída, sem ser armazenada em buffer.
ENV PYTHONUNBUFFERED 1

# Copia a pasta "django_weather_app" e "scripts" para dentro do container.
COPY django_weather_app /django_weather_app
COPY scripts /scripts

# Entra na pasta djangoapp no container
WORKDIR /django_weather_app

# A porta 8000 estará disponível para conexões externas ao container
EXPOSE 8000

RUN python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r /django_weather_app/requirements.txt && \
  adduser --disabled-password --no-create-home duser && \
  mkdir -p /data/web/static && \
  mkdir -p /data/web/media && \
  chown -R duser:duser /venv && \
  chown -R duser:duser /data/web/static && \
  chown -R duser:duser /data/web/media && \
  chmod -R 755 /data/web/static && \
  chmod -R 755 /data/web/media && \
  chmod -R +x /scripts

# Adiciona a pasta scripts e venv/bin
# no $PATH do container.
ENV PATH="/scripts:/venv/bin:$PATH"

# Muda o usuário para duser
USER duser

# Executa o arquivo scripts/commands.sh
CMD ["commands.sh"]