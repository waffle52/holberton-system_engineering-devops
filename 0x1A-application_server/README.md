# 0x1A-application_server
Project to set up application server on remote ubuntu server.
## 2-app_server-nginx_config
Building on your work in the previous tasks, configure Nginx to serve your page from the route /airbnb-onepage/
Requirements:
Nginx must serve this page both locally and on its public IP on port 80.
Nginx should proxy requests to the process listening on port 5000.
Include your Nginx config file as 2-app_server-nginx_config.
## 3-app_server-nginx_config
Building on what you did in the previous tasks, let’s expand our web application by adding another service for Gunicorn to handle. In AirBnB_clone_v2/web_flask/6-number_odd_or_even, the route /number_odd_or_even/<int:n> should already be defined to render a page telling you whether an integer is odd or even. You’ll need to configure Nginx to proxy HTTP requests to the route /airbnb-dynamic/number_odd_or_even/(any integer) to a Gunicorn instance listening on port 5001. The key to this exercise is getting Nginx configured to proxy requests to processes listening on two different ports. You are not expected to keep your application server processes running. If you want to know how to run multiple instances of Gunicorn without having multiple terminals open, see tips below.
Requirements:
Nginx must serve this page both locally and on its public IP on port 80.
Nginx should proxy requests to the route /airbnb-dynamic/number_odd_or_even/(any integer) the process listening on port 5001.
Include your Nginx config file as 3-app_server-nginx_config.
## 4-app_server-nginx_config
Let’s serve what you built for AirBnB clone v3 - RESTful API on web-01.
Requirements:
Git clone your AirBnB_clone_v3
Setup Nginx so that the route /api/ points to a Gunicorn instance listening on port 5002
Nginx must serve this page both locally and on its public IP on port 80
To test your setup you should bind Gunicorn to api/v1/app.py
It may be helpful to import your data (and environment variables) from this project
Upload your Nginx config file as 4-app_server-nginx_config
## 5-app_server-nginx_config
Let’s serve what you built for AirBnB clone - Web dynamic on web-01.
Requirements:
Git clone your AirBnB_clone_v4
Your Gunicorn instance should serve content from web_dynamic/2-hbnb.py on port 5003
Setup Nginx so that the route / points to your Gunicorn instance
Setup Nginx so that it properly serves the static assets found in web_dynamic/static/ (this is essential for your page to render properly)
For your website to be fully functional, you will need to reconfigure web_dynamic/static/scripts/2-hbnb.js to the correct IP
Nginx must serve this page both locally and on its public IP and port 5003
Make sure to pull up your Developer Tools on your favorite browser to verify that you have no errors
Upload your Nginx config as 5-app_server-nginx_config
