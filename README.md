# TP6
The TP6 project is part of the "Administrateur Infrastructures et Cloud" cursus of Openclassrooms.
The goal is to write a Python script code that will automate admin tasks.
We propose to install a GLPI server using a MariaDB database under a Ubuntu 20.04 server and to configure HTTPS 443 with a autosigned certificate.
The choice to keep an autosigned certificate and not to use tools such as letsencrypt or certbot can be justified because we do not use any public domain name.

### users and passwords
GLPI Database : glpi / glpi
MariaDB : root / P@ssw0rd

### installation-prerequis.py
This first script goal is to install all required the packets including MariaDB
That script ends up with the secure-mysql script that will ask for interactive choices to the user such as password or remote login (security purpose)
You must identify the last GLPI stable version. You can know it by clicking on this link https://github.com/glpi-project/glpi/releases
Then edit the line 35 of the file and replace if necessary the string of the variable GLPI_VER = "9.5.6" to match the new version.

### configuration-https.py
This second script will prepare http for Apache2 server
It will generate a Diffie Hellmann group if this one does not exist and also create a configuration Apache file for SSL

### configuration-glpi.py
The third and last script is to configure the MariaDB database, Apache and GLPI.
User wil be prompted to enter User and password credentials

### full-install.py
This script is the main script that will launch the three other scripts

### Logs
Each script will create its own log file at the root of the project folder, and errors will be logged onto it.
