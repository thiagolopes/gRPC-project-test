GOCMD=go
GOMOD=$(GOCMD) mod
GOGET=$(GOCMD) get
GOTEST=$(GOCMD) test
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

tools:
	$(GOGET) github.com/golang/protobuf/protoc-gen-go
	$(GOGET) golang.org/x/tools/cmd/goimports
	$(GOGET) github.com/kisielk/errcheck
	$(GOGET) golang.org/x/lint/golint
	$(GOGET) github.com/golang/protobuf

errors:
	errcheck -ignoretests -blank ./...

lint:
	golint ./...

imports:
	goimports -l -w .

fmt:
	go fmt ./...

test:
	$(GOTEST) -v ./...

all: imports fmt lint errors build
