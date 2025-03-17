from conversion import text_to_textnodes, markdown_to_blocks, text_node_to_html_node
from htmlnode import ParentNode, LeafNode
from blocknode import block_to_block_type, BlockType


def checkIfInCodeBlock(text):
   return (text[:4] == """```
""" and text[-4:] == """
```""")

def get_tag(input_type, input):
   match input_type:
      case BlockType.PARAGRAPH:
         return "p"
      case BlockType.HEADING:
         # Headings start with 1-6 # characters,
         print(input[6:])
         return "h"
      case BlockType.CODE:
         return "pre"
      case BlockType.QUOTE:
         return "blockquote"
      case BlockType.UNORDERED_LIST:
         return "ul"
      case BlockType.ORDERED_LIST:
         return "ol"
      case default:
         raise Exception ("unsupported block type")

def markdown_to_html_node(block):
   if (not isinstance(block, str)):
      raise Exception("cannot process this type")
   block_list = markdown_to_blocks(block)
   arr = []
   for current_block in block_list:
      if (len(current_block)==0 or not isinstance(current_block, str)):
         continue
      # get blockType
      current_block_type, outBlock = block_to_block_type(current_block)
      # print(outBlock)
      txt_list = text_to_textnodes(current_block)
      create_parent = tag_parent("p")
      match current_block_type:
         case BlockType.PARAGRAPH:
            create_parent = tag_parent("p")
         case BlockType.HEADING:
            # Headings start with 1-6 # characters,
            print(input[6:])
            create_parent = tag_parent("h")
         case BlockType.CODE:
            create_parent = tag_parent("pre")
         case BlockType.QUOTE:
            create_parent = tag_parent("blockquote")
         case BlockType.UNORDERED_LIST:
            create_parent = tag_list_parent("ul")
            leafArr = parse_list(txt_list)
            if (len(leafArr) > 0 ):
               arr.append(
                  create_parent(leafArr)
               )
            break
         case BlockType.ORDERED_LIST:
            create_parent = tag_list_parent("ol")
            leafArr = parse_list(txt_list)
            if (len(leafArr) > 0 ):
               arr.append(
                  create_parent(leafArr)
               )
            break
         case default:
            raise Exception ("unsupported block type")

      # print (current_block)
      leafArr = parse_leaves(txt_list)
      if (len(leafArr) > 0 ):
         arr.append(
            create_parent(leafArr)
         )
   return ParentNode("div", arr)

def parse_leaves(txt_list):
   leafArr = []
   for text_node in txt_list:
      # print (text_node)
      html_node = text_node_to_html_node(text_node)
      if ( isinstance(html_node, LeafNode)):
         leafArr.append(html_node)
   return leafArr

def parse_list(txt_list):
   leafArr = []
   for text_node in txt_list:
      # print (text_node)
      html_node = text_node_to_html_node(text_node)
      if ( isinstance(html_node, LeafNode)):
         leafArr.append(ParentNode("li", [html_node]))
   return leafArr

def tag_parent(parentTag):
   def create(leafArr):
      return ParentNode(parentTag, leafArr)
   return create
def tag_list_parent(parentTag):
   def create(leafArr):
      # print (leafArr)
      return ParentNode(parentTag, [ParentNode("li", leafArr)])
   return create

def detectHeaderOne(text):
   # H1s start with 1 # characters, followed by a space and then the heading text.
   # print (text, ( 0 <= text.strip().rfind("#") < 1))
   return ( 0 <= text.rfind("#") < 1)
def extract_title(markdown):
   baseNode = markdown.split("\n")
   for node in baseNode:
      if (detectHeaderOne(node)):
         cleanText = (node[1:]).strip()
         return (cleanText)
   raise Exception("No header one")
