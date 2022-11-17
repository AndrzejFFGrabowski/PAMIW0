function set_output(text) {
  output = document.getElementById("output")

  if (!output) {
    output = document.createElement("span")
    output.setAttribute("id", "output")
    document.body.appendChild(output)
  }

  output.innerText = text
}

function clear_output() {
    set_output("")
}

async function update(response) {
  code = await response.status
  text = await response.text()
  set_output("Current job finished in " + text + "%")

  return (code == 200) ? text : "ERR"
}

async function check_with_ajax_polling() {
  await fetch("/check?mode=ajax")
        .then((response) => update(response));
}


window.addEventListener("load", function() {
  start = document.getElementById("start")
  if (start) {
    start.addEventListener("submit", function(event) {
      event.preventDefault()
      fetch(start.action, {method:"post"})
      .then((response) => response.text())
      .then((text) => console.info(text))
    })
  }

  reset = document.getElementById("reset")
  if (reset) {
    reset.addEventListener("submit", function(event) {
      event.preventDefault()
      fetch(reset.action, {method:"post"})
      .then((response) => response.text())
      .then((text) => console.info(text))
    })
  }

  ajax_polling = document.getElementById("ajax-polling")
  if (ajax_polling) {
    console.info("Ajax polling active");
    ajax_polling.addEventListener("click", function(event) {
      event.preventDefault()
      clear_output()

      if (window.tid) {
        console.info("Stopped interval timer")
        window.clearInterval(window.tid)
        window.tid = undefined
        ajax_polling.innerText = "start"
      } else {
        console.info("Started interval timer")
        window.tid = window.setInterval(check_with_ajax_polling, 500)
        ajax_polling.innerText = "stop"
      }
    })
  }
})
