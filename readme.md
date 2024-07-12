# pyboard-badusb

## Description
Simple pyboard v1 badusb implementation.


## Usage

Before you can upload this project to the pyboard, you must to prepare a file with a payload, or use example one from payloads directory. Payload file must be named payload.json and placed in the root directory of the project.

> [!NOTE]
> Payload is a JSON file with keystrokes sent to the victim computer. 

> [!NOTE]
> There is a converter which allows to covert a text file with a raw payload to the format supported by the pyboard.

```
python3 ./converter.py raw_payload.txt payload.json
```

To deploy to the pyboard use the depoy.sh script, or copy and paste files to the pyboard flash.
> [!IMPORTANT]
> You need to modify the deploy.sh script to include the directory the script is based in. You may also need to change port.
