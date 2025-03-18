class HTMLNode():
   def __init__(self, tag=None, value=None, children=None, props=None):
      self.tag = tag
      self.value = value
      self.children = children
      self.props = props
      self.attrs = [
         "tag", "value", "children", "props"
      ]
      pass
   def to_html(self):
      raise Exception("Not Implemented")
      pass
   def props_to_html(self):
      output = []
      if self.props:
         for prop in self.props:
            # print(f"{self.props}")
            # print(f"{self.props[prop]}")
            output.append(f'{prop}="{self.props[prop]}"')
         return (" ").join(output)
      return ""
   def getChildren(self):
      output = []
      for child in self.children:
         output.append(child.to_html())
      return ("").join(output)
   def hasChildren(self):
      return ( isinstance(self.children, list))

   def __eq__(self, other):
      if self.tag == other.tag and self.value == other.value and self.props == self.props:
         if (not self.hasChildren() and not other.hasChildren()):
            return True
         if (self.hasChildren() and other.hasChildren()):
            return (self.getChildren() == other.getChildren())
         return False
      else: 
         return False
      pass
   def __repr__(self):
      output = ["HTMLNode("]
      if self.tag:
         output.append(f"tag: {self.tag}")
      if self.value:
         output.append(f"value: {self.value}")
      if self.children:
         output.append(f"children: {self.children}")
      if self.props:
         output.append(f"props: {self.props}")
      output.append(")")
      string = (" ").join(output)
      return string
   pass


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        props = ""
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        if (len(self.props_to_html()) > 0):
           props = (" "+ self.props_to_html())
        return f"<{self.tag}{props}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
   def __init__(self, tag, children, props=None):
      super().__init__(tag, None, children, props)

   def to_html(self):
      if self.tag is None:
         raise ValueError("Invalid tag: no value")
      if self.children is None:
         raise ValueError("Invalid parent: no children")
      # if self.tag is None:
      #    return self.value.strip()
      return f"<{self.tag}{self.props_to_html()}>{self.getChildren()}</{self.tag}>"
      
   def __repr__(self):
      return f"LeafNode({self.tag}, {self.getChildren()}, {self.props})"
