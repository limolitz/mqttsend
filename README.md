# mqttsend

Mqttsend is a little bash and python tool which receives a JSON object over stdin and sends it out over MQTT under the given topic, a configurable username and the current hostname.

## Dependencies

* Python3
* paho-mqtt==1.3.0

Make a virtualenv `python3 -m venv .` and install via `pip install -r requirements.txt`.

## Configuration

Copy the file `config.ini.sample` to `config.ini` and adjust the contents.

## Usage
Pipe your JSON to mqttsend.sh. That's it!

JSON should contain keys named `topic` and `measurements`. It may contain a key named `timestamp`. If there is none, this tool adds one via `utcnow`.
