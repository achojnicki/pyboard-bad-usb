import pyb
import json
from map import keymap, mods


class Rei:
	def __init__(self):
		self._hid=pyb.USB_HID()
		self._switch=pyb.Switch()


		with open('payload.json','r') as f:
			self._payload=json.load(f)


	def _mod(self, mod, active):
		if active:
			return mods[mod]
		else:
			return 0

	def _send_keystrokes(self, char, ctrl=False, shift=False, alt=False, win=False):

		buff=bytearray(8)
		buff[0]=self._mod('lctrl', ctrl)|self._mod('lshift',shift)|self._mod('lalt',alt)|self._mod('lwin',win)
		buff[2]=keymap[char] if char in keymap else 0x00
		print('\t',buff)
		self._hid.send(buff)
		pyb.delay(10)
		buff[0]=0x00
		buff[2]=0x00
		self._hid.send(buff)
		pyb.delay(10)

	def _send_key(self, key):
		ctrl=True if 'ctrl' in key['mods'] else False
		alt=True if 'alt' in key['mods'] else False
		shift=True if 'shift' in key['mods'] else False
		win=True if 'win' in key['mods'] else False

		for k in key['keys']:
			self._send_keystrokes(
				char=k,
				alt=alt,
				ctrl=ctrl,
				shift=shift,
				win=win
				)
		if "delay" in key:
			pyb.delay(key['delay'])


	def send_payload(self):
		for item in self._payload:
			print(item)
			self._send_key(item)


	def loop(self):
		while True:
			if self._switch.value():
				self.send_payload()
				while self._switch.value():
					pyb.delay(1)
			pyb.delay(10)

rei=Rei()
rei.loop()