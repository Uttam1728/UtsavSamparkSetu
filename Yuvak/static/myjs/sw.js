self.addEventListener("install", e => {
    console.log("from SW-2.js")
    e.waitUntil(
        caches.open("static").then(cache => {
            return cache.addAll(["/admin","/static/img/utsav.png","/static/img/swaminarayan.png","/static/img/gunatitanandswami.png","/static/img/bhagataji_maharaj.png","/static/img/Shastriji_Maharaj.png","/static/img/yogiji_maharaj.png","/static/img/psm.png","/static/img/msm.png"]);
            })
        );
});
//console.log("hi from sw2")