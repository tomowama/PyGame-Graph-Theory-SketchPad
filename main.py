

import time
import random
import math
import pygame
import itertools




class Edge:
    all = []
    def __init__(self, vertex1=int,vertex2=int, num = 1, bridge = False):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.num = num
        self.bridge = bridge
        self.name = f"{vertex1} {vertex2}"
        Edge.all.append(self)
    def __repr__(self):
        return f"{self.name}"
    @classmethod
    def get(cls, name):
        for inst in cls.all:
            if inst.name == name:
                return inst
    @staticmethod
    def DrawAndLabelEdge(background, color, vertex1, vertex2):
        Edge(vertex1,vertex2)
        pygame.draw.line(background, color, vertex1.pos, vertex2.pos, 4)
    @staticmethod
    def EdgeDrawer(background, color):
        Edge.BridgeGiver()
        for edge in Edge.all:
            if edge.bridge:
                color = (0,0,255)
            else:
                color = (0,255,0)
            if edge.vertex1 == edge.vertex2:
                pygame.draw.line(background,color, edge.vertex1.pos, [edge.vertex2.pos[0] + 50, edge.vertex2.pos[1] + 50], 2)
                pygame.draw.line(background, color, [edge.vertex2.pos[0] + 50, edge.vertex2.pos[1] + 50], [edge.vertex2.pos[0] + 100, edge.vertex2.pos[1]], 2)
                pygame.draw.line(background, color, [edge.vertex2.pos[0] + 100, edge.vertex2.pos[1]], [edge.vertex2.pos[0] + 50, edge.vertex2.pos[1] - 50], 2)
                pygame.draw.line(background, color, [edge.vertex2.pos[0] + 50, edge.vertex2.pos[1] - 50], edge.vertex2.pos, 2)
                if edge.num > 1:
                    pos = [edge.vertex1.pos[0] +50, edge.vertex1.pos[1]]
                    text = font.render(f'{edge.num}', True, color)
                    background.blit(text, pos)
            else:
                pygame.draw.line(background, color, edge.vertex1.pos, edge.vertex2.pos, 2)
                if edge.num > 1:
                    pos = [(edge.vertex1.pos[0] +edge.vertex2.pos[0]) / 2 , (edge.vertex1.pos[1] +edge.vertex2.pos[1]) / 2]
                    text = font.render(f'{edge.num}', True, color)
                    background.blit(text, pos)

    @staticmethod
    def BridgeGiver():
        bridges = Component.BridgeDector()
        for edge in Edge.all:
            if edge in bridges:
                edge.bridge = True
            else:
                edge.bridge = False
                
        return 0

    @staticmethod
    def EdgeCreator(v1,v2):
        
        for edge in Edge.all:
            
            if (v1.index == edge.vertex1.index) and (v2.index == edge.vertex2.index):
                
                edge.num += 1
                return 
            elif (v1.index == edge.vertex2.index) and (v2.index == edge.vertex1.index):
                
                edge.num += 1
                return
        
        
        return Edge(v1,v2)
    
    @staticmethod
    def EdgeCount():
        m = 0
        for edge in Edge.all:
            m += edge.num

        return m
    
    
        




        

        

