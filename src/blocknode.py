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
   return ( 0 <= text.rfind("#") <= 6)
def detectCode(text):
   # Code blocks must start with 3 backticks and end with 3 backticks.
   tail_of_block = (text[(len(text) - 3):])
   return (( text[:3] == "```" and tail_of_block == "```") or (text[:4] == """```
""" and text[-4:] == """
```"""))
def detectQuote(arr):
   # Every line in a quote block must start with a > character.
   expected_prefix = "> "
   for line in arr:
      if not line.startswith(expected_prefix):
         return False
   return True
def detectList(arr):
   for i in range(len(arr)):
      expected_prefix = f"- "
      if not arr[i].startswith(expected_prefix):
         return False
   return True
def detectOrderedList(arr):
   for i in range(len(arr)):
      expected_prefix = f"{i+1}. "
      if not arr[i].startswith(expected_prefix):
         return False
   return True

def clean_string(input):
   return input[2:].strip()

def clean_string_starter(blockArr):
   outArr = []
   for i in range(len(blockArr)):
      txt = blockArr[i][2:].strip()
      if (len(txt) > 0):
         outArr.append(blockArr[i][2:])
   return "\n".join(outArr)

def cleanList(inputText):
   newArray = inputText.split("\n")
   return (list(map( clean_string, newArray)))

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
      text = block.lstrip("#")
      text = text.strip()
      return BlockType.HEADING, text
   if (detectCode(block)):
      text = block.strip("```")
      return BlockType.CODE, text
   # cleaned = block.strip("\n")
   blockArr = block.split("\n")
   if (not isinstance(blockArr, list) or len(blockArr) == 0):
      raise Exception("not array")
   if (detectQuote(blockArr)):
      # remove those '> '
      return BlockType.QUOTE, clean_string_starter(blockArr)
   if (detectList(blockArr)):
      return BlockType.UNORDERED_LIST, clean_string_starter(blockArr)
   if (detectOrderedList(blockArr)):
      text = clean_string_starter(blockArr)
      return BlockType.ORDERED_LIST, text
   return discovered_blockType, block


def stripBlock(inputText):
   # temporarily remove \n characters, strip(), then restore
   if ( not isinstance(inputText, str)):
      raise Exception("stripBlock: Not a string")
   if ( len(inputText) == 0):
      raise Exception("stripBlock: no text in string")
   outerType, txt = block_to_block_type(inputText)
   newArray = inputText.split("\n")
   outArray = []
   currentString = ""
   lastType = BlockType.PARAGRAPH
   if (outerType == BlockType.ORDERED_LIST or outerType == BlockType.UNORDERED_LIST):
      return ([inputText])

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
               outArray.append(currentString)
               currentString = ""
               lastType = currentType
            currentString += text
            # outArray.append( text )
   if (len(currentString) > 0):
      outArray.append(currentString)
   return outArray

def splitBlock(text):
   newArray = text.split("\n\n")
   outArray = []
   for i in range(len(newArray)):
      if (len(newArray[i]) <= 0):
         # skip empty lines
         continue
      arr = stripBlock(newArray[i])
      if ( len(arr) > 0 and (len(arr[0]) > 0)):
         outArray.extend(arr)
   return outArray

def markdown_to_blocks(text):
   blocks = splitBlock(text)
   return blocks