RFID Reader with InfuxDB & Grafana Using MFRC522-python
==============
Reads UID from RFID using the MFRC522-python class created by [mxgxw](https://github.com/mxgxw), which was a python port of MF522-AN.
Currently also authenticates hardcoded users, logs details to terminal, file and InfluxDB. This can then be imported to Grafana.
 
**Important notice from the class creator:** This library has not being actively updated in almost four years.
It might not work as intended on more recent Raspberry Pi devices. You might want to 
take a look to the open pull-requests and forks to see other implementations and bug-fixes.

## Requirements
- [SPI-Py - lthiery](https://github.com/lthiery/SPI-Py)

- [MFRC5522-python - mxgxw](https://github.com/mxgxw/MFRC522-python)

## GPIO Connection / Pins
You can use [this](http://i.imgur.com/y7Fnvhq.png) image for reference.

| Name | Pin # | Pin name   |
|:------:|:-------:|:------------:|
| SDA  | 24    | GPIO8      |
| SCK  | 23    | GPIO11     |
| MOSI | 19    | GPIO10     |
| MISO | 21    | GPIO9      |
| IRQ  | None  | None       |
| GND  | Any   | Any Ground |
| RST  | 22    | GPIO25     |
| 3.3V | 1     | 3V3        |

## Usage
Import the class by importing MFRC522 in the top of your script. For more info see the examples.

## To Do
- Add Functionality to add 

## Credit
- [Initial Fork from MFRC5522-python - mxgxw](https://github.com/mxgxw/MFRC522-python)

- [SPI-Py - lthiery](https://github.com/lthiery/SPI-Py)

## License
This code and examples are licensed under the GNU Lesser General Public License 3.0.