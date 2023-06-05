function agregarFila() {
  var table = document.getElementById("fieldsTable");
  var newRow = table.insertRow(-1);
  var cell1 = newRow.insertCell(0);
  var cell2 = newRow.insertCell(1);

  cell1.innerHTML = '<input type="text" name="plato[]" class="form-control" placeholder="nombre del plato">';
  cell2.innerHTML = '<input type="number" name="calorias[]" class="form-control" placeholder="cantidad de calorias">';
}