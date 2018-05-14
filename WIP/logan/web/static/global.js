// Dollar sign means jquery
// Once webpage (document) is ready, run function
$(document).ready(function(){

  // Make this function asynchronous so that the later await work
  // Asynchronous - many things going on at once
  // All javascript is asynchronous, but we have to explicitly declare it here
  // for the await to work.
  $('#prediction').click(async function(){

    // This would normally never work
    // New thing in JS, in the last year, that lets you make an asynchronous call
    // SYNCHRONOUS!
    // So we use await!
    const response = await $.ajax('/score', {
      method: 'post',
      contentType: 'application/json'
    });

    console.log('response', response)

    $('#output').val(response.name);

  });

});
