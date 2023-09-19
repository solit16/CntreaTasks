package main

import "fmt"

func main() {
	numbers := []int{}
	changed := false
	for {
		var value int
		if n, _ := fmt.Scan(&value); n == 0 {
			break
		}
		numbers = append(numbers, value)
	}
	for j := 0; j < len(numbers)-1; j++ {
		for i := 0; i < len(numbers)-1; i++ {
			if numbers[i] > numbers[i+1] {
				numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
				changed = true
			}
		}
		if changed {
			fmt.Println(convertToString(numbers))
			changed = false
		}
	}
}

func convertToString(list []int) string {
	result := ""
	for i := 0; i < len(list); i++ {
		result += fmt.Sprintf("%d", list[i])
		result += " "
	}
	return result
}

func Sprintf(s string, i int) {
	panic("unimplemented")
}
