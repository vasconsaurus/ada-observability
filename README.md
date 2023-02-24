### **constrói a imagem**

`docker image build -t ada-deva-observability .`

### **constrói a imagem do app-client**

`docker image build -t adda-app-client -f Dockerfile-client .`

### **roda conteiner pela linha de comando**

`docker run -p 5001:5001 -d ada-deva-observability`

### **roda conteiner pelo docker compose**

`docker-compose up`
