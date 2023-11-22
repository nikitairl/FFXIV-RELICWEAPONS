FROM nginx

COPY relicweapons.com.crt /etc/ssl/
COPY relicweapons.com.key /etc/ssl/

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/