package promotion

import (
	"fmt"
	"log"
	"time"
)

const (
	BF_DAY                        = "25"
	BF_MOUTH                      = "11"
	BF_TIME_PARSE                 = "01-02"
	BF_PERCENTAGE_DISCOUNT        = 0.10
	BIRTH_DAY_PERCENTAGE_DISCOUNT = 0.05
	USER_TIME_PARSE               = "2006-01-02"
)

type Promotionary func(Order) Discount

type Promotions struct {
	Promotion []Promotionary
}

func isEqual(t1, t2 time.Time, parse string) bool {
	if t1.Format(parse) == t2.Format(parse) {
		return true
	}
	return false
}

// BlackFridayPromotion is the function that describe the discounts in
// black friday day
func BlackFridayPromotion(order Order) Discount {
	BFDate, err := time.Parse(BF_TIME_PARSE, fmt.Sprint(BF_MOUTH, "-", BF_DAY))
	if err != nil {
		log.Printf("bf_date_parse_error, bf_date=%v, bf_parse=%v, error=%v", fmt.Sprint(BF_MOUTH, "-", BF_DAY), BF_TIME_PARSE, err)
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

	if isEqual(UserDate, Today, BF_TIME_PARSE) {
		return Discount{
			Percentage:  BIRTH_DAY_PERCENTAGE_DISCOUNT,
			Description: "Cake day promotion",
		}
	}

	return Discount{}
}

// AllPromotions will handle all Promotionary functions and aggregate
// all in one struct.
func AllPromotions() Promotions{
	return Promotions{
		Promotion: []Promotionary{
			BlackFridayPromotion,
			BirthDayPromotion,
		},
	}
}

func VerifyDiscountsAvalibyToOrder(order Order) []Discount {
	discounts := []Discount{}
	promotions := AllPromotions().Promotion
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
