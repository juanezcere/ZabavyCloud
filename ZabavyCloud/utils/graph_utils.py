from .uuid_utils import generate_id


class Edge:
    def __init__(self, node: Node, edge_type: EdgeType = EdgeType.TERRAIN_EDGE, weight: float = 0.0):
        self.__id: str = generate_id()
        self.set_node(node)
        self.__type: EdgeType = edge_type
        self.set_weight(weight)

    """----------- MAGICS -----------"""

    def __str__(self) -> str:
        return f"Edge: {self.__weight} ==> {self.__node.get_name()}"

    """----------- GETTERS -----------"""

    def get_id(self) -> str:
        return self.__id

    def get_node(self) -> Node:
        return self.__node

    def get_type(self) -> EdgeType:
        return self.__type

    def get_weight(self) -> float:
        return self.__weight

    """----------- SETTERS -----------"""

    def set_node(self, node: Node) -> None:
        self.__node: Node = node

    def set_weight(self, weight: float) -> None:
        self.__weight: float = weight


class Node:
    def __init__(self, name: str, position: tuple = (0, 0, 0), building: Building = None):
        self.__id: str = generate_id()
        self.set_name(name)
        self.set_position(position)
        self.set_building(building)
        self.set_terrain()

    """----------- MAGICS -----------"""

    def __str__(self) -> str:
        return f"Node: {self.__name}"

    """----------- PROPS -------------"""

    @property
    def x(self) -> float:
        return self.__position[0]

    @property
    def y(self) -> float:
        return self.__position[1]

    @property
    def z(self) -> float:
        return self.__position[2]

    """----------- GETTERS -----------"""

    def get_id(self) -> str:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_position(self) -> tuple:
        return self.__position

    def get_building(self) -> Building:
        return self.__building

    def get_terrain(self) -> Terrain:
        return self.__terrain

    """----------- SETTERS -----------"""

    def set_name(self, name: str) -> None:
        self.__name: str = name

    def set_position(self, position: tuple = (0, 0, 0)) -> None:
        self.__position: tuple = position

    def set_building(self, building: Building = None) -> None:
        self.__building: Building = building

    def set_terrain(self, terrain: Terrain = Terrain()) -> None:
        self.__terrain: Terrain = terrain


class Graph:
    def __init__(self):
        self.__graph: dict = {}

    """----------- MAGICS -----------"""

    def __str__(self) -> str:
        text: str = ''
        for origin in self.__graph:
            text += f"Node '{origin.get_name()}'\n"
            for edge in self.__graph[origin]:
                text += f"{origin.get_name()} ==> {edge.get_node().get_name()} ({edge.get_type().value}).\n"
        return f'Graph:\n{text}' if len(text) else 'Graph: Empty.'

    """----------- PROPS -----------"""

    @property
    def graph(self) -> dict:
        return self.__graph

    """----------- FUNCTIONS -----------"""

    def add_node(self, node: Node) -> None:
        if node in self.__graph:
            raise Exception(
                f"The node '{node.get_name()}' is already in the graph.")
        self.__graph[node]: list = []

    def add_edge(self, origin: Node, edge: Edge) -> None:
        if origin not in self.__graph:
            raise Exception(
                f"The node '{origin.get_name()}' isn't inside the graph.")
        if edge in self.__graph[origin]:
            return
        self.__graph[origin].append(edge)

    def get_node(self, name: str) -> Node:
        nodes = list(filter(lambda node: name ==
                     node.get_name(), self.__graph))
        if not len(nodes):
            raise Exception(f"The node '{name}' was not found.")
        return nodes[0]

    def get_neighbours(self, node: Node) -> list:
        if node not in self.__graph:
            raise Exception(
                f"The node '{origin.get_name()}' isn't inside the graph.")
        return self.__graph[node]
