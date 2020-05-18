from flask import Flask, render_template, request
import psycopg2
import requests
import hvac
import json
import os

app = Flask(__name__)
POSTGRES_PW = None
SQL_READ_TOKEN = None


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        # get posgres password from spring cloud config server
        r = requests.get("http://configserver:8888/sql/default",
                         headers={"X-Config-Token": SQL_READ_TOKEN})

        # get postgres password from configserver response
        POSTGRES_PW = r.json()[
            'propertySources'][0]["source"]["postgres-password"]

        # connect to postgres
        conn = psycopg2.connect(dbname="postgres", user="postgres",
                                password=POSTGRES_PW, host="postgres-db")
        cur = conn.cursor()
        # try to execute provided query
        try:
            cur.execute(str(request.form['query']))
            data = cur.fetchall()
        except Exception:
            return render_template("error.html")

        return render_template("base.html", data=data)

    return render_template("base.html")


if __name__ == "__main__":
    # connect to vault
    vault = hvac.Client(url='http://vault:8200',
                        token=os.environ['VAULT_TOKEN'], verify=False)
    read_only_sql = """
    path "secret/data/sql" {
        capabilities = ["read"]
    }

    path "secret/data/application" {
        capabilities = ["read"]
    }
    """
    # register new read only policy with vault
    vault.sys.create_or_update_policy(
        name='sql_read',
        policy=read_only_sql,
    )
    # create token for read only policy
    token = vault.create_token(policies=['sql_read'], lease='12h')
    SQL_READ_TOKEN = token['auth']['client_token']

    app.run(debug=True, host="0.0.0.0", port=8080)
