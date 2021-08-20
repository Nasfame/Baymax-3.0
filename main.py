from JarvisAI import JarvisAssistant

baymax = JarvisAssistant(sync=True,token="436c57eab581dbb2253cfa77c41574f6")

while 1:
    res = baymax.mic_input(lang='en')
    print(res)