var express = require('express');
var multer = require('multer');
var app = express();
var bodyParser = require('body-parser');
var crypto = require('crypto');
var mime = require('mime');
var PythonShell = require('python-shell');
//var pyshell = new PythonShell('./public/parse.py');

console.log(__dirname);
app.use(express.static(__dirname + '/public'));
//app.use(express.bodyParser({uploadDir:'./uploads'}));
//app.use(bodyParser.json());
//app.use('/uploads', express.static(__dirname + 'uploads'));

var storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, './public/uploads/')
  },
  filename: function (req, file, cb) {
    crypto.pseudoRandomBytes(16, function (err, raw) {
      cb(null, raw.toString('hex') + Date.now() + '.' + mime.extension(file.mimetype));
    });
  }
});

var upload = multer({storage: storage});

//var upload = multer({ dest : 'uploads/' });

app.post('/uploads',upload.array('userPhoto',10), function(req,res){
        //console.log('single', req.body['path']);
	arr = [];
        console.log(req.files);
	for(var file of req.files){
		//console.log("obj"+ Object.keys(file));
		arr.push(file.path);
	}
	var options = {
		mode: 'text',
		args: [arr.toString()]
	};
	PythonShell.run('./public/mood.py', options, function(err,results){
		if(err) throw err;
		console.log('results', results);
	});

	console.log(arr);
        res.end("File is uploaded");
});

//app.post('/uploads', function(req, res) {
//    res.send('Photo array?: ' + req.body.userPhoto);
//});

app.listen(80, function(){
        console.log('Listening at port 80');
});

