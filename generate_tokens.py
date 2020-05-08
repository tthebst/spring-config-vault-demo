import json
import hvac

# connect to vault
client = hvac.Client(url='http://localhost:8200', token="myroot", verify=False)

# read sql policy file to string
with open("vault/policies/sql.hcl", "r") as f:
    sql_policy = f.read()

# read foo policy file to string
with open("vault/policies/foo.hcl", "r") as f:
    foo = f.read()

# read bar policy file to string
with open("vault/policies/bar.hcl", "r") as f:
    bar = f.read()

# create sql policy
client.sys.create_or_update_policy(
    name='sql-policy',
    policy=sql_policy,
)

# create foo policy
client.sys.create_or_update_policy(
    name='foo-policy',
    policy=foo,
)

# create bar policy
client.sys.create_or_update_policy(
    name='bar-policy',
    policy=bar,
)

# create tokens for each policy
sql_token = client.create_token(policies=['sql-policy'], lease='1h')
foo_token = client.create_token(policies=['foo-policy'], lease='1h')
bar_token = client.create_token(policies=['bar-policy'], lease='1h')


tokens = {}

tokens['sql_client_token'] = sql_token['auth']['client_token']
tokens['foo_client_token'] = foo_token['auth']['client_token']
tokens['bar_client_token'] = bar_token['auth']['client_token']


with open('tokens.json', 'w') as f:
    json.dump(tokens, f)
