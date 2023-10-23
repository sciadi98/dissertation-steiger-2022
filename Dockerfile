FROM python:3

WORKDIR /app
COPY . .
RUN ./install.sh

CMD ["./SFT_analysis.sh"]
