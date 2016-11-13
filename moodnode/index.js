var express = require('express');
var multer = require('multer');
var app = express();
var bodyParser = require('body-parser');

console.log(__dirname);
app.use(express.static(__dirname + '/public'));
app.use(bodyParser.json());

var upload = multer({ dest : 'uploads/' });


app.post('/uploads',upload.array('userPhoto',10), function(req,res){
        console.log(req.body);
        console.log(req.files);
        res.end("File is uploaded");
});

//app.post('/uploads', function(req, res) {
//    res.send('Photo array?: ' + req.body.userPhoto);
//});

app.listen(8000, function(){
        console.log('Listening at port 8000');
});

