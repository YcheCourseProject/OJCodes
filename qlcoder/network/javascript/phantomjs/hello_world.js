var webPage = require('webpage');
var page = webPage.create();

page.open('http://www.google.com/', function(status) {
  console.log('Status: ' + status);
  // Do other things here...
});
