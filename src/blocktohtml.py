from blocknode import block_to_block_type, BlockType
from conversion import text_node_to_html_node, split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes, markdown_to_blocks


def markdown_to_html_node(block):
   block_list = markdown_to_blocks(block)
   arr = []
   for b in block_list:
      arr.append(
         text_to_textnodes(b)
         )
   print(arr)
   pass


# Create a new function called def markdown_to_html_node(markdown): that converts a full markdown document into a single parent HTMLNode. That one parent HTMLNode should (obviously) contain many child HTMLNode objects representing the nested elements.

# FYI: I created an additional 8 helper functions to keep my code neat and easy to understand, because there's a lot of logic necessary for markdown_to_html_node. I don't want to give you my exact functions because I want you to do this from scratch. However, I'll give you the basic order of operations:

# Split the markdown into blocks (you already have a function for this)
# Loop over each block:
# Determine the type of block (you already have a function for this)
# Based on the type of block, create a new HTMLNode with the proper data
# Assign the proper child HTMLNode objects to the block node. I created a shared text_to_children(text) function that works for all block types. It takes a string of text and returns a list of HTMLNodes that represent the inline markdown using previously created functions (think TextNode -> HTMLNode).
# The "code" block is a bit of a special case: it should not do any inline markdown parsing of its children. I didn't use my text_to_children function for this block type, I manually made a TextNode and used text_node_to_html_node.
# Make all the block nodes children under a single parent HTML node (which should just be a div) and return it.
# Create unit tests. Here are two to get you started: