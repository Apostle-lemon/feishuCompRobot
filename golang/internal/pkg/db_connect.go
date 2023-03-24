package pkg

import (
	"database/sql"
	"fmt"
	"xlab-feishu-robot/internal/config"

	_ "github.com/go-sql-driver/mysql"
	"github.com/sirupsen/logrus"
)

func Connect() (*sql.DB, error) {
	host := config.C.DB.Host
	port := config.C.DB.Port
	user := config.C.DB.User
	password := config.C.DB.Password
	dbName := config.C.DB.DbName

	// 构造 MySQL 数据库连接字符串
	dataSourceName := fmt.Sprintf("%s:%s@%s:%s/%s?charset=utf8mb4", user, password, host, port, dbName)
	logrus.Info("Connecting to database...", host, port, user, password, dbName)

	// 连接 MySQL 数据库
	db, err := sql.Open("mysql", dataSourceName)
	if err != nil {
		return nil, err
	}

	// 测试连接数据库是否成功
	err = db.Ping()
	if err != nil {
		db.Close()
		return nil, err
	}

	return db, nil
}

var DB *sql.DB

func init() {
	var err error
	DB, err = Connect()
	if err != nil {
		panic(err)
	}
	defer DB.Close()
}
