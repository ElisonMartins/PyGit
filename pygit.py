import os

def read_file(filename):
    """Read contents of a file and return as bytes."""
    with open(filename, 'rb') as f:
        return f.read()

def write_file(filename, data):
    """Write data to a file."""
    with open(filename, 'wb') as f:
        f.write(data)

def init(repo):
    """Create directory for repo and initialize .git directory."""
    os.mkdir(repo)
    os.mkdir(os.path.join(repo, '.git'))
    for name in ['objects', 'refs', 'refs/heads']:
        os.mkdir(os.path.join(repo, '.git', name))
    write_file(os.path.join(repo, '.git', 'HEAD'),
               b'ref: refs/heads/master')
    print('initialized empty repository: {}'.format(repo))

# Exemplo de uso:
init("meu_repositorio")
