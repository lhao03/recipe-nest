function submit_message(message) {
  $.post("/send_message", { message: message }, handle_response);

  function handle_response(data) {
    // append the bot repsonse to the div
    $(".chat-container").append(`
            <div class="chat-message col-md-5 offset-md-7 bot-message">
                ${data.message}
            </div>
      `);
    // remove the loading indicator
    $("#loading").remove();
  }
}

$("#target").on("submit", function(e) {
  e.preventDefault();
  const input_message = $("#input_message").val();
  // return if the user does not enter any text
  if (!input_message) {
    return;
  }

  $(".chat-container").append(`
        <div class="chat-message col-md-5 human-message">
            ${input_message}
        </div>
    `);

  // loading
  $(".chat-container").append(`
        <div class="chat-message text-center col-md-2 offset-md-10 bot-message" id="loading">
          <div class="spinner">
            <div class="bounce1"></div>
            <div class="bounce2"></div>
            <div class="bounce3"></div>
          </div>
        </div>
    `);

  // clear the text input
  $("#input_message").val("");

  // send the message
  submit_message(input_message);

  // Get a reference to the div you want to auto-scroll.
  var someElement = document.querySelector(".chat-container"); // Create an observer and pass it a callback.
  var observer = new MutationObserver(scrollToBottom); // Tell it to look for new children that will change the height.
  var config = { childList: true };
  observer.observe(someElement, config);

  function scrollToBottom() {
    someElement.scrollTop = someElement.scrollHeight;
  }

  // First, define a helper function.
  function animateScroll(duration) {
    var start = someElement.scrollTop;
    var end = someElement.scrollHeight;
    var change = end - start;
    var increment = 20;
    function easeInOut(currentTime, start, change, duration) {
      // by Robert Penner
      currentTime /= duration / 2;
      if (currentTime < 1) {
        return (change / 2) * currentTime * currentTime + start;
      }
      currentTime -= 1;
      return (-change / 2) * (currentTime * (currentTime - 2) - 1) + start;
    }
    function animate(elapsedTime) {
      elapsedTime += increment;
      var position = easeInOut(elapsedTime, start, change, duration);
      someElement.scrollTop = position;
      if (elapsedTime < duration) {
        setTimeout(function() {
          animate(elapsedTime);
        }, increment);
      }
    }
    animate(0);
  }
  // Here's our main callback function we passed to the observer
  function scrollToBottom() {
    var duration = 300; // Or however many milliseconds you want to scroll to last
    animateScroll(duration);
  }
});
