ARG STRAVA_ACCESS_TOKEN
ARG DATE
FROM  python:3.13-alpine3.22

ENV STRAVA_ACCESS_TOKEN=${STRAVA_ACCESS_TOKEN}
ENV DATE=${DATE}

COPY requirements.txt . 
RUN pip install -r requirements.txt

COPY core/ core/
COPY .env .
COPY main.py . 


CMD sh -c "python main.py"