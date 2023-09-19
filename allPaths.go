package main

import (
	"fmt"
	"io"
	"os"
	"os/exec"
)

var checkProgram func()

type Vertex int

type matrixType map[Vertex]map[Vertex]struct{}
type vertexPair struct{ from, to Vertex }

type Graph struct {
	matrix        matrixType
	pathCountMemo map[vertexPair]int
}

func NewGraph() Graph {
	return Graph{
		matrix:        matrixType{},
		pathCountMemo: map[vertexPair]int{},
	}
}

func (g *Graph) AddEdge(a, b Vertex) {
	if neighbors, ok := g.matrix[a]; ok {
		neighbors[b] = struct{}{}
	} else {
		g.matrix[a] = map[Vertex]struct{}{
			b: struct{}{},
		}
	}

	g.pathCountMemo = map[vertexPair]int{}
}

func (g Graph) PathCount(start, end Vertex) (result int) {
	if start == end {
		return 1
	}

	vp := vertexPair{from: start, to: end}
	answer, ok := g.pathCountMemo[vp]
	if ok {
		return answer
	}

	for _, v := range g.Neighbors(start) {
		result += g.PathCount(v, end)
	}

	g.pathCountMemo[vp] = result

	return
}

func (g Graph) Neighbors(a Vertex) (result []Vertex) {
	for vertex := range g.matrix[a] {
		result = append(result, vertex)
	}

	return
}

func main() {
	if checkProgram == nil {
		checkerSource, err := io.ReadAll(os.Stdin)

		if err != nil {
			fmt.Println("Couldn't read checker source")
			return
		}

		err = os.WriteFile("checker.go", checkerSource, 0666)

		if err != nil {
			fmt.Println("Couldn't save checker source")
			return
		}

		out, err := exec.
			Command("go", "build", "-o", "combined", "program.go", "checker.go").
			CombinedOutput()

		if err != nil {
			fmt.Printf("Couldn't compile program:\n%v\n", string(out))
			return
		}

		out, err = exec.
			Command("./combined").
			CombinedOutput()

		if err != nil {
			fmt.Printf("Program exited unexpectedly:\n%v\n", string(out))
			return
		}

		fmt.Print(string(out))
	} else {
		checkProgram()
	}
}

func isIn(array []Vertex, number Vertex) bool {
	for _, el := range array {
		if el == number {
			return true
		}
	}
	return false
}

func (g Graph) maxVertex(start Vertex, path []Vertex) (Vertex, bool) {
	neighbors_good := []Vertex{}
	for _, v := range g.Neighbors(start) {
		if !(isIn(path, v)) {
			neighbors_good = append(neighbors_good, v)
		}
	}
	for _, v := range neighbors_good {
		if len(g.Neighbors(v)) == 0 {
			return v, true
		}
		path = append(path, v)
		start = v
		return g.maxVertex(start, path)
	}
	return 0, false
}

func getCopy(l []Vertex) (res []Vertex) {
	for _, i := range l {
		res = append(res, i)
	}
	return
}

func (g Graph) AllPaths(start Vertex, current_path []Vertex) (paths [][]Vertex) {
	if (start == Vertex(1)) {
		paths = append(paths, current_path)
		return
	}

	neighbors := g.Neighbors(start)

	if (len(neighbors) == 0) {
		return
	}

	for i := range neighbors {
		paths = append(paths, g.AllPaths(neighbors[i], append(getCopy(current_path), neighbors[i]))...)
	}
	return paths

}

func (g Graph) Solve() [][]Vertex {
	return g.AllPaths(Vertex(0), []Vertex{0})
}
