FROM python

ENV BIND_PORT 5000

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY ./event_parser.py /event_parser.py

EXPOSE 5000

CMD [ "python", "/event_parser.py" ]
