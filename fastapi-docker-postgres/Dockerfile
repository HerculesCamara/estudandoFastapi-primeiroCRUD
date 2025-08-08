# 1. Use uma imagem base oficial do Python
FROM python:3.11-slim

# 2. Defina o diretório de trabalho dentro do container
WORKDIR /code

# 3. Copie o arquivo de dependências para o container
COPY ./requirements.txt /code/requirements.txt

# 4. Instale as dependências
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 5. Copie o código da sua aplicação para o container
COPY ./app /code/app

# 6. Comando para executar a aplicação quando o container iniciar
# O host 0.0.0.0 é crucial para que a aplicação seja acessível de fora do container
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]