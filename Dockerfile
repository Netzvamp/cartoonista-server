FROM python:3.8-slim
MAINTAINER Robert Lieback <robertlieback@zetabyte.de>
WORKDIR /srv
COPY cartoonista-server /srv
COPY requirements.txt /srv
RUN pip install -r requirements.txt && \
    pip install gunicorn
EXPOSE 5000
CMD ["/usr/local/bin/gunicorn", "-b", "0.0.0.0:5000", "app:app",  "--workers", "4"]