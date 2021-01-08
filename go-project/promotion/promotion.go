package promotion

import (
	"context"
	"log"
)

type Server struct {
	UnimplementedDiscountServiceServer
}

func (s *Server) AvailableDiscounts(ctx context.Context, order *Order) (*Discounts, error) {
	log.Println(order)
	return &Discounts{}, nil
}
