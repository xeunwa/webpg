Playground for web exploits/vulns 

(Docker) Running Docker file
```sh
docker build -t webpg .
docker run -p 5000:5000 webpg
```

(Local) Setting up requirements and venv
```sh
python3 -m venv venv
pip3 install -r requirements.txt

# generating requirements.txt
pip3 freeze > requirements.txt
```

