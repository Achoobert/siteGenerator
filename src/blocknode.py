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
   return ( 0 < text.rfind("#") < 6)
def detectCode(text):
   # Code blocks must start with 3 backticks and end with 3 backticks.
   tail_of_block = (text[(len(text) - 3):])
   return ( text[:3] == "```" and tail_of_block == "```")
def detectQuote(arr):
   # Every line in a quote block must start with a > character.
   # map( lambda l: l[:1] == "> " , text.split("\n"))
   # arr = text.split("\n")
   for line in arr:
      if (line[0] == ">"  and line[1] == " " ):
         continue
      else:
         return False
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
   # If none of the following conditions are met, the block is a normal paragraph
   discovered_blockType = BlockType.PARAGRAPH
   if (detectHeader(block)):
      return BlockType.HEADING
   if (detectCode(block)):
      return BlockType.CODE
   blockArr = block.split("\n")
   if (detectQuote(blockArr)):
      return BlockType.QUOTE
   if (detectList(blockArr)):
      return BlockType.UNORDERED_LIST
   if (detectOrderedList(blockArr)):
      return BlockType.ORDERED_LIST     
   return discovered_blockType
