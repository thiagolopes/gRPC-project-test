package promotion

import (
	"io/ioutil"
	"log"
	"os"
	"testing"
	"time"
)

func TestMain(m *testing.M) {
	log.SetOutput(ioutil.Discard)
	os.Exit(m.Run())
}

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

func TestAllPromotionsAvalibe(t *testing.T) {
	ExpectedLenPromotions := 2

	promotions := AllPromotionsAvalibe()
	if len(promotions) != ExpectedLenPromotions {
		t.Errorf("AllPromotions, len=%v, expected_len=%v", len(promotions), ExpectedLenPromotions)
	}
}

func TestDateISOIsValid(t *testing.T) {
	dates := []struct {
		dateISO            DateISO
		expectedValidation bool
	}{
		{"2010-10-10", true},
		{"2010-13-1", false},
		{"200000000", false},
		{"10-10-2010", false},
	}

	for _, date := range dates {
		valid := DateISOIsValid(date.dateISO)

		if valid != date.expectedValidation {
			t.Errorf("IsValid of %v is=%v, expected=%v", date.dateISO, valid, date.expectedValidation)
		}
	}
}

func TestVerifyDiscountsAvalibeToOrder(t *testing.T) {
	fake_promotions := []Promotionary{
		func(o Order) (d Discount) {
			return Discount{Percentage: 50.0, Description: "promotion one"}
		},
		func(o Order) (d Discount) {
			return Discount{Percentage: 0.1, Description: "promotion two"}
		},
		func(o Order) (d Discount) {
			return Discount{}
		},
	}
	fake_order := Order{User: User{Date: "2000-12-23"}}
	expected_discounts := []Discount{
		{Percentage: 50.0, Description: "promotion one"},
		{Percentage: 0.1, Description: "promotion two"},
	}

	discounts := VerifyDiscountsAvalibeToOrder(fake_order, fake_promotions)

	for i, discount := range discounts {
		if expected_discounts[i] != discount {
			t.Errorf("VerifyDiscountsAvalibeToOrder is=%v, expected=%v", discount, expected_discounts[i])
		}
	}
}
