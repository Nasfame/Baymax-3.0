from JarvisAI import JarvisAssistant

baymax = JarvisAssistant(sync=True,token="436c57eab581dbb2253cfa77c41574f6")

print("SD")
while 1:
    res = baymax.mic_input(lang='en')
    print(res)