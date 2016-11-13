var express = require('express');
var multer = require('multer');
var app = express();
var storage = multer.diskStorage({
        destionation: function(req,file,callback){
                callback(null,'./uploads');
        },
        filename: function(req,file,callback){
                callback(null, file.fieldname + '-' + Date.now());
        }
});
var upload = multer({storage:storage}).single('userPhoto');

app.get('/',function(req,res) {
        res.send(__dirname + "/index.html");
});

app.post('/api/photo',function(req,res){
    upload(req,res,function(err) {
        if(err) {
            return res.end("Error uploading file.");
        }
        res.end("File is uploaded");
    });
});

app.listen(8888,function(){
	console.log("runnning moodnode on port 8888");
});
