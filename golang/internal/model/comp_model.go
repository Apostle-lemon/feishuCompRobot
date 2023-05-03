package model

import "time"

type CompModel struct {
	Name       string    `gorm:"type:varchar(100);not null"`
	URL        string    `gorm:"type:varchar(200);not null;unique;primaryKey"`
	StartTime  time.Time `gorm:"type:datetime"`
	EndTime    time.Time `gorm:"type:datetime"`
	Location   string    `gorm:"type:varchar(100)"`
	Organizer  string    `gorm:"type:varchar(100)"`
	CreateTime time.Time `gorm:"type:timestamp;not null;default:CURRENT_TIMESTAMP"`
	Checked    int       `gorm:"type:int;not null;default:0"`
}

func (CompModel) TableName() string {
	return "comp"
}
