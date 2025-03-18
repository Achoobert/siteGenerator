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
   # print (text, ( 0 < text.rfind("#") < 6))

   # return ( 0 < text.rfind("# "))
   return ( 0 <= text.rfind("#") <= 6)
def detectCode(text):
   # Code blocks must start with 3 backticks and end with 3 backticks.
   tail_of_block = (text[(len(text) - 3):])
   # print (tail_of_block)
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

def clean_string_starter(blockArr):
   out_string = ""
   for i in range(len(blockArr)):
      out_string += (blockArr[i][2:]) # TODO smarter 
      out_string += ("\n")
   return out_string

# Create a block_to_block_type function that takes a single block of markdown text as input 
# and returns the BlockType representing the type of block it is. 
def block_to_block_type(block):
   if (not isinstance(block, str) or len(block) == 0):
      raise Exception("not string")
   # If none of the following conditions are met, the block is a normal paragraph
   discovered_blockType = BlockType.PARAGRAPH
   if (detectHeader(block)):
      # cannot count header here
      # text = block[(2+ block[7:].rfind("#")):]
      text = block.strip("#")
      text = text.strip()
      return BlockType.HEADING, text
   if (detectCode(block)):
      text = block.strip("```")
      return BlockType.CODE, text
   blockArr = block.split("\n")
   if (not isinstance(blockArr, list) or len(blockArr) == 0):
      raise Exception("not array")
   if (detectQuote(blockArr)):
      # remove those '> '
      return BlockType.QUOTE, clean_string_starter(blockArr)
   if (detectList(blockArr)):
      return BlockType.UNORDERED_LIST, clean_string_starter(blockArr)
   if (detectOrderedList(blockArr)):
      return BlockType.ORDERED_LIST, clean_string_starter(blockArr)
   return discovered_blockType, block


def stripBlock(text):
   # temporarily remove \n characters, strip(), then restore
   newArray = text.split("\n")
   outArray = []
   currentString = ""
   lastType = BlockType.PARAGRAPH
   for i in range(len(newArray)):
      text = newArray[i].strip()
      if ( len(text) > 0):
            currentType, txt = block_to_block_type(text)
            if (len(outArray) == 0 and currentString == ""):
               lastType = currentType
               currentString = text
               continue
            if (lastType == BlockType.CODE and currentType != BlockType.CODE):
               # keep appending
               currentString += text
               currentString += "\n"
               continue
            if (lastType == currentType):
               # this is where to optionally get rid of newlines
               if (lastType == BlockType.PARAGRAPH ):
                  currentString += " "
               else:
                  if (currentType == BlockType.CODE):
                     outArray.append(currentString+text)
                     currentString = ""
                     # we've reached end of code block
                     lastType = BlockType.PARAGRAPH
                     continue
                  currentString += "\n"
            else:
               # print ((lastType , currentType))
               outArray.append(currentString)
               currentString = ""
               lastType = currentType
            currentString += text
            # outArray.append( text )
   if (len(currentString) > 0):
      outArray.append(currentString)
   # print("isaac out array: ", outArray)
   return outArray

def splitBlock(text):
   newArray = text.split("\n\n")
   outArray = []
   for i in range(len(newArray)):
      arr = stripBlock(newArray[i])
      if ( len(arr) > 0 and (len(arr[0]) > 0)):
         outArray.extend(arr)
   return outArray

def markdown_to_blocks(text):
   blocks = splitBlock(text)
   return blocks