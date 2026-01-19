package gross

// Units stores the Gross Store unit measurements.
func Units() map[string]int {
	m := map[string]int{
		"quarter_of_a_dozen": 3,
		"half_of_a_dozen":    6,
		"dozen":              12,
		"small_gross":        120,
		"gross":              144,
		"great_gross":        1728,
	}
	return m
}

// NewBill creates a new bill.
func NewBill() map[string]int {
	return make(map[string]int)
}

// AddItem adds an item to customer bill.
func AddItem(bill, units map[string]int, item, unit string) bool {
	v, exist := units[unit]
	if !exist {
		return false
	} else {
		bill[item] += v
		return true
	}
}

// RemoveItem removes an item from customer bill.
func RemoveItem(bill, units map[string]int, item, unit string) bool {
	v_unit, exist1 := units[unit]
	if !exist1 {
		return false
	} else {
		v_bill, exist2 := bill[item]
		if !exist2 {
			return false
		} else if v_bill < v_unit {
			return false
		} else if v_bill == v_unit {
			delete(bill, item)
			return true
		} else {
			bill[item] -= v_unit
			return true
		}
	}
}

// GetItem returns the quantity of an item that the customer has in his/her bill.
func GetItem(bill map[string]int, item string) (int, bool) {
	v, exist := bill[item]
	if exist {
		return v, true
	} else {
		return 0, false
	}
}
