FROM golang:alpine AS builder

WORKDIR /robot

ENV GOPROXY https://goproxy.cn
COPY ./golang/go.mod /robot
COPY ./golang/go.sum /robot
RUN go mod download
RUN go mod verify

COPY ./golang /robot

RUN go build -o robot

FROM alpine:latest

WORKDIR /root/
COPY --from=builder /robot/robot .
COPY --from=builder /robot/config/config.yaml ./config/

ENTRYPOINT ["./robot"]