from conversion import text_to_textnodes, text_node_to_html_node
from htmlnode import ParentNode, LeafNode
from blocknode import block_to_block_type, BlockType, markdown_to_blocks
from textnode import TextType, TextNode

def get_tag(input_type, input):
   match input_type:
      case BlockType.PARAGRAPH:
         return "p"
      case BlockType.HEADING:
         # Headings start with 1-6 # characters,
         # print("isaac make header: ", 1+(input[:6]).rfind("#"), input[:6])
         return f"h{1+(input[:6]).rfind("#")}"
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
   # print("isaac markdownblocklist: ", block_list)
   arr = []
   last_block_type = BlockType.PARAGRAPH
   for current_block in block_list:
      if (len(current_block)==0 or not isinstance(current_block, str)):
         continue
      found_block_type, outBlock = block_to_block_type(current_block)
      # print ("get blockType", current_block, found_block_type)
      # print(outBlock)
      txt_list = text_to_textnodes(current_block)
      create_parent = tag_parent("p")
      match found_block_type:
         case BlockType.PARAGRAPH:
            create_parent = tag_parent("p")
         case BlockType.HEADING:
            # Headings start with 1-6 # characters,
            txt_list = text_to_textnodes(outBlock)
            create_parent = tag_parent(get_tag(found_block_type, current_block))
         case BlockType.CODE:
            textB = TextNode( outBlock, TextType.CODE )
            codeB = text_node_to_html_node(textB)
            # create_parent_pre = tag_parent("pre")
            arr.append(
               ParentNode("pre", [codeB])
            )
            continue
         case BlockType.QUOTE:
            create_parent = tag_parent("blockquote")
         case BlockType.UNORDERED_LIST:
            create_parent = tag_parent("ul")
            # leafArr = parse_list(txt_list)
            if (len(leafArr) > 0 ):
               arr.append(
                  create_parent(leafArr)
               )
            continue
         case BlockType.ORDERED_LIST:
            create_parent = tag_parent("ol")
            # leafArr = parse_list(txt_list)
            if (len(leafArr) > 0 ):
               arr.append(
                  create_parent(leafArr)
               )
            continue
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
      html_node = text_node_to_html_node(text_node)
      if ( isinstance(html_node, LeafNode)):
         leafArr.append(html_node)
   return leafArr

def tag_parent(parentTag):
   def create(leafArr):
      return ParentNode(parentTag, leafArr)
   return create

def detectHeaderOne(text):
   return ( 0 <= text.rfind("#") < 1)
def extract_title(markdown):
   baseNode = markdown.split("\n")
   for node in baseNode:
      if (detectHeaderOne(node)):
         cleanText = (node[1:]).strip()
         return (cleanText)
   raise Exception("No header one")
