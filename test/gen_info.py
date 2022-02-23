import os
import yaml

dir_path = 'D:\Workspaces\IdeaProjects\Java Itheima Course\lesson4'
files = os.listdir(dir_path)

dirs = []
for file in files:
    filepath = os.path.join(dir_path, file)
    isdir = os.path.isdir(filepath)
    if isdir:
        print(file)
        dirs.append(file)

content = {"content": dirs}

with open(os.path.join(dir_path, "lesson-info.yaml"), "w") as f:
    yaml.dump(content, f)