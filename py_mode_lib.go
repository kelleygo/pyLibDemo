package main

import "C"

//export Add
func Add(a, b int) int {
	return a + b
}

func main() {
	// 空的 main 函数，仅用于满足 Go 编译器要求
}
