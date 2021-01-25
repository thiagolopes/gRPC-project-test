package promotion

import "testing"

func TestIsValidDateISO(t *testing.T) {
	dates := []struct{
		dateISO DateISO
		expectedValidation bool
	}{
		{"2010-10-10", true},
		{"2010-13-1", false},
		{"200000000", false},
		{"10-10-2010", false},

	}

	for _, date := range dates {
		valid := IsValid(date.dateISO)

		if valid != date.expectedValidation {
			t.Errorf("IsValid of %v is=%v, expected=%v", date.dateISO, valid, date.expectedValidation)
		}
	}
}
