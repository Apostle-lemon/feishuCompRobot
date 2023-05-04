package pkg

import (
	"fmt"
	"time"
	"xlab-feishu-robot/internal/config"

	"github.com/sirupsen/logrus"
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

func Connect() (*gorm.DB, error) {
	host := config.C.DB.Host
	port := config.C.DB.Port
	user := config.C.DB.User
	password := config.C.DB.Password
	dbName := config.C.DB.DbName

	dsn := fmt.Sprintf("%s:%s@tcp(%s:%s)/%s?charset=utf8&parseTime=true", user, password, host, port, dbName)

	logrus.Info("wait 120 seconds for database to start...")
	time.Sleep(120 * time.Second)
	logrus.Info("Connecting to database...", dsn)

	gromdb, err := gorm.Open(mysql.Open(dsn), &gorm.Config{})
	if err != nil {
		return nil, err
	}

	logrus.Info("Database connected")

	return gromdb, nil
}

var DB *gorm.DB

func InitDB() {
	var err error
	DB, err = Connect()
	if err != nil {
		panic(err)
	}
}
