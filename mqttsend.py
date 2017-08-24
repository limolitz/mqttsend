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
	def sendMQTT(self, topic, measurements):
		config = configparser.ConfigParser()
		config.read("config.ini")

		client = mqtt.Client()

		# Get configuration
		hostname = config.get("Account", "hostname")
		port = int(config.get("Account", "port"))
		username = config.get("Account", "user")
		password = config.get("Account", "password")

		# Connect
		client.username_pw_set(username, password = password)
		client.tls_set(config.get("Account", "cacrtPath"), tls_version=ssl.PROTOCOL_TLSv1_2)
		client.connect(hostname, port, 60)

		uname = subprocess.Popen('uname -n', stdout=subprocess.PIPE, shell=True).stdout.read().decode(encoding='UTF-8').strip()

		# Publish a message
		print("Topic: {}/{}/{}, data: {}".format(topic,username,uname,measurements))
		client.publish(topic+"/"+username+"/"+uname, json.dumps(data))

	def parseStdIn(self):
		try:
			data = json.load(sys.stdin)
			#print(data.keys())
			# expected data: topic, measurements
			# measurements should contain timestamp
			if "topic" in data.keys() and "measurements" in data.keys():
				measurements = data["measurements"]
				if "timestamp" in measurements.keys():
					print(data)
					return data["topic"], measurements
				else:
					print("Malformed data: No timestamp sent.")
			else:
				print("Malformed data: No topic sent.")
		except json.decoder.JSONDecodeError as e:
			print("Malformed data: {}".format(e.msg))




if __name__ == "__main__":
	mqttSender = MqttSender()
	topic, data = mqttSender.parseStdIn()
	mqttSender.sendMQTT(topic,data)
