package promotion

import "github.com/thiagolopes/gRPC-project-test/go-project/pkg/promotion"

func Order2Order(o *Order) promotion.Order {
	return promotion.Order{
		User: promotion.User{promotion.DateISO(o.User.DateBirth)},
	}
}

func Discount2Discounts(ds []promotion.Discount) *Discounts {
	pds := make([]*Discount, len(ds))
	for i, d := range ds {
		pds[i] = &Discount{
			Percentage:   d.Percentage,
			DiscountName: d.Description,
		}
	}
	return &Discounts{Discounts: pds}
}
