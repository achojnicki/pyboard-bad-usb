# pyboard-badusb

## Description
Simple pyboard v1 badusb implementation.


## Usage

Before you can upload this project to the pyboard, you must prepare a file with a payload. Payload file must be named payload.json and placed in the root directory of the project.

> [!NOTE]
> Payload is a JSON file with keystrokes sent to the victim computer. 

There is a converter which allows you to covert a text file with a raw payload to the format supported by the pyboard.

```
python3 ./convert.py ./payloads/colorful.txt payload.json
```

To deploy to the pyboard use the depoy.sh script, or copy and paste files to the pyboard flash.
> [!IMPORTANT]
> You need to modify the deploy.sh script to include the directory the script is based in. You may also need to change the port.
