FROM amd64/ubuntu

ENV OPENAI_API_KEY=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


WORKDIR /tmp
ARG DEBIAN_FRONTEND=noninteractive

# Install necessary libraries for subsequent commands
RUN apt-get update && apt-get install -y wget git dumb-init python3 python3-distutils python3-pip python3-apt

EXPOSE 8000

COPY . .

RUN pip3 install -r requirements.txt



CMD ["gunicorn", "-b","0.0.0.0:8000","wsgi:app"]
