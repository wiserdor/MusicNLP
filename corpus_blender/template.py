import json


def save_template(template_name, template_skeleton):
    with open('templates/' + template_name + '.json', 'wb') as fp:
        fp.write(json.dumps(template_skeleton).encode("utf-8"))


rap1 = {'name': 'rap1', 'structure': ['chorus', 'verse', 'hook', 'chorus', 'verse', 'chorus']}
rap2 = {'name': 'rap2', 'structure': ['verse', 'chorus', 'hook', 'verse', 'chorus']}
rock1 = {'name': 'rock1', 'structure': ['verse', 'chorus', 'verse', 'chorus', 'chorus']}

save_template('rap1', rap1)
save_template('rap2', rap2)
save_template('rock1', rock1)
