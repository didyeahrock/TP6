# TP6
The TP6 project part of the "Administrateur Infrastructures et Cloud" of Openclassrooms.
The goal is to write a Python script code that will automate admin tasks.

We propose ton install a GLPI server using a MariaDB database under a Ubuntu 20.04 server and ton configure HTTPS 443 with a autosigned certificate.

The choice to keep an autosigned certificate and not to use tools such as letsencrypt or certbot can be justified because we do not use any public domain name.

### installation-prerequis.py
This firts script goal is to install all required the packets includong MariaDB
Tha script ends up with the secure-mysql script that will ask for interactive choices to the user such as password or remote login (security purpose)

### configuration-https.py
This second script will prepare http for Apache2 server
It wil generate a Diffie Hellmann group if this one does not exist and also create a configuration Apache file for SSL

### configuration-glpi.py
The third and last script is to configure the MariaDB database, Apache and GLPI.
User wil be prompted to enter User and password credentials

### full-install.py
This script is the main script that will launch the three scripts

### Logs
Each script will create its own log file at the root of the project folder, and errors will be logged onto it.
