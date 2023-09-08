$(function () {
	/* home */
	$('ul.work a.home').on('click', () => {
	const elem = $('<div></div>');
	elem.html('<p> Am flying blind</p>');
	$("body").append(elem);
	console.log('Here we go');
	});

	/* Running */
	function done () {
        	const ele = $('<div></div>');
        	ele.html(`
			<div class="card" style="width: 18rem;">
  			  <img src="https://upload.wikimedia.org/wikipedia/en/9/90/ConTest_Logo.PNG" class="card-img-top" alt="...">
  			  <div class="card-body">
    			    <h5 class="card-title">object.name</h5>
    			    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
    			    <a href="#" class="btn btn-primary">Go somewhere</a>
  			  </div>
			</div>
			`);
        	$("div.body_run").append(ele);

		/* upcoming */
        	const el = $('<div></div>');
        	el.html(`
			<div class="card" style="width: 18rem;">
                	  <img src="https://upload.wikimedia.org/wikipedia/en/9/90/ConTest_Logo.PNG" cl>
                	  <div class="card-body">
                	    <h5 class="card-title">object</h5>
                	      <p class="card-text">Some quick example text to build on the card title and>
                	      <a href="#" class="btn btn-primary">Go somewhere</a>
                	  </div>
                	</div>
			`);
        	$("div.body_up").append(el);
	}
	done()
	/* resourses */
});

