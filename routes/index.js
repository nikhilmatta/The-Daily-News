var express = require('express');
var router = express.Router();

/* GET about page. */
router.get('/about', function(req, res, next) {
    res.render('about', { title: 'The Daily News' });
});

/* GET contact page. */
router.get('/contact', function(req, res, next) {
    res.render('contact', { title: 'The Daily News' });
});

/* GET home page. */
router.get('/home', function(req, res) {
    var db = req.db;
    var collection = db.get('articlesData');
    collection.find({}, {}, function(e, docs) {
        res.render('home', {
            "home": docs
        });
    });
});

router.get('/india', function(req, res) {
    var db = req.db;
    var collection = db.get('articlesData');
    collection.find({}, {}, function(e, docs) {
        res.render('india', {
            "home": docs
        });
    });
});

router.get('/entertainment', function(req, res) {
    var db = req.db;
    var collection = db.get('articlesData');
    collection.find({}, {}, function(e, docs) {
        res.render('entertainment', {
            "home": docs
        });
    });
});

router.get('/technology', function(req, res) {
    var db = req.db;
    var collection = db.get('articlesData');
    collection.find({}, {}, function(e, docs) {
        res.render('technology', {
            "home": docs
        });
    });
});

router.get('/business', function(req, res) {
    var db = req.db;
    var collection = db.get('articlesData');
    collection.find({}, {}, function(e, docs) {
        res.render('business', {
            "home": docs
        });
    });
});

router.get('/sports', function(req, res) {
    var db = req.db;
    var collection = db.get('articlesData');
    collection.find({}, {}, function(e, docs) {
        res.render('sports', {
            "home": docs
        });
    });
});

router.get('/world', function(req, res) {
    var db = req.db;
    var collection = db.get('articlesData');
    collection.find({}, {}, function(e, docs) {
        res.render('world', {
            "home": docs
        });
    });
});

module.exports = router;