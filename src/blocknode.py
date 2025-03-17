from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

# We need a way to inspect a block of markdown text and determine what type of block it is.
def detectHeader(text):
   # Headings start with 1-6 # characters, followed by a space and then the heading text.
   print (text, ( 0 < text.rfind("#") < 6))
   return ( 0 <= text.rfind("#") < 6)
def detectCode(text):
   # Code blocks must start with 3 backticks and end with 3 backticks.
   tail_of_block = (text[(len(text) - 3):])
   return (( text[:3] == "```" and tail_of_block == "```") or (text[:4] == """```
""" and text[-4:] == """
```"""))
def detectQuote(arr):
   # Every line in a quote block must start with a > character.
   for line in arr:
      if (isinstance(line, str) and len(line) > 0 and line[0] == """>"""  and line[1] == " " ):
         continue
      else:
         return False
   # print("found quote", arr)
   return True
def detectList(arr):
   # Every line in an unordered list block must start with a - character, followed by a space.
   for line in arr:
      if (line[0] == "-" and line[1] == " " ):  
         continue
      else:
         return False
   return True
def detectOrderedList(arr):
   # Every line in an ordered list block must start with a number followed by a . character and a space. The number must start at 1 and increment by 1 for each line.
   for i in range(len(arr)):
      checkNum = i+1
      if (arr[i][0] == f"{checkNum}" and arr[i][1] == "." ):
         continue
      else:
         return False
   return True

# Create a block_to_block_type function that takes a single block of markdown text as input 
# and returns the BlockType representing the type of block it is. 
def block_to_block_type(block):
   if (not isinstance(block, str) or len(block) == 0):
      raise Exception("not string")
   # If none of the following conditions are met, the block is a normal paragraph
   discovered_blockType = BlockType.PARAGRAPH
   if (detectHeader(block)):
      print( block.rfind("#") )
      return BlockType.HEADING, block
   if (detectCode(block)):
      return BlockType.CODE, ("```" + block[4:])
   blockArr = block.split("\n")
   if (not isinstance(blockArr, list) or len(blockArr) == 0):
      raise Exception("not array")
   if (detectQuote(blockArr)):
      # remove those '> '
      out_string = ""
      for i in range(len(blockArr)):
         out_string += (blockArr[i][2:]) # TODO smarter 
         out_string += ("\n")
      return BlockType.QUOTE, out_string
   if (detectList(blockArr)):
      return BlockType.UNORDERED_LIST, block
   if (detectOrderedList(blockArr)):
      return BlockType.ORDERED_LIST, block
   return discovered_blockType, block
