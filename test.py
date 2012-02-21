import aifc

file = aifc.open('aiff_01.aif')
print file.getnchannels()
print file.getsampwidth()
print file.getframerate()

