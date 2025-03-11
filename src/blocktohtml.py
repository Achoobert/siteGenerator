from blocknode import block_to_block_type, BlockType
from conversion import text_to_textnodes, markdown_to_blocks, text_node_to_html_node
from htmlnode import ParentNode, LeafNode

def checkIfInCodeBlock(text):
   return (text[:4] == """```
""" and text[-4:] == """
```""")

def markdown_to_html_node(block):
   block_list = markdown_to_blocks(block)
   arr = []
   for b in block_list:
      parentTag = "p"
      if (checkIfInCodeBlock(b)):
         parentTag = "pre"
         b = ("```" + b[4:]) # remove first line break in code block
      txt_list = text_to_textnodes(b)
      # print(txt_list)
      leafArr = []
      for c in txt_list:
         d = text_node_to_html_node(c)
         if ( isinstance(d, LeafNode)):
            leafArr.append(
               text_node_to_html_node(c)
               )
      if (len(leafArr) > 0 ):
         arr.append(
            ParentNode(parentTag, leafArr)
         )
   return ParentNode("div", arr)
