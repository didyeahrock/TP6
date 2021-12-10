#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
    configuration-https.py
    This script will configure HTTP and create certificates
    Athor   :   Didier Lemaitre
    Version :   0.1
    Date    :   09-12-2021
    Tested with Python 3.7 under Ubuntu 20.04
"""
# Importation of the requiered modules
import logging
import os
import subprocess
"""
    Tasks to do : 
        - Configure apache for ssl
        - Configure the group Diffie Helman
"""
# Définition of constants

LOG_FILE = "./configuration-https.log"

# Configuration of the log file
try:
    logging.basicConfig(filename=LOG_FILE, format="%(asctime)s : %(levelname)s:%(message)s",
            level=logging.DEBUG)
    logging.info("Starting https configuration for apache")
except Exception as e:
    print("")
    raise e
# Generate the group Diffie Hellmann to improve the certificate security des certificats if the file does not exist 
try:
    logging.info("Generate the file of the group Diffie Hellmann /etc/ssl/certs/dhparam.pem")
    print("Generate the file of the group Diffie Hellmann /etc/ssl/certs/dhparam.pem...")

    if not os.path.isfile("/etc/ssl/certs/dhparam.pem"):
        creation_dh_group = "openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048"
        os.system(creation_dh_group)
        logging.info("File has been created successfully")
        print("File has been created successfully\n")
    else:
        logging.info("The file already exists, it has not been mofified")
        print("The file already exists, it has not been modified\n")
except Exception as e:
    logging.error("Creation of the Diffie Hellmann group has failed")
    logging.error(e)
    raise e
# Generate the file /etc/apache2/conf-available/ssl-params.conf
try:
    ssl_params = [
            "SSLCipherSuite EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH\n",
            "SSLProtocol All -SSLv2 -SSLv3\n",
            "SSLHonorCipherOrder On\n",
            "Header always set Strict-Transport-Security \"max-age=63072000; includeSubdomains\"\n",
            "Header always set X-Frame-Options DENY\n",
            "Header always set X-Content-Type-Options nosniff\n",
            "SSLCompression off\n",
            "SSLSessionTickets Off\n",
            "SSLUseStapling on\n",
            "SSLStaplingCache \"shmcb:logs/stapling-cache(150000)\"\n",
            "SSLOpenSSLConfCmd DHParameters \"/etc/ssl/certs/dhparam.pem\"\n"
            ]

    logging.info("Creation of the file /etc/apache2/conf-available/ssl-params.conf")
    print("Creation of tje file /etc/apache2/conf-available/ssl-params.conf...")
    
    if not os.path.isfile("/etc/apache2/conf-available/ssl-params.conf"):
        with open("/etc/apache2/conf-available/ssl-params.conf", "w") as ssl_params_file:
            ssl_params_file.writelines(ssl_params)
            logging.info("The file has been successfully created")
            print("The file has been successfully created\n")
    else:
        logging.info("The file ssl-params.conf already exists, it has not been modified")
        print("The file ssl-params.conf already exists, it has not been modified.\n")
 
except Exception as e:
    logging.error("Creation of the file /etc/apache2/conf-available/ssl-params.conf has failed")
    logging.error(e)
    raise e
