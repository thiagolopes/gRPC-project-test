package promotion

import (
	"testing"
	"time"
)

func TestIsEqual(t *testing.T) {
	Today := time.Now().UTC()
	Yesterday := time.Now().Add(-24 * time.Hour)

	if isEqual(Today, Today, "2006-01-02") != true {
		t.Errorf("isEqual, expected=%v", true)
	}

	if isEqual(Today, Yesterday, "2006-01-02") != false {
		t.Errorf("isEqual, expected=%v", false)
	}
}

func TestBlackFridayPromotion(t *testing.T) {
	tests := []struct {
		Order            Order
		ExpectedDiscount Discount
	}{
		{
			Order:            Order{User: User{Date: "invalid"}},
			ExpectedDiscount: Discount{},
		},
		{
			Order: Order{User: User{Date: "1995-11-25"}},
			ExpectedDiscount: Discount{
				Percentage:  BF_PERCENTAGE_DISCOUNT,
				Description: "Black friday day promotion",
			},
		},
		{
			Order:            Order{User: User{Date: "1995-11-22"}},
			ExpectedDiscount: Discount{},
		},
	}

	for _, test := range tests {
		discount := BlackFridayPromotion(test.Order)

		if discount != test.ExpectedDiscount {
			t.Errorf("BlackFridayPromotion, order=%v, expected=%v, returned=%v", test.Order, test.ExpectedDiscount, discount)
		}
	}
}

func TestBirthDayPromotion(t *testing.T) {
	Today := time.Now().UTC().Format("2006-01-02")
	Yesterday := time.Now().Add(-24 * time.Hour).Format("2006-01-02")

	tests := []struct {
		Order            Order
		ExpectedDiscount Discount
	}{
		{
			Order:            Order{User: User{Date: "invalid"}},
			ExpectedDiscount: Discount{},
		},
		{
			Order: Order{User: User{Date: DateISO(Today)}},
			ExpectedDiscount: Discount{
				Percentage:  BIRTH_DAY_PERCENTAGE_DISCOUNT,
				Description: "Cake day promotion",
			},
		},
		{
			Order:            Order{User: User{Date: DateISO(Yesterday)}},
			ExpectedDiscount: Discount{},
		},
	}

	for _, test := range tests {
		discount := BirthDayPromotion(test.Order)

		if discount != test.ExpectedDiscount {
			t.Errorf("BlackFridayPromotion, order=%v, expected=%v, returned=%v", test.Order, test.ExpectedDiscount, discount)
		}
	}
}
