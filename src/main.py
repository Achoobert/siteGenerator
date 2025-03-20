from sys import argv
from copyDir import moveDirectory, generateFromDirectory

content = "./content"
static = "./static"
out_dir = "./docs"

class main():   
    base_path = "/"
    if (len(argv) > 1):
        print( "first argument: ", argv[1])
        base_path = argv[1]
        print("changing the base path to: ", base_path)
    moveDirectory(static, out_dir)
    generateFromDirectory(base_path, content, out_dir)