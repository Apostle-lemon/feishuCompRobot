package config

import (
	"github.com/YasyaKarasu/feishuapi"
	"github.com/sirupsen/logrus"
	"github.com/spf13/viper"
)

type Config struct {
	Feishu feishuapi.Config
	Server struct {
		Port int
	}
	DB struct {
		Host     string
		Port     string
		User     string
		Password string
		DbName   string
	}
}

var C Config

func ReadConfig() {
	viper.SetConfigName("lemonconfig")
	viper.AddConfigPath("./config/")

	if err := viper.ReadInConfig(); err != nil {
		logrus.Panic(err)
	}

	if err := viper.Unmarshal(&C); err != nil {
		logrus.Error("Failed to unmarshal config")
	}

	logrus.Info("Configuration file loaded")
}

func SetupFeishuApiClient(cli *feishuapi.AppClient) {
	cli.Conf = C.Feishu
}
