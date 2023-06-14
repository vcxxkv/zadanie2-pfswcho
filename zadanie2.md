Zadanie2 - Krystian Wypart

1. (max. 100%)
Wykorzystując opracowaną aplikację (kod + Dockerfile) z zadania nr1 należy:
a. zbudować, uruchomić i potwierdzić poprawność działania łańcucha Github Actions,
który zbuduje obrazy kontenera z tą aplikacją na architektury: linux/arm64/v8 oraz linux/amd64 wykorzystując QEMU

W 1 kroku tworzymy plik opisujący działanie łańcucha GitHub Actions

Zawartość pliku YML:

name: Docker Build
'on':
  push:
    branches:
      - main
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2
      - name: Set up QEMU
        uses: docker/setup-qemu-action@v1
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v1
      - name: DockerHub Login
        uses: docker/login-action@v1
        with:
          username: '${{ secrets.DOCKER_USERNAME }}'
          password: '${{ secrets.DOCKER_PASSWORD }}'
      - name: Build and push Docker images
        uses: docker/build-push-action@v2
        with:
          context: .
          push: true
          tags: |
            zygmuntdeveloper/server-image:linux-amd64
            zygmuntdeveloper/server-image:linux-arm64-v8
          platforms: 'linux/amd64,linux/arm64/v8'


Następnie po dokonaniu push'a do repo, następuje wywołanie łańcucha GitHub Actions, jego wyniki prezentują się następująco:

<img width="1306" alt="Zrzut ekranu 2023-06-14 o 22 53 03" src="https://github.com/vcxxkv/zadanie2-pfswcho/assets/134099778/e5cff443-18e4-4376-9bf9-145f1ba79592">
<img width="1288" alt="Zrzut ekranu 2023-06-14 o 22 53 22" src="https://github.com/vcxxkv/zadanie2-pfswcho/assets/134099778/ea24dc47-5521-4c2a-95f4-9735020d963b">

Stworzone obrazy zgodnie z kolejnymi krokami są dodane do repozytorium na platformie Docker Hub

<img width="561" alt="Zrzut ekranu 2023-06-14 o 22 52 46" src="https://github.com/vcxxkv/zadanie2-pfswcho/assets/134099778/65b0e0c6-a2c1-4705-af34-ff10f874303a">
