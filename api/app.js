var express = require('express'),
    bodyParser = require('body-parser'),
    config = require('config'),
    bunyan = require('bunyan'),
    elasticsearch = require('elasticsearch'),
    uuid = require('uuid');

var app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
    extended: true
}));
var log = bunyan.createLogger({
    name: config.app_name,
    streams: [{
        level: 'info',
        path: config.logging.path + config.app_name + '-info.log'
    }, {
        level: 'error',
        path: config.logging.path + config.app_name + '-error.log'
    }]
});
var es_client = new elasticsearch.Client({
    host: config.elasticsearch.host,
    log: 'trace'
});

app.set('port', (process.env.PORT || 3000))

app.get('/', function (request, response) {
    log.info("hello /");
    response.send('Hello World!')
})

app.post('/save', function (req, res) {
    log.info(req.body);
    es_client.index({
        index: config.elasticsearch.index,
        type: config.elasticsearch.type,
        id: uuid(),
        body: req.body
    }, function (error, response) {
        log.info(response);
    });
    res.send('success!');
});

app.get('/query/:query', function (req, res) {
    log.info(req.params.query);
    es_client.search({
        q: req.params.query
    }).then(function (body) {
        var hits = body.hits.hits;
        log.info(hits);
        res.send(hits);
    }, function (error) {
        console.trace(error.message);
    });
    
});

app.listen(app.get('port'), function () {
    console.log("Node app is running at localhost:" + app.get('port'))
});