from os.path import join
from os import path
from blocktohtml import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path):
   if (not path.exists(from_path) or not path.exists(template_path) ):
      # print(source)
      raise Exception("Cannot find source!")
   print(f"Generating page from {from_path} to {dest_path} using {template_path}")
   # Read the markdown file at from_path and store the contents in a variable.
   from_markdown_file = open(join(from_path)).read() 
   # print (from_markdown_file)
   # Read the template file at template_path and store the contents in a variable.
   from_html_file = open(join(from_path)).read()

   # Use your markdown_to_html_node function and .to_html() method to convert the markdown file to an HTML string.
   content = (markdown_to_html_node(from_markdown_file))

   # Use the extract_title function to grab the title of the page.
   title = extract_title(from_markdown_file)
   # print(title,content)
   # Replace the {{ Title }} and {{ Content }} placeholders in the template with the HTML and title you generated.
   # print(from_html_file)
   # Write the new full HTML page to a file at dest_path. Be sure to create any necessary directories if they don't exist.

   pass