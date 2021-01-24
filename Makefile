proto-path = ./protos
python-proto-output = ./python-project/shopping-api/apps/stubs
go-proto-output = ./go-project/internal

generate-promotion:
	protoc -I=$(proto-path) \
	       --python_out=$(python-proto-output) \
	       --go_out=$(go-proto-output) \
               --go-grpc_out=$(go-proto-output) \
	       --descriptor_set_out=$(proto-path)/promotion.protoset \
               $(proto-path)/promotion.proto

	python -m grpc_tools.protoc -I=$(proto-path) \
				    --grpc_python_out=$(python-proto-output) \
				    $(proto-path)/promotion.proto
