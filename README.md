# Quick start

```bash
git clone https://github.com/utec-pi-facerecognition/frecognition.git

git submodule init

git submodule update

or 

git clone --recurse-submodules https://github.com/utec-pi-facerecognition/frecognition.git
```

```bash
cd frontend
npm install
```

# Initialize docker-compose
```bash
docker-compose up
```

## Initialize in dettach mode (container starts up and runs in background)
```bash
docker-compose up -d
```

# Remove containers
```bash
docker-compose down
```