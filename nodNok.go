package main

import (
	"fmt"
	"math/big"
)

func main() {
	numbers := make([]*big.Int, 0)
	for {
		var value big.Int
		n, _ := fmt.Scan(&value)
		if n == 0 {
			break
		}
		numbers = append(numbers, &value)
	}
	if len(numbers) == 0 {
		fmt.Println(0, 1)
		return
	}
	// nod
	local_res := big.NewInt(0)
	for i := 0; i < len(numbers); i++ {
		local_res = nod(numbers[i], local_res)
	}

	//nok
	local_res_for_nok := big.NewInt(1)
	for i := 0; i < len(numbers); i++ {
		local_res_for_nok = nok(numbers[i], local_res_for_nok)
	}
	fmt.Println(local_res, local_res_for_nok)
}

func nod(a *big.Int, b *big.Int) *big.Int {
	return big.NewInt(1).Abs(big.NewInt(0).GCD(nil, nil, a, b))
}

func nok(a *big.Int, b *big.Int) *big.Int {
	if (a.Cmp(big.NewInt(0)) == 0) || (b.Cmp(big.NewInt(0)) == 0) {
		return big.NewInt(0)
	}

	// res := big.NewInt(0)
	return big.NewInt(1).Abs(big.NewInt(1).Div(big.NewInt(1).Mul(a, b), nod(a, b)))
}
