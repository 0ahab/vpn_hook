from errbot import BotPlugin, webhook
import subprocess
import sys

class VPNHook(BotPlugin):
	"""Errbot plugin to run reverse shell"""
	@webhook('/vpnhook/<name>/')
	def vpnhook(self, request, name):
        identifier = self.build_identifier('#ops')
        self.send_card(title='Title + Body',
			body=name + ' has logged into the VPN.',
			thumbnail='https://raw.githubusercontent.com/errbotio/errbot/master/docs/_static/errbot.png',
			image='https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png',
			color='red')
