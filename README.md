docker image build -t ada-deva-observability .

docker run -p 5001:5001 -d ada-deva-observability
