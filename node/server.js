var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require("ip");

const { memoryUsage } = require("process");

var server = http.createServer(function(req, res){
    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
            res.writeHead(200, {"Content-Type":"text/html"});
            res.end(body);
        })
    }
    else if(req.url.match("/sysinfo")){
        myHostName=os.hostname()
        myTotalMem=os.totalmem()
        myUptime=os.uptime()
        myFreeMem=os.freemem()
        myCPUs=os.cpus()
        html=`
        <!DOCTYPE html>
        <html>
            <head>
                <title>System Information</title>
            </head>
        <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: ${myUptime}</p>
            <p>Total Memory: ${myTotalMem} MB</p>
            <p>Free Memory: ${myFreeMem} MB</p>
            <p>Number of CPUs: ${myCPUs.length}</p>
        </body>
        </html>
        `
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html)
    }
    else {
        res.writeHead(404, {"Content-Type": "text/html"});
        res.end(`404 File Not Found at ${req.url}`);
    }
    //res.writeHead(200, {"Content-Type": "text/html"});
    //res.end();
})

server.listen(3000);

console.log("Server listening on port 3000");