package promotion

import (
	"context"
	"log"

	"github.com/thiagolopes/gRPC-project-test/go-project/pkg/promotion"
)

type Server struct {
	UnimplementedDiscountServiceServer
}

func (s *Server) AvailableDiscounts(ctx context.Context, order *Order) (*Discounts, error) {
	log.Printf("available_discounts_handler_start, order=%v, ctx=%v", order, ctx)
	discounts := availableDiscountsHandler(order)
	log.Printf("available_discounts_handler_end, discounts=%v", discounts)
	return discounts, nil
}

func availableDiscountsHandler(o *Order) *Discounts {
	p := promotion.AllPromotionsAvalibe()
	d := promotion.VerifyDiscountsAvalibe(Order2Order(o), p)
	return Discount2Discounts(d)
}
