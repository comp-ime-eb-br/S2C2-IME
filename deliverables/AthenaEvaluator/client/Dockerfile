# Use uma imagem base oficial do Node.js
FROM node:22-alpine

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo package.json e package-lock.json para o diretório de trabalho
COPY package.json package-lock.json ./

# Instale as dependências do Node.js
RUN npm install

# Copie o restante do código da aplicação para o diretório de trabalho
COPY . .

# Construa o projeto Next.js
RUN npm run build

# Exponha a porta em que a aplicação será executada
EXPOSE 3000

# Comando para rodar a aplicação
CMD ["npm", "start"]