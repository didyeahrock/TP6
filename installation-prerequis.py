#!/usr/bin/python3
# -*- coding: utf8 -*-
"""   installation-prerequis.py
    Script to install a GLPI server with a maria DB database and apache2 server
    Author :    Didier Lemaitre
    Version :   0.1
    Date :      2021-11-01
    Tested with Python 3.7 running on a Ubuntu 20.04 

"""
#Import of required modules

import logging
import subprocess
import os

"""
    Paquets to be installed : 
        apache2
        php
        mariadb-server
        curl 
        python3
        module python validators
        module python mariadb
        pip

    Configuration de base :
        mysql_secure_installation

"""
#constants Définitions

LOG_FILE = "./installation.log"
GLPI_VER = "9.5.6"

# Log File Configuration 

try:
    logging.basicConfig(filename=LOG_FILE, format="%(asctime)s : %(levelname)s:%(message)s", 
        level=logging.DEBUG)
    logging.info("Début de l'installation des pré-requis")
except Exception as e:
    print("Erreur lors de la création du fichier de journalisation")
    raise e

# system update and paquet Installation

try:
    logging.info("system update and paquet Installation...")
    os.system("apt update ; apt upgrade")
    os.system("dpkg --configure -a")
    os.system("apt install -y apache2 php mariadb-server curl python3 python3-pip libmariadbclient-dev pip php-mysql php-json php-gd php-curl php-mbstring php-cas php-xml php-cli php-imap php-ldap php-xmlrpc php-apcu php7.4-intl php7.4-bz2 php7.4-zip")
    os.system("pip install upgrade setuptools")
    os.system("pip install validators")
    os.system("pip install mariadb")
    os.system("mysql_secure_installation")
# Installation of GLPI
    os.system("cd /tmp")
    wget = "wget https://github.com/glpi-project/glpi/releases/download/{}/glpi-{}.tgz".format(GLPI_VER,GLPI_VER)
#    os.system("wget https://github.com/glpi-project/glpi/releases/download/9.5.6/glpi-9.5.6.tgz")
    os.system(wget)
    tar_glpi = "tar -zxvf glpi-{}.tgz".format(GLPI_VER)
    os.system(tar_glpi)
# Moving /tmp/glpi to the root folder of apache2 
    os.system("mv glpi /usr/share/")
# make www-data owner of GLPI folder
    os.system("chown -R www-data /usr/share/glpi")
    logging.info("system update and paquet installations succeeded !")
    exit(0)
except Exception as e:
    print("p.5.6aquets installation failed !")
    logging.error("paquets installation failed !")
    logging.error(e)
    raise e