class Vertex:
    all = []
    def __init__(self, pos=(0.0,0.0), color = (255,0,0)):
        index = len(Vertex.all)
        self.index = index
        self.pos = pos
        self.color = color
        Vertex.all.append(self)
    def connections(self, edges=Edge.all):
        connections = []
        
        for edge in edges:
            edgelist = edge.name.split()
            for string in edgelist:
                #print(f"string is {string} index is {self.index}")
                if string == str(self.index):
                    #print(f"in, string is {string}")
                    edgelist.remove(string)
                    #print(f"adding {edgelist} to our connections")
                    
                    connections.append(edgelist[0])
                    #print(f"our connections are {connections}")
                #print(modedge)
        #print(connections)
        #print(f"vertext is {self} connections are {connections} - from connections functions")
        
            
        return connections
            
            


        
        

        

    @staticmethod
    def are_directly_connected(vertex1, vertex2, edges = Edge.all):
        #print(f"the vertices we are working with are {vertex1}, {vertex2}")
        if vertex1 == None or vertex2 == None:
            return False
        if vertex1 == vertex2:
            return False
        for string in edges:
            edge = [int(x) for x in str(string).split()] 
            #print(f"we are passing in {vertex1} and {vertex2}")
            if (vertex1.index in edge) and (vertex2.index in edge):
                return True
            edge = []
        return False



    @staticmethod
    def are_connected(StartVertex, EndVertex):
        if StartVertex == None or EndVertex == None:
            return False
        
        CurrentPathOfVertices = []
        CurrentVertex = StartVertex
        Edges = Edge.all[:]
        VisitableVertices = []
        CompletedVertices = []
        EndOfLine = False
        #print(f"CHECKING IF VERTEX {StartVertex} AND {EndVertex} ARE CONNECTED")
        while not Vertex.are_directly_connected(CurrentVertex, EndVertex):
            # check if there are no more vertices to go to besides the one we have visited already
            
            #print(f"current vertex is {CurrentVertex}")
            connections = CurrentVertex.connections()[:]
            if str(CurrentVertex.index) in connections:
                connections.remove(str(CurrentVertex.index))
            
            
            for index in connections:
                if (Vertex.get(int(index)) not in CurrentPathOfVertices) and (Vertex.get(int(index)) not in CompletedVertices):
                    
                    VisitableVertices.append(Vertex.get(int(index)))
            
            #print(f"Visitable vertices are {VisitableVertices}")
            
            # check if we have no vertexs to vists and if we are at the start vertex - which means it is not possible to make the connection
            if CurrentVertex == StartVertex and VisitableVertices == []:
                return False
            #change vertex
            if CurrentVertex not in CurrentPathOfVertices:
                CurrentPathOfVertices.append(CurrentVertex)
            #print(f"Current path is {CurrentPathOfVertices}")
            
            
            if VisitableVertices == []: # we have reached the end of the line and need to move back to the last vertex and mark this vertex as completed
                #print("should be adding")
                CompletedVertices.append(CurrentVertex)
                # now we need to change the current vertex.
                del CurrentPathOfVertices[-1] # delete last element from the path since it will be a None type object
                CurrentVertex = CurrentPathOfVertices[-1]
                VisitableVertices = []
            else:
                CurrentVertex = VisitableVertices[0]
            #print(f"completed vertices are {CompletedVertices}")
            VisitableVertices = []
            
        
        return True
            




        


























    def __repr__(self):
        return f"{self.index}"
    @staticmethod
    def connected(vertices = []):
        for vertex1 in vertices:
            for vertex2 in reversed(vertices):
                if not Vertex.are_connected(vertex1, vertex2):
                    return False
        return True
    @classmethod
    def get(cls, index):
        for inst in cls.all:
            if inst.index == index:
                return inst
    @classmethod
    def get_pos(cls, pos):
        for inst in cls.all:
            if inst.pos == pos:
                return inst
    @staticmethod
    def DrawAndLabelVertex(background, color, pos, radius):
        pygame.draw.circle(background, color, pos, radius)
        Vertex(pos)

    @staticmethod
    def VertexDrawer(background, color, radius, bipartite):
        font = pygame.font.SysFont("comicsans", 25)
        for vertex in Vertex.all:
            if bipartite:
                pygame.draw.circle(background, vertex.color, vertex.pos, radius)
            else:
                pygame.draw.circle(background, color, vertex.pos, radius)
            
            text = font.render(f'{vertex.index}', True, (255, 255, 255))
            background.blit(text, [vertex.pos[0] - WINDOW_SIZE[0]/100, vertex.pos[1] - WINDOW_SIZE[1]/60])
        
    @staticmethod
    def bipartie():
        ## RECURSIVE ALGO FOR THIS
        blue = []
        red = []
        done_vertices = []
        color = 0
        
        done = False

        for vertex in Vertex.all:
            done = False
            CurrentVertex = vertex
            
            if vertex not in done_vertices:
                #print(f"current vertex is {CurrentVertex}")

                if vertex in red:
                    color = 1
                else:
                    color = 0
                while not done:
                    #print(f"current vertex is {CurrentVertex}")
                    #print(f"our connections are {CurrentVertex.connections()}")
                    for edge in CurrentVertex.connections():
                        if edge == str(CurrentVertex.index):
                            return False
                    if color % 2 == 0:
                        if CurrentVertex not in blue:
                            blue.append(CurrentVertex)
                        done_vertices.append(CurrentVertex)

                        for index in CurrentVertex.connections():
                            
                            if Vertex.get(int(index)) not in red:
                                #print(f"current vertex is {CurrentVertex} and we are adding vertex {Vertex.get(int(index))} to red")
                                red.append(Vertex.get(int(index)))
                            if Vertex.get(int(index)) not in done_vertices:
                                CurrentVertex = Vertex.get(int(index))
                    elif color % 2 == 1:
                        if CurrentVertex not in red:
                            red.append(CurrentVertex)
                        done_vertices.append(CurrentVertex)
                        for index in CurrentVertex.connections():
                            if Vertex.get(int(index)) not in blue:
                                #print(f"current vertex is {CurrentVertex} and we are adding vertex {Vertex.get(int(index))} to blue")
                                blue.append(Vertex.get(int(index)))
                            if Vertex.get(int(index)) not in done_vertices:
                                CurrentVertex = Vertex.get(int(index))
                    if CurrentVertex == done_vertices[-1]:
                        done = True
                    color +=1
                    #print(f"color is {color}")
        #print(blue)
        #print(red)
        #print(done_vertices)
        for vertex in blue:
            if vertex in red:
                return False
        for vertex in blue:
            vertex.color = (0,0,255)
        for vertex in red:
            vertex.color = (255,0,0)
        return True
    @staticmethod
    def DegreeDisplayer():
        for vertex in Vertex.all:
            degree = 0
            for edge in vertex.connections():
                #print(f"vertex is {vertex} and the connections are {vertex.connections()}")
                edgename = f"{vertex.index} {edge}"
                if Edge.get(edgename) != None:
                    degree += Edge.get(edgename).num
                else:
                    edgename = f"{edge} {vertex.index}"
                    #print(f"connection is {edge}")
                    #print(f"vertex is {vertex}")
                    #print(f" edge name is {edgename}")
                    if Edge.get(edgename) == None:
                        edgename = f"{vertex.index} {vertex.index}"
                        degree += Edge.get(edgename).num
                        break
                    degree += Edge.get(edgename).num
            text = font.render(f'{degree}', True, (255, 255, 0))
            background.blit(text, [vertex.pos[0] - 30 * WINDOW_SIZE[0]/800, vertex.pos[1] - WINDOW_SIZE[1]/300])
    
    
