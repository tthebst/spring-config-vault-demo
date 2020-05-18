# spring-config-vault-demo

This is a small demo with Vault and Spring Cloud Config Server. Only for Demo purposes!

---

### Table of Contents

- [spring-config-vault-demo](#spring-config-vault-demo)
    - [Table of Contents](#table-of-contents)
  - [Requirements](#requirements)
  - [Setup](#setup)
  - [Usage](#usage)
  - [Details](#details)
  - [Project Structure](#project-structure)
  - [Troubleshooting](#troubleshooting)
  - [Contact](#contact)
  - [License](#license)

---

## Requirements

- Docker && Docker compose 
- Python 3

--- 

## Setup

You can start the setup with docker compose. 

```
$ docker-compose up
```

---

Now everything is setup and we can test the demo.

## Usage

The web application is available at [localhost:8080](http://localhost:8080). You can now query the pagilia database from the web application.

--- 

## Details

![alt text]((https://github.com/tthebst/spring-config-vault-demo/blob/postgres/graphics/app.pdf))







---
## Project Structure

```
.
├── README.md
├── configserver
│   ├── Dockerfile                  // Dockerfile to create Spring cloud server
│   ├── HELP.md
│   ├── mvnw
│   ├── mvnw.cmd
│   ├── pom.xml
│   ├── src                         // java application source code
├── docker-compose.yml              // Dockercompose file for microservices
├── generate_sample_secrets.py      // python script to apply sample secrets
├── generate_tokens.py              // python script for token generation
├── tokens.json                     // tokens which are generated
├── postgres
│   ├── Dockerfile                  // Dockerfile for postgres
│   ├── init-db.sh                  // init script for database, populates db with schema and data from *.sql files
│   ├── init.sh                     // db init scripts which registers password with vault
│   ├── pagila-data.sql             // sql data
│   └── pagila-schema.sql           // sql schema
├── webapp
│   ├── Dockerfile                  // Dockerfile for web applications
│   ├── app.py                      // flask app
│   └── templates/                  // html templates
└── vault
    └── policies/                   //vault policies which get applied by generate_tokens.py
```


---

## Troubleshooting

It is possible that docker-compose reuses volume from a previous deployment. This will cause misbehaviour in the postgres database initialization. To solve this run:

```
$ docker-compose up --renew-anon-volume
```

---

## Contact

Reach out to me at one of the following places!

- Mail at <a href="mailto:tgretler@vmware.com">`tgretler@vmware.com`</a>

---

## License

TBA
