FROM cormorack/hypercorn:python3.7-conda4.9.2

WORKDIR /home/user1/newapp

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
ENV HYPERCORN_CMD_ARGS="--reload"
COPY /home/user/web_scrapping/app .

EXPOSE 5000

CMD ["hypercorn", "main:app"]

