from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
	TG_BOT_TOKEN= "1669723279:AAGqPjyUFt6-4JbwTyvTzs1fHEBr4hKX62M"
	APP_ID = 2410874
	API_HASH = "fbb8ea76cb2817d67f74347ff7969a6a"
	OWNER_ID = "" #ID of bot owner
	AUTH_CHANNEL = [-10082786282972]
	DESTINATION_FOLDER = "Torrent" #Name of your folder read readme
	RCLONE_CONFIG = """type = drive\nscope = drive\ntoken = {"access_token":"ya29.a0AfH6SMArIWkBlSI4GTfq3Nx3I42avnFdu6YZu7dpCygoHOtyMQI9Y-spbjDVFpVQV8StyOQLAdbOt-qkMmcbP6REUrkz3N8_sDM4_53PkL29HNkBLyuH3f8XDeVr4OoRkeFLLGC_Ql5jJK6PB8yisIixkx3_","token_type":"Bearer","refresh_token":"1//09YjDSVvL9QNUCgYIARAAGAkSNwF-L9IrR3krGWqdPFE4bFN2tYmQosFh9o_QjEJ3kxhK_5BY5oQAhnbqRWZoJyMytIPR1vmpUAY","expiry":"2021-03-13T12:46:43.725293309Z"}"""
	#fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
