class Environment:
    def __init__(self):
        self.vars = {}

    def define(self, name, value):
        self.vars[name] = value

    def get(self, name):
        return self.vars.get(name, f"<undefined: {name}>")

def evaluate(ast, env):
    for node in ast:
        if node['type'] == 'let':
            value_node = node['value']
            if value_node['type'] == 'call':
                val = {
                    'type': value_node['name'],
                    'data': value_node['args'][0]
                }
                env.define(node['name'], val)
        elif node['type'] == 'print':
            val = env.get(node['arg'])
            print(f"[{val['type'].upper()}] {val['data']}")
