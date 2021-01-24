package config

import (
	"log"
	"os"

	"github.com/joho/godotenv"
)

type Settings struct {
	Host string
	Port string
}

func LoadSettings(settings *Settings) {
	err := godotenv.Load()
	if err != nil {
		log.Fatalf("error_loading_dot_env_file, err=%v", err)
	}

	settings.Host = os.Getenv("HOST")
	settings.Port = os.Getenv("PORT")
}
