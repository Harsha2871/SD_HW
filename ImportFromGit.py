from git import Repo
import os
import stat

def rmtree(top):
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            os.chmod(filename, stat.S_IWUSR)
            os.remove(filename)
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(top)



def retrieve_codes(repo):
    Repo.clone_from(repo,'Gitfiles')
    py_paths=[]
    go_paths=[]
    js_paths=[]
    ruby_paths=[]
    for root, dirs, files in os.walk(r'Gitfiles'):
        for file in files:
            if file.endswith('.py'):
                py_paths.append(os.path.join(root, file))
            if file.endswith('.go'):
                go_paths.append(os.path.join(root, file))
            if file.endswith('.js'):
                js_paths.append(os.path.join(root, file))
            if file.endswith('.rb'):
                ruby_paths.append(os.path.join(root, file))
    py_codes=[]
    py_programs=[]
    for i in range(len(py_paths)):
        with open(py_paths[i]) as f:
            try:
                contents = f.read()
                py_programs.append(py_paths[i].split('\\')[-1])
                py_codes.append(contents)
            except:
                pass
    go_codes = []
    go_programs=[]
    for i in range(len(go_paths)):
        with open(go_paths[i]) as f:
            try:
                contents = f.read()
                go_programs.append(go_paths[i].split('\\')[-1])
                go_codes.append(contents)
            except:
                pass
    js_codes = []
    js_programs=[]
    for i in range(len(js_paths)):
        with open(js_paths[i]) as f:
            try:
                contents = f.read()
                js_programs.append(js_paths[i].split('\\')[-1])
                js_codes.append(contents)
            except:
                pass
    ruby_codes = []
    ruby_programs=[]
    for i in range(len(ruby_paths)):
        with open(ruby_paths[i]) as f:
            try:
                contents = f.read()
                ruby_programs.append(ruby_paths[i].split('\\')[-1])
                ruby_codes.append(contents)
            except:
                pass
    rmtree('Gitfiles')
    return py_codes,go_codes,js_codes,ruby_codes,py_programs,go_programs,js_programs,ruby_programs




