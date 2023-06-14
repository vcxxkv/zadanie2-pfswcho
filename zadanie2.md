Zadanie2 - Krystian Wypart

1. (max. 100%)
Wykorzystując opracowaną aplikację (kod + Dockerfile) z zadania nr1 należy:
a. zbudować, uruchomić i potwierdzić poprawność działania łańcucha Github Actions,
który zbuduje obrazy kontenera z tą aplikacją na architektury: linux/arm64/v8 oraz linux/amd64 wykorzystując QEMU

W 1 kroku tworzymy plik opisujący działanie łańcucha GitHub Actions

Zawartość pliku YML:

<img width="1051" alt="Zrzut ekranu 2023-06-14 o 22 53 54" src="https://github.com/vcxxkv/zadanie2-pfswcho/assets/134099778/42d2f414-468a-4021-a02a-53a213ae0e49">


Następnie po dokonaniu push'a do repo, następuje wywołanie łańcucha GitHub Actions, jego wyniki prezentują się następująco:

<img width="1306" alt="Zrzut ekranu 2023-06-14 o 22 53 03" src="https://github.com/vcxxkv/zadanie2-pfswcho/assets/134099778/e5cff443-18e4-4376-9bf9-145f1ba79592">
<img width="1288" alt="Zrzut ekranu 2023-06-14 o 22 53 22" src="https://github.com/vcxxkv/zadanie2-pfswcho/assets/134099778/ea24dc47-5521-4c2a-95f4-9735020d963b">

Stworzone obrazy zgodnie z kolejnymi krokami są dodane do repozytorium na platformie Docker Hub

<img width="561" alt="Zrzut ekranu 2023-06-14 o 22 52 46" src="https://github.com/vcxxkv/zadanie2-pfswcho/assets/134099778/65b0e0c6-a2c1-4705-af34-ff10f874303a">
