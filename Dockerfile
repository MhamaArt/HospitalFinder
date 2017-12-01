FROM python:3.5

# Update aptitude with new repo
RUN apt-get update

# Install software
RUN apt-get install -y apt-utils git libhunspell-dev libpq-dev

# since Quay.IO check out will results in a different timestamp to the cache
ADD .git/HEAD /app/CACHE_BUSTER
RUN rm /app/CACHE_BUSTER

ADD / /code

RUN pip install -r /code/requirements.txt
WORKDIR /code