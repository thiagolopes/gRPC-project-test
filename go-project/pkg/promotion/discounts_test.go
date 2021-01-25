package promotion

import "testing"

func TestBlackFridayPromotion(t *testing.T){
	tests := []struct {
		Order Order
		ExpectedDiscount Discount
	}{
		{
			Order: Order{User: User{Date: "invalid"}},
			ExpectedDiscount: Discount{Description: "user_date_parse_error"},
		},
		{
			Order: Order{User: User{Date: "1995-11-26"}},
			ExpectedDiscount: Discount{
				Percentage:  BF_PERCENTAGE_DISCOUNT,
				Description: "Black friday day promotion",
			},
		},
		{
			Order: Order{User: User{Date: "1995-11-24"}},
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