class Component:
    all = []
    def __init__(self, vertices=[]):
        self.vertices = vertices
        self.num = len(vertices)
        Component.all.append(self)
    def __repr__(self):
        return f"{self.vertices}"


    @staticmethod
    def ComponentMaker(Edges = Edge.all):
        Component.all = []
        for vertex in Vertex.all:
            NewComponent = Component([vertex])
            NewComponent.ComponentJoiner(Edges)
        return len(Component.all)





    
    def ComponentJoiner(self, Edges):
        ComponentsToAdjoin = []
        if len(Component.all) <= 1:
            return 0
        connections = []
        for vertex in self.vertices:
            
            connections = connections + vertex.connections(Edges)
        if '' in connections:
            connections.remove('')
        
        #print(f"component is {self} and our connections are {self.connections}")
        #print('')
        for index in connections:
            if Vertex.get(int(index)) not in self.vertices: #vertex is in anothher component, so we need to find which one it is in.
                
                LoopComponents = Component.all[:]
                LoopComponents.remove(self)

                for comp in LoopComponents:
                    
                    if Vertex.get(int(index)) in comp.vertices: # then our self and this comp are connected, so we need to join them
                        #print(f"the components {comp} and {self} are connected")
                        
                        if comp not in ComponentsToAdjoin:
                            ComponentsToAdjoin.append(comp)

        # now we need to adjoin the components
        #print(f"components to adjoin are {ComponentsToAdjoin}")
        #print('')
        NewCompVertices = self.vertices
        for comp in ComponentsToAdjoin:
            NewCompVertices = NewCompVertices + comp.vertices
            Component.all.remove(comp)
        #print(f"component is {self} and the new components vertices are {NewCompVertices}")
        #print('')
        if len(NewCompVertices) > 0:
            Component(NewCompVertices)
            Component.all.remove(self)
        #print(f"all the componenets are {Component.all}")
        #print('')
        return 0
    
    @staticmethod
    def BridgeDector():
        
        bridges = []
        Num = Component.ComponentMaker()
        
        for edge in Edge.all:
            #print(f"testing edge {edge}")
            ModifiedEdges = Edge.all[:]
            ModifiedEdges.remove(edge)
            
            #Component.ComponentMaker(ModifiedEdges)
            #print(f"our edge is {edge} and the components are {Component.all}")
            if Component.ComponentMaker(ModifiedEdges) > Num:
                bridges.append(edge)
            Component.all = []
        return bridges
        



        

        
        

