# qrdecode

Service web de décodage d'un QR Code

Le script prend une image avec un QR Code et affiche les données, éventuellement codées, qu'il contient.

## Usage

Via Docker, pour instancier le conteneur :

```bash
docker run -p 80:80 --rm -it $(docker build -q .)
```

ou

Via l'interpréteur Python3

```
pip3 install -r requirements.txt
python3 ./app/server.py
```

Allez sur http://127.0.0.1 et uploader l'image

![qrcode](qrcode.jpg)

![capture](screenshot.png)
