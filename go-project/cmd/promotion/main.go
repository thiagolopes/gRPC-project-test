package main

import (
	"fmt"
	"log"
	"net"

	"github.com/thiagolopes/gRPC-project-test/go-project/internal/promotion"
	"github.com/thiagolopes/gRPC-project-test/go-project/pkg/config"

	// third-party imports
	"google.golang.org/grpc"
)

func main() {
	settings := config.Settings{}
	config.LoadSettings(&settings)

	listen, err := net.Listen("tcp", fmt.Sprint(":", settings.Port))
	if err != nil {
		log.Fatalf("failed_to_listen_port: port=%v, err=%v", settings.Port, err)
	}

	log.Printf("grpc_server_started: host=%v, port=%v", settings.Host, settings.Port)

	gRPCServer := grpc.NewServer()
	server := promotion.Server{}

	promotion.RegisterDiscountServiceServer(gRPCServer, &server)

	if err := gRPCServer.Serve(listen); err != nil {
		log.Fatalf("grpc_server_failed_to_serve: %s", err)
	}
}
