install:
	pip install pipwin
	pipwin install pyaudio
	pip --no-cache-dir install jarvisai
#	pip --no-cache-dir install -r requirements.txt

lint:
	py -m pylint app.py

test:
	python -m pytest -vv

all:
	install lint test
