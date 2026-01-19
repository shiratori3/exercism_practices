package chessboard

// Declare a type named File which stores if a square is occupied by a piece - this will be a slice of bools
type File []bool

// Declare a type named Chessboard which contains a map of eight Files, accessed with keys from "A" to "H"
type Chessboard map[string]File

// CountInFile returns how many squares are occupied in the chessboard,
// within the given file.
func CountInFile(cb Chessboard, file string) int {
	cnt := 0
	s, exists := cb[file]
	if exists {
		for _, c := range s {
			if c {
				cnt++
			}
		}
	}
	return cnt
}

// CountInRank returns how many squares are occupied in the chessboard,
// within the given rank.
func CountInRank(cb Chessboard, rank int) int {
	cnt := 0
	if rank < 1 || rank > 8 {
		return 0
	}
	for col := 'A'; col <= 'H'; col++ {
		if cb[string(col)][rank-1] {
			cnt++
		}
	}
	return cnt
}

// CountAll should count how many squares are present in the chessboard.
func CountAll(cb Chessboard) int {
	cnt := 0
	for _, v := range cb {
		for range v {
			cnt++
		}
	}
	return cnt
}

// CountOccupied returns how many squares are occupied in the chessboard.
func CountOccupied(cb Chessboard) int {
	cnt := 0
	for _, c := range "ABCDEFGH" {
		for _, v := range cb[string(c)] {
			if v {
				cnt++
			}
		}
	}
	return cnt
}
