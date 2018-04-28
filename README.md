# Home page project for mahkonen.org

Things to get running
* Using Swagger for interface definitions
* Using Jenkins for CI/CD
* Using Nginx as web backend
* Using Jquery, Bootsrap, web-components and Polymmer (testing)
* Learning CI/CD

## TODOs:
* Iamge server fro family fotos
* IoT
	..* Temperature sensors Arduino
		....* Time series data
		....* Graphs
	..* Raspberry Pi cameras
	..* Images and video from Nest and Arlo (hopefully)
	..* Personal page

## Firewall (UFW):
```
sudo ufw allow OpenSSH
sudo ufw enable (Warning you may lose connectivity here to the server!)
sudo ufw status
```

## Nginx (https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-16-04):
```
sudo apt-get update
sudo apt-get install nginx
sudo ufw allow 'Nginx HTTP'
sudo ufw status
```

Test that Nginx is running by browsing to your server.

### Setup you site (https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04):
```
sudo mkdir -p /var/www/<domainname>/html
sudo chmown -R $USER:$USER /var/www/<domainname>/html
sudo chmod -R 755 /var/www
```

Deploy your sites under src:
```
src/deploy.sh
```

### Create and enable serve block files:
```
sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/<domainname>
sudo sed -i.bak 's/ default_server//g' /etc/nginx/sites-available/<domainname>
sudo sed -i.bak 's\/var/www/html\/var/www/<domainname>/html\g' /etc/nginx/sites-available/<domainname>
sudo sed -i.bak 's/server_name _/server_name <domainname> www.<domainname>/' /etc/nginx/sites-available/<somainname>
sudo ln -s /etc/nginx/sites-available/<domainname> /etc/nginx/sites-enabled
sudo cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.orig (Just in case!)
sudo sed -i.bak 's/# server_names_hash_bucket_size 64;/server_names_hash_bucket_size 64;/' /etc/nginx/nginx.conf
sudo nginx -t (To check configs!)
```

### HTTPS (https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-16-04):
```
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install python-certbot-nginx
sudo ufw allow 'Nginx Full'
sudo ufw delete allow 'Nginx HTTP'
sudo certbot --nginx -d mahkonen.org -d www.mahkonen.org
(sudo certbot renew --dry-run)
```

## Jenkins (https://www.digitalocean.com/community/tutorials/how-to-install-jenkins-on-ubuntu-16-04):
```
wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -
echo deb https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list
sudo apt-get update
sudo apt-get install jenkins
sudo service start jenkins
sudo service status jenkins
sudo ufw allow 8080
```
With a browser go to server port 8080. Then initial admin password is in /var/lib//jenkins/secrets/initialAdminPassword file. Use it to login and install suggested plugins. Create first admin account and login.

## TBD:
* https://www.digitalocean.com/community/tutorials/how-to-configure-jenkins-with-ssl-using-an-nginx-reverse-proxy
* https://www.digitalocean.com/community/tutorials/how-to-set-up-continuous-integration-pipelines-in-jenkins-on-ubuntu-16-04
https://jenkins.io/doc/pipeline/tour/hello-world/