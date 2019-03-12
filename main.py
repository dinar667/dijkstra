# coding: utf-8
#

from dijkstra import (
    inf, DijkstraAlgorythm, print_readable_dijkstra_results, read_graph
)


def main():
    graph = {
        '0': {
            '1': 2,
            '2': 5,
            '3': 4,
            '4': 12
        },
        '1': {
            '2': 1,
            '6': 11
        },
        '2': {
            '7': 13
        },
        '3': {
            '2': 3,
            '4': 1
        },
        '4': {
            '5': 6,
            '7': 9
        },
        '5': {
            '7': 7
        },
        '6': {
            '7': 8
        },
        '7': {}
    }
    parents = {'1': '0', '2': '0', '3': '0', '4': '0'}
    costs = {'1': 2, '2': 5, '3': 4, '4': 12, '5': inf, '6': inf, '7': inf}

    # graph, parents, costs = read_graph()

    d = DijkstraAlgorythm(
        graph=graph,
        parents=parents,
        costs=costs
    )
    d.find_lower_paths()

    print_readable_dijkstra_results(d)


if __name__ == "__main__":
    main()
