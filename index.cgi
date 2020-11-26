#!/bin/bash
echo "Content-type: text/html"
echo ""
echo "<html><head><title>Bash as CGI"
echo "</title></head><body bgcolor=black>"

echo "<h1> Kubernetes Mayank Load Balancing Testing System </h1>"
echo "<h2>Your System IP:-  $(ifconfig | head -2 | grep inet | tail -c +9 | cut -d " " -f 2)</h2>"

echo "</body></html>"
