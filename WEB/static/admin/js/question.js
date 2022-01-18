let idx = 0
let idx_iter = 0
$('#input').click(function (e) {
  idx += 1

  document.getElementById('content').insertAdjacentHTML(
    'beforeend',
    `<div class="mb-3" id="${idx.toString()}">
          <label for="${idx.toString()}-Label" class="form-label">
            <input class="form-control" id="${idx.toString()}-Input-Name"  type="text" >
          </label>
          <input type="text" class="form-control" id="${idx.toString()}-Label">
          <br>
          <button type="button" class="btn btn-danger" onClick="removeElement(${idx.toString()})">Delete</button>
          <hr>
        </div>`
  )
})
$('#text').click(function (e) {
  idx += 1

  document.getElementById('content').insertAdjacentHTML(
    'beforeend',
    `<div id="${idx.toString()}">
          <input class="form-control" id="${idx.toString()}-Input-Name"  type="text" >
          <br>
          <button type="button" class="btn btn-danger" onClick="removeElement(${idx.toString()})">Delete</button>
          <br>
          <hr>
        </div>
      </div>`
  )
})
$('#checkbox').click(function (e) {
  idx += 1

  document.getElementById('content').insertAdjacentHTML(
    'beforeend',
    `<div class="mb-3" id="${idx.toString()}">
          <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="${idx.toString()}-Label">
            <label class="form-check-label" for="${idx.toString()}-Input-Name">
              <input class="form-control" id="${idx.toString()}-Input-Name"  type="text" >
            </label>
          </div>
          <button type="button" class="btn btn-danger" onClick="removeElement(${idx.toString()})">Delete</button>
          <hr>
        </div>`
  )
})
$('#big_input').click(function (e) {
  idx += 1

  document.getElementById('content').insertAdjacentHTML(
    'beforeend',
    `<div class="mb-3" id="${idx.toString()}">
          <label for="${idx.toString()}-Label" class="form-label">
            <input class="form-control" id="${idx.toString()}-Input-Name"  type="text" >
          </label>
          <textarea class="form-control" id="${idx.toString()}-Label" rows="3">        
          </textarea>
          <br>
          <button type="button" class="btn btn-danger" onClick="removeElement(${idx.toString()})">Delete</button>
          <hr>
        </div>`
  )
})
$('#switches').click(function (e) {
  idx += 1

  document.getElementById('content').insertAdjacentHTML(
    'beforeend',
    `<div class="mb-3" id="${idx.toString()}">
        <div class="form-check form-switch">
        <input class="form-check-input" type="checkbox" role="switch" id="${idx.toString()}-Input-Name">
        <label class="form-check-label" for="flexSwitchCheckDefault">
          <input class="form-control" id="${idx.toString()}-Input-Name"  type="text" >
        </div>
          <br>
          <button type="button" class="btn btn-danger" onClick="removeElement(${idx.toString()})">Delete</button>
          <hr>
        </div>`
  )
})
$('#checks').click(function (e) {
  idx += 1

  document.getElementById('content').insertAdjacentHTML(
    'beforeend',
    `<div class="mb-3" id="${idx.toString()}">
    <div class="form-check">
           <input type="checkbox" class="form-check-input" id="${idx.toString()}-Label">
    <label class="form-check-label" for="${idx.toString()}-Label">
<input class="form-control" id="${idx.toString()}-Input-Name"  type="text" ></label>
      
        </label>
          </div>
          <br>
          <button type="button" class="btn btn-danger" onClick="removeElement(${idx.toString()})">Delete</button>
          <hr>
        </div>`
  )
})
$('#range').click(function (e) {
  idx += 1

  document.getElementById('content').insertAdjacentHTML(
    'beforeend',
    `<div class="mb-3" id="${idx.toString()}">
    <label for="${idx.toString()}-Label" class="form-label"><input class="form-control" id="${idx.toString()}-Input-Name"  type="text" ></label></label>
<input type="range" class="form-range" id="${idx.toString()}-Label">
          <br>
          <button type="button" class="btn btn-danger" onClick="removeElement(${idx.toString()})">Delete</button>
          <hr>
        </div>`
  )
})
$('#submit_btn').click(function (e) {
  const info = {}
  for (idx_iter = 1; idx_iter <= idx; idx_iter++) {
    try {
      var label = document.getElementById(
        `${idx_iter.toString()}-Input-Name`
      ).value
    } catch (error) {
      var label = 'None'
    }
    try {
      var content = document.getElementById(
        `${idx_iter.toString()}-Label`
      ).value
    } catch (error) {
      var content = 'None'
    }
    try {
      var name = document.getElementById('name').value
    } catch (error) {
      var name = 'None'
    }

    info[idx_iter] = [label, content]
  }
  info.name = name
  const yourdiv = $('#content').html()
  $.ajax({
    type: 'POST',
    url: '/Admin/Question/Post/',
    data: JSON.stringify({ info: info, yourdiv: yourdiv })
  })
  alert('Question Added')
  window.location.reload(0)
})
function removeElement (idx) {
  const element = document.getElementById(`${idx}`)
  element.remove()
} // TODO Redirect the POST Request to the API
