#!/usr/bin/node

const request = require('request');
const server = require('http');
const fs = require('fs');

url = "https://kontests.net/api/v1/all";



request(url, (error, response, body) => {
	if (error) {
		console.log("An error happened");
	}
	console.log(response.statusCode);
	const myArray = JSON.parse(body);
	myArray.forEach((obj) => {
		console.log(obj);});
});

