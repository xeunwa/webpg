Playground for web exploits/vulns 

Running Docker file
```sh
docker build -t webpg .
docker run -p 5000:5000 webpg
```

Setting up requirements and venv
```sh
python3 -m venv venv
pip3 install -r requirements.txt
# installing package
# pip3 install -r flask

# generating requirements.txt
pip3 freeze > requirements.txt
```

