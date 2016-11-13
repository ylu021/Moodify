var express = require('express');
var multer = require('multer');
var app = express();

console.log(__dirname);
app.use(express.static(__dirname + '/public'));

app.listen(8000, function(){
        console.log('Listening at port 8000');
});

