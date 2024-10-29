# Use the official Nginx image from Docker Hub
FROM nginx

# Remove default server block file
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom Nginx config file
COPY nginx.conf /etc/nginx/nginx.conf
