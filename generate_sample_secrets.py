import hvac

# connect to vault
client = hvac.Client(url='http://localhost:8200', token="myroot", verify=False)

foo_secret = {"foo": "foos super secret foo"}
client.secrets.kv.v2.create_or_update_secret(
    path='foo',
    secret=foo_secret,
)

bar_secret = {"bar": "bars super secret bar"}
client.secrets.kv.v2.create_or_update_secret(
    path='bar',
    secret=bar_secret,
)

sql_secret = {"sql-cert": "put sql cert here"}
client.secrets.kv.v2.create_or_update_secret(
    path='sql',
    secret=sql_secret,
)
