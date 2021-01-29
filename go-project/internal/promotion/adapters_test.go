package promotion

import (
	"testing"

	"github.com/thiagolopes/gRPC-project-test/go-project/pkg/promotion"
)

func TestOrder2Order(t *testing.T) {
	d := "2000-12-20"
	u := User{DateBirth: d}
	order := Order{User: &u}
	expected_order := promotion.Order{User: promotion.User{promotion.DateISO(d)}}

	o := Order2Order(&order)

	if o != expected_order {
		t.Errorf("Order2Order is=%v, expected=%v", o, expected_order)
	}
}

func TestDiscount2Discounts(t *testing.T) {
	ds := []promotion.Discount{
		{
			Percentage:  0.1,
			Description: "promotion one",
		},
		{
			Percentage:  0.04,
			Description: "promotion two",
		},
	}
	expected_len := 2

	d2d := Discount2Discounts(ds)

	if len(d2d.Discounts) != expected_len {
		t.Errorf("Discount2Discounts len is=%v, expected=%v", len(d2d.Discounts), expected_len)
	}
}
