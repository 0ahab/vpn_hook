from errbot import BotPlugin, webhook
import subprocess
import sys

class VPNHook(BotPlugin):
	"""Errbot plugin to run reverse shell"""
	@webhook('/vpnhook/<name>/')
	def vpnhook(self, request, name):
		identifier = self.build_identifier('#ops/casper')
        self.send(identifier, "%s logged into VPN" % name)

# bang
