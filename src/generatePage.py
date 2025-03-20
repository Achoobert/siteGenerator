from os.path import join
from os import path, mkdir
from blocktohtml import markdown_to_html_node, extract_title

def generate_page(base_path, from_path, template_path, dest_path):
   if (not path.exists(from_path) or not path.exists(template_path) ):
      # print(source)
      raise Exception("Cannot find source!")
   print(f"Generating page from {from_path} to {dest_path} using {template_path}")
   # Read the markdown file at from_path and store the contents in a variable.
   from_markdown_file = open(join(from_path)).read() 
   # print (from_markdown_file)

   # Use your markdown_to_html_node function and .to_html() method to convert the markdown file to an HTML string.
   content = (markdown_to_html_node(from_markdown_file))

   # Use the extract_title function to grab the title of the page.
   title = extract_title(from_markdown_file)
   # print("title",title)
   # Read the template file at template_path and store the contents in a variable.
   from_html_file = open(join(template_path)).read()
   # Replace the {{ Title }} and {{ Content }} placeholders in the template with the HTML and title you generated.
   new_html_string = from_html_file.replace("{{ Title }}",title)
   new_html_string = new_html_string.replace("{{ Content }}",content.to_html())

   # replace any instances of:
   # href="/ with href="{BASEPATH}
   # src="/ with src="{BASEPATH}
   new_html_string = new_html_string.replace("""href="/""", f"href=\"{base_path}")
   new_html_string = new_html_string.replace("""src="/""", f"src=\"{base_path}")

   # Write the new full HTML page to a file at dest_path. Be sure to 
   # create any necessary directories if they don't exist.
   dest_dir = path.split(dest_path)[0]
   makeDir(dest_dir)
   open(dest_path, mode='w').write(new_html_string)
   pass

def makeDir(dir):
   basePath = path.split(path.join(dir))[0]
   # print(basePath)
   if(not path.exists( dir )):
      # recurse up a level
      makeDir(basePath)
      # print("make_path ", basePath)
      mkdir(path.join(dir))
   return