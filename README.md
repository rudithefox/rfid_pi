RFID Reader with InfuxDB using MFRC522-python
==============
Reads UID from RFID using the MFRC522-python class created by [mxgxw](https://github.com/mxgxw), which was a python port of MF522-AN.
Currently also authenticates hardcoded users, outputs details to terminal, file and InfluxDB.
 
**Important notice from the class creator:** This library has not being actively updated in almost four years.
It might not work as intended on more recent Raspberry Pi devices. You might want to 
take a look to the open pull-requests and forks to see other implementations and bug-fixes.

## Requirements
- [SPI-Py - lthiery](https://github.com/lthiery/SPI-Py)

- [MFRC5522-python - mxgxw](https://github.com/mxgxw/MFRC522-python)

## To Do
- Add Functionality to manage users.

## Credit
- [Initial Fork from MFRC5522-python - mxgxw](https://github.com/mxgxw/MFRC522-python)

- [SPI-Py - lthiery](https://github.com/lthiery/SPI-Py)

## License
This code and examples are licensed under the GNU Lesser General Public License 3.0.
