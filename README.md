# ToDo FastAPI pet project
ToDo pet project

### JWT Auth local setup

Go to devops/cert.

```shell
openssl genrsa -out auth_private_key.pem 2048
```

```shell
openssl rsa -in auth_private_key.pem -outform PEM -pubout -out auth_public_key.pem
```