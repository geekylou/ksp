class SaveFileNode():	
	def __init__(self,parent):
		self.parent = parent
		self.child_elements = []
		self.attributes     = []
		self.parent         = parent
		self.type           = ""

class SaveFileParser():
	save_file   = open("E:\ksp-win-0-90-0\KSP_win\saves\default\persistent.sfs", 'r')
	
	def __add_attribute(self,node,line):
		stripped_line = line.lstrip().rstrip()
				
		if stripped_line != "":
			#print module_path,'"'+stripped_line+'"'
			node.attributes.append(stripped_line)
			
	def __init__(self):	
		old_line = ""
		node = SaveFileNode(None)
		self.parent_node = node
		module_path = []
		
		for line in self.save_file.readlines():
			if line.find('{') >= 0:
				module_path.append(old_line.lstrip().rstrip())
				
				new_node      = SaveFileNode(node)
				new_node.type = old_line.rstrip().lstrip()
				node.child_elements.append(new_node)
				node = new_node
				line     = ""
			else:
				self.__add_attribute(node,old_line)
				if line.find('}') >= 0:
					module_path = module_path[:-1]
					node = node.parent
					line = ""
			old_line = line.lstrip().rstrip()
	
	def node_to_files(self,node):
		for element in node.child_elements:
			for attribute in element.attributes:
				args = attribute.split('=')
				if args[0].strip() == "name":
					file = open(args[1].lstrip(),"w")
					self.write_node(file,element,"")
	def write_node(self,file,node,indent):
		file.write(indent+node.type+"\n")
		file.write(indent+"{\n")
		for attribute in node.attributes:
			file.write(indent+"\t"+attribute+"\n")
		for element in node.child_elements:
			self.write_node(file,element,indent+"\t")
		file.write(indent+"}\n")
save_file = SaveFileParser()
print save_file.parent_node.child_elements[0].child_elements[6].attributes
save_file.node_to_files(save_file.parent_node.child_elements[0].child_elements[5])