package promotion

import (
	"fmt"
	"log"
	"time"
)

func isEqual(t1, t2 time.Time, parse string) bool {
	if t1.Format(parse) == t2.Format(parse) {
		return true
	}
	return false
}

func DateISOIsValid(date DateISO) bool {
	_, err := time.Parse(ISO_LAYOUT, string(date))
	if err != nil {
		return false
	}

	return true
}

// BlackFridayPromotion is the function that describe the discounts in
// black friday day
func BlackFridayPromotion(order Order) Discount {
	BFDate, err := time.Parse(BF_TIME_PARSE, fmt.Sprint(BF_MONTH, "-", BF_DAY))
	if err != nil {
		log.Printf("bf_date_parse_error, bf_date=%v, bf_parse=%v, error=%v", fmt.Sprint(BF_MONTH, "-", BF_DAY), BF_TIME_PARSE, err)
		return Discount{}
	}

	UserDate, err := time.Parse(USER_TIME_PARSE, string(order.User.Date))
	if err != nil {
		log.Printf("bf_user_date_parse_error, order=%v, user_parse=%v, error=%v", order, BF_TIME_PARSE, err)
		return Discount{}
	}

	if isEqual(UserDate, BFDate, BF_TIME_PARSE) == true {
		return Discount{
			Percentage:  BF_PERCENTAGE_DISCOUNT,
			Description: "Black friday day promotion",
		}
	}

	return Discount{}
}

// BirthDayPromotion is the function that describe the discount in user b-day
func BirthDayPromotion(order Order) Discount {
	UserDate, err := time.Parse(USER_TIME_PARSE, string(order.User.Date))
	if err != nil {
		log.Printf("cake_day_user_date_parse_error, order=%v, user_parse=%v, error=%v", order, USER_TIME_PARSE, err)
		return Discount{}
	}

	Today := time.Now().UTC()

	if isEqual(UserDate, Today, BF_TIME_PARSE) == true {
		return Discount{
			Percentage:  BIRTH_DAY_PERCENTAGE_DISCOUNT,
			Description: "Cake day promotion",
		}
	}

	return Discount{}
}

// AllPromotionsAvalibe will handle all Promotionary functions and aggregate
// all in one struct.
func AllPromotionsAvalibe() []Promotionary {
	return []Promotionary{
		BlackFridayPromotion,
		BirthDayPromotion,
	}
}

// VerifyDiscountsAvalibe will apply all promotionarys in the order,
// and return all discounts applicable
func VerifyDiscountsAvalibe(order Order, promotions []Promotionary) []Discount {
	discounts := []Discount{}
	dateUser := order.User.Date

	if valid := DateISOIsValid(dateUser); valid == false {
		log.Printf("date_iso_is_not_valid, order:%v", order)
		return discounts
	}

	for _, promotion := range promotions {
		discount := promotion(order)
		if discount != (Discount{}) {
			discounts = append(discounts, discount)
		}
	}

	return discounts
}
