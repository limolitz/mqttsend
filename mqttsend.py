#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import configparser
import ssl
import json
import datetime
import subprocess
import sys

class MqttSender(object):
	"""docstring for ClassName"""
	#def __init__(self):


	def sendMQTT(self, topic, data):
		config = configparser.ConfigParser()
		config.read("config.ini")

		client = mqtt.Client()

		# Get configuration
		hostname = config.get("Account", "hostname")
		port = config.get("Account", "port")
		username = config.get("Account", "user")
		password = config.get("Account", "password")

		# Connect
		client.username_pw_set(username, password = password)
		client.tls_set(config.get("Account", "cacrtPath"), tls_version=ssl.PROTOCOL_TLSv1_2)
		client.connect(hostname, port, 60)

		uname = subprocess.Popen('uname -n', stdout=subprocess.PIPE, shell=True).stdout.read().strip()

		# Publish a message
		print("Topic: {}/{}/{}, data: {}".format(topic,username,uname,data))
		#client.publish(topic+"/"+username+"/"+uname, json.dumps(data))

	def parseStdIn(self):
		for line in sys.stdin:
			print(line)

if __name__ == "__main__":
	mqttSender = MqttSender()
	topic, data = mqttSender.parseStdIn()
	mqttSender.sendMQTT(topic,data)
