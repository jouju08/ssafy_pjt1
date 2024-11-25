# Stage 1: Build the Vue.js application using Vite
FROM node:lts-alpine as build-stage

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# 임시로 파일 목록 출력
RUN ls -R /app

# Build the application
RUN npm run dev

# Stage 2: Serve the app with Nginx
FROM nginx:stable-alpine as production-stage

# Copy the built files from the previous stage to Nginx's html directory
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Copy custom Nginx configuration
COPY docker/nginx/vue.vhost.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

# Set environment variable for timezone
ENV TZ=Asia/Seoul

# Start Nginx when the container launches
CMD ["nginx", "-g", "daemon off;"]
