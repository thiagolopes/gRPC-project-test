package main

import (
	"log"
	"net"

	// third-party imports
	"github.com/thiagolopes/gRPC-project-test/go-project/promotion"
	"google.golang.org/grpc"
)

type discountServer struct{}

func main() {
	log.Println("grpc_server_started")
	listen, err := net.Listen("tcp", ":5555")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	gRPCServer := grpc.NewServer()
	server := promotion.Server{}

	promotion.RegisterDiscountServiceServer(gRPCServer, &server)

	if err := gRPCServer.Serve(listen); err != nil {
		log.Fatalf("failed_to_serve: %s", err)
	}
}
