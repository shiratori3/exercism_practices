package thefarm

import (
	"errors"
	"fmt"
)

// TODO: define the 'DivideFood' function
func DivideFood(fc FodderCalculator, num int) (float64, error) {
	total, err := fc.FodderAmount(num)
	if err != nil {
		return 0, err
	}
	factor, err := fc.FatteningFactor()
	if err != nil {
		return 0, err
	}
	return total / float64(num) * factor, err
}

// TODO: define the 'ValidateInputAndDivideFood' function
func ValidateInputAndDivideFood(fc FodderCalculator, num int) (float64, error) {
	if num > 0 {
		return DivideFood(fc, num)
	} else {
		return 0, errors.New("invalid number of cows")
	}
}

// TODO: define the 'ValidateNumberOfCows' function
type InvalidCowsError struct {
	num     int
	message string
}

func (ice *InvalidCowsError) Error() string {
	return fmt.Sprintf("%d cows are invalid: %s", ice.num, ice.message)
}

func ValidateNumberOfCows(num int) error {
	if num > 0 {
		return nil
	} else if num == 0 {
		return &InvalidCowsError{num: num, message: "no cows don't need food"}
	} else {
		return &InvalidCowsError{num: num, message: "there are no negative cows"}
	}
}

// Your first steps could be to read through the tasks, and create
// these functions with their correct parameter lists and return types.
// The function body only needs to contain `panic("")`.
//
// This will make the tests compile, but they will fail.
// You can then implement the function logic one by one and see
// an increasing number of tests passing as you implement more
// functionality.
