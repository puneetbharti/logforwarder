var config = {};
config.app_name = "logApi";
config.logging = {};
config.logging.path = "/tmp/"
config.elasticsearch = {};
config.elasticsearch.host = "";
config.elasticsearch.index = "forwarderlogs";
config.elasticsearch.type = "log";


module.exports = config;