var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res) {
  res.render('index', { title: 'Express' });
});
router.get("/partidas/",function(req,res){
	res.render('crerpartida',{title:"Express"});

});
router.get("/chat/",function(req,res){
	res.render('chat',{title:"Express"});

});
module.exports = router;



var sesiones=Array();
router.get("/errorsession/",function(req,res){
	console.log("ERROR SESSION")
	res.writeHead("302",{"Location":"http://localhost:8000/blog/login/"});
	res.end();
});
router.get("/django/:id?",function(req,res){
	s.getSession(req.params.id,function(s){
		if(s.estado=="conectado")
		{
			req.params.username=s.name;
			sesiones[req.cookies.sessionid]={id:req.params.id,name:s.name};
			console.log(sesiones);
			res.render('index', { title: 'Express',sessionid:req.params.id});
		}else{
			res.writeHead("302",{"Location":"http://localhost:8000/blog/login/"});
			res.end();
		}
	});
	
});
router.get("/chat/",function(req,res){
	
	if(sesiones[req.cookies.sessionid]==undefined)
	{
		res.writeHead("302",{"Location":"http://localhost:8000/blog/login/"});
		res.end();
		return;
	}
	res.render('chat',{title:"Chat",idsession:sesiones[req.cookies.sessionid].id,username:sesiones[req.cookies.sessionid].name});

});
router.get("/sala",function(req,res){
	if(sesiones[req.cookies.sessionid]==undefined)
	{
		res.writeHead("302",{"Location":"http://localhost:8000/blog/login/"});
		res.end();
		return;
	}
	console.log(req.session);
	res.render("sala",{title:"Sala"});
});
router.get('/registrate/', function(req, res) {
  if(sesiones[req.cookies.sessionid]==undefined)
	{
		res.writeHead("302",{"Location":"http://localhost:8000/blog/login/"});
		res.end();
		return;
	}
  res.render('registrate', { title: 'Express' });
});
module.exports = router;
