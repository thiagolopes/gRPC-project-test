GOCMD=go
GOMOD=$(GOCMD) mod
GOBUILD=$(GOCMD) build
BINARY_DIR=bin
BIN_NAME=promotion

run:
	$(GOCMD) run cmd/promotion/main.go

build: deps
	mkdir -p $(BINARY_DIR)
	$(GOBUILD) -mod vendor -a -o $(BINARY_DIR)/$(BIN_NAME) ./cmd/promotion

deps:
	$(GOMOD) tidy
	$(GOMOD) vendor