def distance_point_line(pt, l1, l2):
    nx, ny = l1[1] - l2[1], l2[0] - l1[0]
    nlen = math.hypot(nx, ny)
    nx /= nlen
    ny /= nlen
    vx, vy = pt[0] - l1[0],  pt[1] - l1[1]
    dist = abs(nx*vx + ny*vy)
    return dist
        
        

def AdjacencyMatrix():
    size = len(Vertex.all)
    Matrix = [[0 for col in range(size)] for row in range(size)]
    # for i in range(size):
    #    for x in range(size):
    #""        Matrix[i][x] = 0
    
    for vertex in Vertex.all:
        for v2 in Vertex.all:
            #print(f"for vertex {vertex} we have the connections {vertex.connections()}")
            if v2 == vertex and str(vertex.index) in vertex.connections():
                print('in')
                Matrix[v2.index][v2.index] = 2
            else:
                
                if Vertex.are_directly_connected(vertex, v2):
                    #print(f"vertex is {vertex} v2 is {v2}")
                    #print(Matrix)
                    #Matrix[vertex.index][v2.index] = 1
                    
                    
                    Matrix[vertex.index][v2.index] = 1
                    #print(Matrix)
                    #Matrix[v2.index][vertex.index] = 1
                else:
                    Matrix[vertex.index][v2.index] = 0
    return Matrix


def MatrixPrinter(Matrix):
    print("Matrix is:")
    print("--------------------------")
    for row in Matrix:
        print(row)
    print("--------------------------")
    return 0


#list(itertools.permutations([1, 2, 3]))
def Hamiltonian():
    starttime = time.time()
    num = len(Vertex.all)
    Vertices = Vertex.all[:]
    Vertices.pop(0)
    total = list(itertools.permutations(Vertices))
    base=[Vertex.get(0)]
    y = int((time.time() - starttime)/10)
    for perm in total:
        TestPerm = base + list(perm)
        length = len(TestPerm)
        x = 0
        #print(f"testing perm {TestPerm}")
        for i in range(length):
            #print(f"length is {length} and i is {i}")
            if i == length-1:
                if not Vertex.are_directly_connected(TestPerm[i], TestPerm[0]):
                    #print(f"vertex {TestPerm[i]} and vertex {TestPerm[0]} are not directly connected")
                    break
            elif not Vertex.are_directly_connected(TestPerm[i], TestPerm[i+1]):
                #print(f"vertex {TestPerm[i]} and vertex {TestPerm[i+1]} are not directly connected")
                break
            x = i
            
        
        if x == length-1:
            return TestPerm
        currenttime = int(time.time() - starttime)
        if currenttime > 10 * y:
            print(f"Still processing....")
            print(f"It has been {currenttime} seconds")
            print("--------------------")
            y +=1
        





 



    return []







