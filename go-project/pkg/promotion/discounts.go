package promotion

import (
	"fmt"
	"time"
)

// TODO add in settings
const (
	BF_DAY                 = "26"
	BF_MOUTH               = "11"
	BF_TIME_PARSE          = "01-02"
	BF_PERCENTAGE_DISCOUNT = 0.10
)

type Promotions struct {
	Promotion []func(Order) Discount
}

// BlackFridayPromotion is the function that describe the discounts in
// black friday day
func BlackFridayPromotion(order Order) Discount {
	BFDate, err := time.Parse(BF_TIME_PARSE, fmt.Sprint(BF_MOUTH, "-", BF_DAY))
	if err != nil {
		fmt.Errorf("bf_date_parse_error, bf_date=%v, bf_parse=%v, error=%v", fmt.Sprint(BF_MOUTH, "-", BF_DAY), BF_TIME_PARSE, err)
		return Discount{Description: "bf_date_parse_error"}
	}

	UserDate, err := time.Parse(BF_TIME_PARSE, string(order.User.Date))
	if err != nil {
		fmt.Errorf("user_date_parse_error, user_date=%v, user_parse=%v, error=%v", order.User.Date)
		return Discount{Description: "user_date_parse_error"}
	}

	if UserDate == BFDate {
		return Discount{
			Percentage:  BF_PERCENTAGE_DISCOUNT,
			Description: "Black friday day promotion",
		}
	}

	return Discount{}
}
