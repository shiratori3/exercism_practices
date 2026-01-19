package lasagna

// TODO: define the 'PreparationTime()' function
func PreparationTime(s []string, time int) int {
	if time <= 0 {
		return len(s) * 2
	}
	return len(s) * time
}

// TODO: define the 'Quantities()' function
func Quantities(s []string) (int, float64) {
	noodles := 0
	sauce := 0.0
	for _, v := range s {
		if v == "noodles" {
			noodles += 50
		} else if v == "sauce" {
			sauce += 0.2
		}
	}
	return noodles, sauce
}

// TODO: define the 'AddSecretIngredient()' function
func AddSecretIngredient(s1 []string, s2 []string) {
	s2[len(s2)-1] = s1[len(s1)-1]
}

// TODO: define the 'ScaleRecipe()' function
func ScaleRecipe(s []float64, n int) []float64 {
	res := []float64{}
	for _, v := range s {
		res = append(res, v/2*float64(n))
	}
	return res
}

// Your first steps could be to read through the tasks, and create
// these functions with their correct parameter lists and return types.
// The function body only needs to contain `panic("")`.
//
// This will make the tests compile, but they will fail.
// You can then implement the function logic one by one and see
// an increasing number of tests passing as you implement more
// functionality.
