# spring-config-vault-demo

This is a small demo with Vault and Spring Cloud Config Server. Only for Demo pur.

---

### Table of Contents

- [spring-config-vault-demo](#spring-config-vault-demo)
    - [Table of Contents](#table-of-contents)
  - [Requirements](#requirements)
    - [Setup](#setup)
    - [Usage](#usage)
  - [Project Structure](#project-structure)
  - [Contact](#contact)
  - [License](#license)

---

## Requirements

- Docker && Docker compose 
- Python 3

### Setup

The Spring Config Server and the Vault are delivered as containers. To start both use docker compose.

```
$ docker-compose up
```

You now can populate the Vault with the following python script. This will create three secrets: foo, bar, sql

```
$ python3 generate_sample_secrets.py
```
Now we want to apply a policy for each secret and generate a token for each secret based on the policies. Run following python script to apply the vault policies and generate a JSON file with the tokens.

```
$ python3 generate_tokens.py
```

Now everything is setup and we can test the demo.

### Usage

Following command will make foos secret available,
```
$ curl -X "GET" "http://localhost:8888/foo/default" -H "X-Config-Token:  <foo_client_token in tokens.json>" | jq
```
Following command will give you permission denied, because you try to access a secret for which you don't have any permissions
```
$ curl -X "GET" "http://localhost:8888/sql/default" -H "X-Config-Token:  <foo_client_token in tokens.json>" | jq
```



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
└── vault
    └── policies/                   //vault policies which get applied by generate_tokens.py
```


---

## Contact

Reach out to me at one of the following places!

- Mail at <a href="mailto:tgretler@vmware.com">`tgretler@vmware.com`</a>

---

## License

TBA
