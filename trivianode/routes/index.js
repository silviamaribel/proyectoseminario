var express = require('express');
var session=require("../session/django");
var s=session();
var router = express.Router();
/* GET home page. */
router.get('/', function(req, res) {
  res.render('index', { title: 'TriviaOnline.com' });
});
router.get('/Partidas', function(req, res) {
  res.render('Partidas', { title: 'cracion partidas' });
});
var sesiones=Array();
router.get("/errorsession/",function(req,res){
	console.log("ERROR SESSION")
	res.writeHead("302",{"Location":"http://localhost:8000/login/"});
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
			res.writeHead("302",{"Location":"http://localhost:8000/login/"});
			res.end();
		}
	});
	
});
router.get("/chat/",function(req,res){
	
	if(sesiones[req.cookies.sessionid]==undefined)
	{
		res.writeHead("302",{"Location":"http://localhost:8000/login/"});
		res.end();
		return;
	}
	res.render('chat',{title:"Chat",idsession:sesiones[req.cookies.sessionid].id,username:sesiones[req.cookies.sessionid].name});

});
router.get("/saladechat",function(req,res){
	if(sesiones[req.cookies.sessionid]==undefined)
	{
		res.writeHead("302",{"Location":"http://localhost:8000/login/"});
		res.end();
		return;
	}
	console.log(req.session);
	res.render("saladechat",{title:"Sala"});
});
router.get('/registrate/', function(req, res) {
  if(sesiones[req.cookies.sessionid]==undefined)
    {
        res.writeHead("302",{"Location":"http://localhost:8000/login/"});
        res.end();
        return;
    }
  res.render('registrate', { title: 'Express' });
});
router.post('/forpartida/',function(req,res){
    id=req.body.id;
    titulo=req.body.titulo;
    jugadores=req.body.jugadores;
    tipo_partida=req.body.tipo_partida;
    preguntas=req.body.preguntas;
    tiempo_respuesta=req.body.tiempo_respuesta;
    usuario_id=req.body.usuario_id;

   connection.query('INSERT INTO partida (id,titulo,jugadores,tipo_partida,preguntas,tiempo_respuesta,usuario_id) VALUES (?,?,?,?,?,?,?);',[id,titulo,jugadores,tipo_partida,preguntas,tiempo_respuesta,usuario_id],function(error,docs){
          if(error) res.json(error);

          res.redirct('/partida/');
    });
});

/*nombre=req.body.nombre;
		tipo_a=req.body.tipo_a;*/

module.exports = router;