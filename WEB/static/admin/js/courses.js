let idx = 0
const idx_val = {}
function removeElement (idx) {
  const element = document.getElementById(`${idx}`)
  element.remove()
}
function add_to_content (val) {
  val = val.split(',')
  idx += 1
  idx_val[idx] = val
  document.getElementById('content').insertAdjacentHTML(
    'beforeend',
    `<div id="${idx}" class="${idx}" style="background-color:lightgray; padding:12.5px; margin:12.5px; border-radius: 25px">
        <h4>${val[0]}</h4>
        <p>${val[2]}</p>
        <button type="button" class="btn btn-outline-danger" onclick='removeElement("${idx}");'>Delete</button>
      </div>`
  )
}
$('#submit_btn').click(function (e) {
  const marks = document.getElementById('Marks Required to Pass').value
  const image = document.getElementById('Image').value
  const name = document.getElementById('Name').value
  whole_content = $('#content').html()
  const info = {}
  for (idx_iter = 1; idx_iter <= idx; idx_iter++) {
    const specific_content = $(`#${idx_iter}`).html()

    info[idx_iter] = [idx_val[idx_iter]]
  }

  $.ajax({
    type: 'POST',
    url: '/Admin/Courses/Post/',
    data: JSON.stringify({
      info: info,
      whole_content: whole_content,
      marks: marks,
      image: image,
      name: name
    })
  })
  alert('Course Added')
  window.location.reload(0)
})
