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
	def sendMQTT(self, topic, measurements, name):
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
		if name is None:
			print("Topic: {}/{}/{}, data: {}".format(topic,username,uname,measurements))
			client.publish("{}/{}/{}".format(topic,username,uname), json.dumps(measurements))
		else:
			print("Topic: {}/{}/{}/{}, data: {}".format(topic,username,uname,measurements,name))
			client.publish("{}/{}/{}/{}".format(topic,username,uname,name), json.dumps(measurements))

	def parseStdIn(self):
		try:
			data = json.load(sys.stdin)
			#print("Keys: {}".format(data.keys()))
			#print("Data: {}".format(data))
			# expected data: topic, measurements
			# could contain additional key name
			# measurements should contain timestamp
			if "topic" in data.keys() and "measurements" in data.keys():
				measurements = data["measurements"]
				if not("timestamp" in measurements.keys()):
					timestamp = datetime.datetime.utcnow().strftime("%s")
					#print("No timestamp sent. Using our own.")
					measurements["timestamp"] = timestamp
				if "name" in data.keys():
					return data["topic"], measurements, data["name"]
				else:
					return data["topic"], measurements, None
			else:
				print("Malformed data: No topic sent.")
		except json.decoder.JSONDecodeError as e:
			print("Malformed data: {}".format(e.msg))




if __name__ == "__main__":
	mqttSender = MqttSender()
	topic, data, name = mqttSender.parseStdIn()
	mqttSender.sendMQTT(topic,data,name)
