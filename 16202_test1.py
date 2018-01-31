input_string='a_b a_c a_f b_d b_e e_x'
input_str=input_string.split(' ')
print input_str

input_1=list(map(lambda x:x.split('_'),input_str))
#print input_1

child_node=[input_1[x][1] for x in range(len(input_1))]
child_node=list(set(child_node))
#print child_node
parent_node=[input_1[x][0] for x in range(len(input_1))]
parent_node=list(set(parent_node))
#print parent_node
total_node=parent_node+child_node
total_node=list(set(total_node))
#print total_node
n=len(total_node)
dict={}
for i in range(len(total_node)):
    dict[i]=total_node[i]
tree=[[0 for i in range(len(total_node))]for j in range(len(total_node))]

def search_parent_child_return_index(input1,dict1):
    for i in dict1:
        if input1==dict1[i]:
            return i

def create_tree_matrix(total_node,input_1,dict,tree):
    for j in range(len(input_1)):
        val1=search_parent_child_return_index(input_1[j][0],dict)
        val2=search_parent_child_return_index(input_1[j][1],dict)
        tree[val1][val2]=1


def immediate_children(tree,parent_node,dict):
   # parent_node=str(input('Enter parent node:='))
    val1=search_parent_child_return_index(parent_node,dict)
    children=[]
    for i in range(len(tree)):
        if (tree[val1][i])==1:
            children.append(dict[i])
    return children


def all_children(tree,parent_node,dict):
    val1=search_parent_child_return_index(parent_node,dict)
    children=[]
    for i in range(val1,len(tree[val1])):
        child=[]
        child=immediate_children(tree,dict[i],dict)
        for i in range(len(child)):
            children.append(child[i])
    return children


def check_ancestor(tree,parent,child,dict):
    val1=search_parent_child_return_index(parent,dict)
    val2=search_parent_child_return_index(child,dict)
    children_parent=all_children(tree,parent,dict)
    for i in children_parent:
        val=search_parent_child_return_index(i,dict)
        if val==val2:
            print "True"
            return
    print "False"

create_tree_matrix(total_node,input_1,dict,tree)
print tree
print "immediate children"
parent_node=str(input('enter parent node:='))
imm_children=[]
imm_children=immediate_children(tree,parent_node,dict)
print imm_children

print "\nall children"
all_child=[]
parent_node=str(input('enter parent node:='))
all_child=all_children(tree,parent_node,dict)
print all_child

print "\nancestor check"
parent=str(input('enter parent node:='))
child=str(input('enter child node:='))
check_ancestor(tree,parent,child,dict)




