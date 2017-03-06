from graphviz import Digraph

dot = Digraph(comment='The Round Table')

dot  #doctest: +ELLIPSIS
dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')

dot.edge('B', 'L')
dot.edge('A', 'B')
print(str(dot.source)) 
archi=open('datos.txt','w')
archi.close()
archi=open('datos.txt','a')
archi.write(str(dot.source))

archi.close()

