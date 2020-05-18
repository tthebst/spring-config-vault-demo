#!/bin/bash

curl --header "X-Vault-Token: $VAULT_TOKEN" --request POST --data "$(jq -n --arg greeting $POSTGRES_PASSWORD --arg mykey postgres-password '{ data: {($mykey):$greeting}}')" vault:8200/v1/secret/data/sql
