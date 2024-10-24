# Use the official Nginx image from Docker Hub
FROM nginx

# Remove default Nginx config file
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom Nginx config file
COPY django.conf /etc/nginx/conf.d
