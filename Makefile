proto-dir = ./protos
python-proto-output = ./python-project/shopping-api/apps/protos
go-proto-output = ./go-project

generate-proto:
	protoc -I=$(proto-dir) --python_out=$(python-proto-output) --go_out=$(go-proto-output) $(proto-dir)/promotion.proto
