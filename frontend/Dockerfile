# Base Image
FROM nginx:alpine3.18-slim

# Remove the default nginx page.
RUN rm -rf /usr/share/nginx/html/*

# Copy the custom nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Copy the static files into the default nginx url
COPY static\ /usr/share/nginx/html

# Expose port.
EXPOSE 80