function finishOrder() {
    // Get the modal
    var modal = document.getElementById('simpleModal');

    // Get the button that opens the modal
    //var modalBtn = document.getElementById('modalBtn');

    // Get the <span> element that closes the modal
    //var closeBtn = document.getElementsByClassName('closeBtn')[0];

    // When the user clicks the button, open the modal 

    // modalBtn.addEventListener('click', openModal);
    // closeBtn.addEventListener('click', closeModal);


    //function openModal(){
    //alert("kjkk");
    modal.style.display = 'block';
}

function closeModal() {
    var modal = document.getElementById('simpleModal');

    modal.style.display = 'none';
}

//finish order


function deleteRow(btn) {
    var row = btn.parentNode.parentNode;
    row.parentNode.removeChild(row);
    calculateRowPrice();
}


function increaseValue1(x) {

    var value = document.getElementById('number' + x).value;
    value++;
    document.getElementById('number' + x).value = value;
    calculate_per_row();
}

function decreaseValue1(x) {

    var value = document.getElementById('number' + x).value;
    if (value == 0) {} else {
        value--;
        document.getElementById('number' + x).value = value;
    }
    calculate_per_row();
}


function calculate_per_row() {
    var table = document.getElementById("table_shopping");

    var sumVal = 0;
    for (var i = 1; i < table.rows.length; i++) {
        quantity = table.rows[i].cells[1].getElementsByTagName('div')[0].getElementsByTagName('input')[1].value;
        sumVal = quantity * parseInt(table.rows[i].cells[2].innerHTML.substring(1));
        table.rows[i].cells[0].innerText = "₪" + sumVal;
    }
    //calculateTotalPrice();
}

function calculateTotalPrice() {


    var table = document.getElementById("table_shopping");
    var sumVal = 0;

    for (var i = 1; i < table.rows.length - 1; i++) {
        sumVal = sumVal + parseInt(table.rows[i].cells[0].innerHTML.substring(1));
    }
    document.getElementById("total_per_row").innerText = "₪" + sumVal;
}