RADIUS = 20
ZEROINTENSITY = 0
MAXINTENSITY = 255
COLOR = (255, 0, 0)



pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600))
WINDOW_SIZE = (1000,800)
background = pygame.Surface(WINDOW_SIZE)
background.fill(pygame.Color('#000000'))
KEY = -1
ListOfVertices = []
temp_edges = []
click_num = 0
vertex_move = []
is_running = True
removed = False
degree = 0
showdegree = False
bipartite = False
button_connected = pygame.Rect(0, 0, 100, 30)
button_bipartie = pygame.Rect(0, 30, 100, 30)
button_matrix = pygame.Rect(0, 60, 100, 30)
button_hamiltonian = pygame.Rect(0, 90, 100, 30)
font = pygame.font.SysFont("comicsans", 25)

def ButtonDrawer(background, color, button, text, textcolor, fontpos, fontsize = 25):
    font = pygame.font.SysFont("comicsans", fontsize)
    pygame.draw.rect(background, color, button)
    letters = font.render(text, True, textcolor)
    background.blit(letters, fontpos)

while is_running:
    time.sleep(1/25)
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if button_connected.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                    # prints current location of mouse
                    edges = Edge.all
                    if Vertex.connected(Vertex.all):
                        print("Our Graph is connected")
                    else:
                        print("The Graph is not connected")
                        Edge.all = edges
        if button_bipartie.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                    # prints current location of mouse
                    
                    if Vertex.bipartie():
                        print("Our Graph is bipartie")
                        bipartite = True
                    else:
                        print("The Graph is not bipartie")
                        bipartite = False
        if button_matrix.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                    # prints current location of mouse
                    
                    MatrixPrinter(AdjacencyMatrix())
        if button_hamiltonian.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                    # prints current location of mouse
                    path = Hamiltonian()

                    if len(path) > 0 :
                        print(f"Our Graph is Hamiltonian, and the path is {path}")
                    else:
                        print("Our graph is not Hamiltonian")
                    
        if event.type == pygame.KEYDOWN:
            if event.unicode == 'v':
                KEY = 'v'
            elif event.unicode == 'e':
                KEY = 'e'
            elif event.unicode == 'd':
                KEY = 'd'
            elif event.unicode == 'm':
                KEY = 'm'
            elif event.unicode == 'g':
                degree += 1
                if degree % 2 == 1:
                    showdegree = True
                else:
                    showdegree = False

        if (event.type == pygame.MOUSEBUTTONDOWN) and (KEY == 'v'):
            #ListOfVertices.append(Vertex.DrawAndLabelVertex(background, COLOR, pos, RADIUS))
            bipartite = False
            Vertex(pos)
            pygame.time.wait(100)

        if (event.type == pygame.MOUSEBUTTONDOWN) and (KEY == 'e'):
            for vertex in Vertex.all:
                if (((pos[0] >= vertex.pos[0] - RADIUS) and (pos[0] <= vertex.pos[0] + RADIUS)) and ((pos[1] >= vertex.pos[1] - RADIUS) and (pos[1] <= vertex.pos[1] + RADIUS))):
                    
                    temp_edges.append(vertex)
                    
                if len(temp_edges) == 2:
                    bipartite = False

                    Edge.EdgeCreator(temp_edges[0], temp_edges[1])
                    temp_edges = []
        if (event.type == pygame.MOUSEBUTTONDOWN) and (KEY == 'd'):#delete any vertex we touch 
            #check if our mouse is inside a vertex.
            vertexremoved = False
            for vertex in Vertex.all:
                if (((pos[0] >= vertex.pos[0] - RADIUS) and (pos[0] <= vertex.pos[0] + RADIUS)) and ((pos[1] >= vertex.pos[1] - RADIUS) and (pos[1] <= vertex.pos[1] + RADIUS))):
                    Vertex.all.remove(vertex)
                    removed = True 
                    removal = []
                    vertexremoved = True
                    for edge in Edge.all:
                        if edge.vertex1 == vertex or edge.vertex2 == vertex:
                            removal.append(1)
                        else:
                            removal.append(0)
                    break
            j = 0
            if vertexremoved:
                for x in range(len(removal)):
                    if removal[-x] == 1:
                        Edge.all.pop(-(x-j))
                        j+=1
                if removed == True:
                    i = 0
                    for vertex in Vertex.all:
                        vertex.index = i
                        i +=1
                    removed = False
                
            for edge in Edge.all:
                
                if (distance_point_line(pos, [edge.vertex1.pos[0],edge.vertex1.pos[1]], [edge.vertex2.pos[0],edge.vertex2.pos[1]]) < 8):
                    Edge.all.remove(edge)

                
        if (event.type == pygame.MOUSEBUTTONDOWN) and (KEY == 'm'):#Move around vertices
            #check if our mouse is inside a vertex.
            for vertex in Vertex.all:
                if (((pos[0] >= vertex.pos[0] - RADIUS) and (pos[0] <= vertex.pos[0] + RADIUS)) and ((pos[1] >= vertex.pos[1] - RADIUS) and (pos[1] <= vertex.pos[1] + RADIUS))):
                    vertex_move.append(vertex)
                    break
                    # We are inside a vertex, so we want to delete it
            
            if (len(vertex_move) >0):
                waiting = True
                while waiting: #wait for new click of a mouse button 
                    pos = pygame.mouse.get_pos()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            is_running = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            vertex_move[0].pos = pos 
                            vertex_move=[]
                            waiting = False

    background.fill(pygame.Color('#000000'))
    

    ButtonDrawer(background, [0,255,0], button_connected, "Connected?", (0,0,0), [0,0])
    
    ButtonDrawer(background, [0,255,0], button_bipartie, "Bipartite?", (0,0,0), [0,30] )

    ButtonDrawer(background, [0,255,0], button_matrix, "Matrix", (0,0,0), [0,60] )

    ButtonDrawer(background, [0,255,0], button_hamiltonian, "Hamiltonian?", (0,0,0), [0,90], 23)


    if KEY == 'v':
        textv = font.render(f'Vertex Creation Mode', True, (255, 255, 255))
        background.blit(textv, [WINDOW_SIZE[0] -400,0])
    
    elif KEY == 'e':
        texte = font.render(f'Edge Creation Mode', True, (255, 255, 255))
        background.blit(texte, [WINDOW_SIZE[0] -400,0])
    elif KEY == 'd':
        textd = font.render(f'Vertex Deletion Mode', True, (255, 255, 255))
        background.blit(textd, [WINDOW_SIZE[0] -400,0])
    elif KEY == 'm':
        textm = font.render(f'Vertex Moving Mode', True, (255, 255, 255))
        background.blit(textm, [WINDOW_SIZE[0] -400,0])

    vertices = font.render(f'n = {len(Vertex.all)}', True, (255, 255, 255))
    background.blit(vertices, [WINDOW_SIZE[0] -300,30])

    
    edges = font.render(f'm = {Edge.EdgeCount()}', True, (255, 255, 255))
    background.blit(edges, [WINDOW_SIZE[0] -300,60])
    
    components = font.render(f'k = {Component.ComponentMaker()}', True, (255, 255, 255))
    background.blit(components, [WINDOW_SIZE[0] -300,90])

    Edge.EdgeDrawer(background, COLOR)
    Vertex.VertexDrawer(background, COLOR, RADIUS, bipartite)
    if showdegree == True:
        Vertex.DegreeDisplayer()
    window_surface.blit(background, (0, 0))
    pygame.display.update()























