package promotion

import (
	"time"
)

// ISO Layout to time.TIME
const ISO_LAYOUT = "2006-01-02"

// DateISO is the date in ISO 8601
type DateISO string

// User struct, than represent the date about User in order.
type User struct {
	Date DateISO
}

// Order struct, than represent the order cart. If in future the
// promotions need ve calculate using products in order as a
// reference, add here the new structs
type Order struct {
	User User
}

// Discount struct, than represent a Discount avalibe to be
type Discount struct {
	Percentage  float32
	Description string
}

func DateISOIsValid(date DateISO) bool {
	_, err := time.Parse(ISO_LAYOUT, string(date))

	if err != nil {
		return false
	}
	return true
}
