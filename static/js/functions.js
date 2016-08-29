function toggleTable(id) {
    var lTable_lecture = document.getElementById("table_lecture"+id);
    lTable_lecture.style.display = (lTable_lecture.style.display == "table") ? "none" : "table";
    var lTable_pset = document.getElementById("table_pset"+id);
    lTable_pset.style.display = (lTable_pset.style.display == "table") ? "none" : "table";
}