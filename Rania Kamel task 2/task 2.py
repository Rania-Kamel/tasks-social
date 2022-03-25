#!/usr/bin/env python
# coding: utf-8

# In[2]:


import networkx as nx
G=nx.Graph()
G.add_node('a')


# In[ ]:





# In[ ]:





# In[6]:


nodes=['b' , 'c' , 'd']

G.add_nodes_from(nodes)


# In[7]:


G.add_edge('a', 'b')


# In[8]:


edges = [('a', 'c'), ('b', 'c'), ('c', 'd')]


# In[9]:


G.add_edges_from(edges)


# In[33]:


nx.draw(G, with_labels=True,
       node_color='red',
        node_size=1200,
        font_color='blue',
        font_size=20,
        edge_color='Yellow',
        
       )


# In[34]:


G.nodes


# In[37]:


for n in G.nodes:
    print(x)


# In[39]:


G.number_of_nodes()


# In[41]:


G.edges


# In[43]:


for e in G.edges:
    print(e)


# In[44]:


G.number_of_edges()


# In[45]:


G.neighbors('b')


# In[46]:


for ne in G.neighbors('b'):
    print(ne)


# In[48]:


list(G.neighbors('b'))


# In[49]:


nx.is_tree(G)


# In[50]:


nx.is_connected(G)


# In[51]:


G.has_node('a')


# In[52]:


G.has_node('x')


# In[53]:


'd' in G.nodes


# In[54]:


G.has_edge('a' , 'b')


# In[55]:


G.has_edge('a' , 'd')


# In[57]:


('c' , 'd') in G.edges


# In[58]:


len(list(G.neighbors('a')))


# In[59]:


G.degree('a')


# In[63]:


items = ['rania', 'z', 'mariam']
[item.upper() for item in items]


# In[ ]:





# In[64]:


print(G.nodes())
print([G.degree(n) for n in G.nodes()])


# In[ ]:





# In[65]:


g = (len(item) for item in items)
list(g)


# In[66]:


max(len(item) for item in items)


# In[67]:


sorted(item.upper() for item in items)


# In[2]:


G = nx.Graph()

G.add_nodes_from(['cat','dog','virus',13])

G.add_edge('cat','dog')

nx.draw(G, with_labels=True, font_color='black', node_size=1400 , node_color="red")


# In[ ]:





# In[3]:


print(open('E:/fci/Social/FirstCourseNetworkScience/datasets/friends.adjlist').read())


# In[ ]:





# In[6]:


SG = nx.read_adjlist('E:/fci/Social/FirstCourseNetworkScience/datasets/friends.adjlist')


# In[ ]:





# In[ ]:





# In[21]:


nx.draw(SG, node_size=2000, node_color='lightblue', with_labels=True)


# In[11]:


SG.degree('Claire')


# In[80]:


D= nx.DiGraph()


# In[84]:


D.add_edges_from([(1,2),(2,3),(3,2),(3,4),(3,5),(4,5),(4,6),(5,6),(6,4),(4,2)])


# In[ ]:





# In[89]:


nx.draw(D, 
        with_labels=True,
        node_color='red',
        node_size=1200,
        font_color='blue',
        font_size=20,
        edge_color='Yellow',)


# In[90]:


D.has_edge(1,2)


# In[91]:


D.has_edge(2,1)


# In[92]:


print('Successors of 2:', list(D.successors(2)))


# In[93]:


print('Predecessors of 2:', list(D.predecessors(2)))


# In[94]:


D.in_degree(2)


# In[95]:


D.out_degree(2)


# In[96]:


D.degree(2)


# In[97]:


print('Successors of 2:', list(D.successors(2)))


# In[100]:


print('"Neighbors" of 2:', list(D.neighbors(2)))


# In[5]:


G = nx.Graph()
G.add_edges_from([
        ('a', 'b'),
        ('a', 'd'),
        ('c', 'd'),
    ])
nodes = G.nodes()
leavies = []
for node in nodes:
    if len(G.edges(node)) == 1:
        leavies.append(node)
leavies


# In[11]:


degrees = SG.degree()
maxScore = 0
maxNode= ""
for (node ,val) in degrees:
    if val > maxScore:
        maxScore = val
        maxNode = node
print("name: " , maxNode , " , degree of: ", maxScore)


# In[14]:


mutal = []
def mutal_friends(node1,node2):
    node1Edges = SG.edges(node1)
    node2Edges = SG.edges(node2)
    for (node , val) in node1Edges:
        for (node2 , val2) in node2Edges:
            if val == val2:
                mutal.append(val)
mutal_friends('Claire', 'George')
mutal


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




