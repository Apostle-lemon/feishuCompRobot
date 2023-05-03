package compmsg

import (
	"time"
	"xlab-feishu-robot/internal/model"
	"xlab-feishu-robot/internal/pkg"

	"github.com/sirupsen/logrus"
)

var AppToken string = "ZEzobwp5VagznYs66zqcDe6Nnac"
var TableId string = "tbls2xvl2e4HWo27"

func Init() {
	// logrus.Info("init compmsg timer")
	// c := cron.New(cron.WithSeconds())
	// // 每天 6 点执行
	// _, err := c.AddFunc("0 0 6 * * *", checkDBUpdate)
	// if err != nil {
	// 	panic(err)
	// }
	// logrus.Info("start compmsg cron timer")
	// c.Start()

	logrus.Info("compmsg DEBUG")
	debug()

}

func checkDBUpdate() {
	logrus.Info("checkDBUpdate at ", time.Now())

	var CompModelList []model.CompModel
	result := pkg.DB.Find(&CompModelList)
	if result.Error != nil {
		logrus.Error(result.Error)
		return
	}
	for _, comp := range CompModelList {
		handleCompDBItem(comp)
	}

	logrus.Info("checkDBUpdate done")
}

func handleCompDBItem(comp model.CompModel) {
	if comp.Checked == 1 {
		return
	} else {
		comp.Checked = 1
		writeFeishuFile(comp)
		pkg.DB.Save(comp)
	}
}

func writeFeishuFile(comp model.CompModel) {
	current_time := time.Now().Unix() * 1000
	name := comp.Name
	URL := comp.URL
	informationMap := map[string]any{
		"筛选日期": current_time,
		"竞赛名称": name,
		"链接":   URL,
	}
	pkg.Cli.DocumentCreateRecord(AppToken, TableId, informationMap)
}

func debug() {
	checkDBUpdate()
}
