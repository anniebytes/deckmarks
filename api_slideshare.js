import fetch from 'node-fetch';
import crypto from 'crypto';

const API_KEY = process.env['API_KEY'];
const SHARED_SECRET = process.env['SHARED_SECRET'];
const USERNAME = process.env['USERNAME'];
const PASSWORD = process.env['PASSWORD'];

const timestamp = Math.round((new Date().getTime())/1000);
const hash = crypto.createHash('sha1')
                    .update(SHARED_SECRET + timestamp)
                    .digest('hex');
const url = "https://www.slideshare.net/api/2/get_slideshows_by_tag";
const tag = "technology";
const url_string = `${url}?tag=${tag}&limit=1&api_key=${API_KEY}&hash=${hash}&ts=${timestamp}`;

console.log(url_string);

// TODO: look into async/await solution
let result;
fetch(url_string)
    .then(response => response.text())
    .then(data => {
        result = data;
        console.log("fetch successful!")
        console.log(result);    
    })