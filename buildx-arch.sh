#!/bin/sh
docker buildx build --platform linux/arm64/v8 -t zygmuntdeveloper/server-image:linux-arm64-v8 --push .

