var currentPage = 1; // Keep track of the current page number

function changePage(event, direction) {
  event.preventDefault();

  if (direction === 'prev' && currentPage > 1) {
    currentPage--;
  } else if (direction === 'next') {
    currentPage++;
  }

  // Remove active class from all page links
  var pageLinks = document.getElementsByClassName('page-link');
  for (var i = 0; i < pageLinks.length; i++) {
    pageLinks[i].classList.remove('active');
  }

  // Add active class to the clicked page link
  event.target.classList.add('active');

  // Load content for the selected page
  loadContent(currentPage);
}

function loadContent(pageNum) {
  // Make an AJAX request or load content based on the page number
  // Replace the following code with your own logic
  var contentDiv = document.getElementById('content');
  contentDiv.innerHTML = 'Content of Page ' + pageNum;
}


function update(id){
        window.location.href="/taskmanager/tasks/change/" + id + "/";
    }


    function sort() {
        let list = document.getElementById("list");
        const titles = list.getElementsByTagName("a");
        const priorities = list.getElementsByClassName("priority");
        const completed = list.getElementsByClassName("completed");
        const deadlines = list.getElementsByClassName("deadline");
        tarefas = [];
        for(let i = 0; i < titles.length; i++ ){
            const tarefa = {
                title: titles[i].innerHTML,
                priority: priorities[i].innerHTML,
                completed: completed[i].checked,
                link: titles[i].href,
                deadline: deadlines[i].innerHTML,
            };
            tarefas.push(tarefa);
            console.log("completed "+completed[i].checked);
        }


        const selectElement = document.getElementById("criteria");
        const selectedValue = selectElement.value;
        if (selectElement.selectedIndex === -1) {
            alert("Por favor selecione uma opção de ordenação");
        } else {
            console.log("essa "+selectedValue);
            typeOfSort(tarefas, selectedValue, priorities, titles, deadlines, completed);
        }
    }

    function typeOfSort(tarefas, sort, priorities, titles, deadlines, completed){
        var type = document.getElementById("sort");
        if(sort == "priority") {
            if (type.textContent.trim() == "") {
                console.log(" primeiro if");
                tarefas.sort(function (a, b) {
                    let priorityA = a.priority.toUpperCase();
                    let priorityB = b.priority.toUpperCase();
                    if (priorityB < priorityA) {
                        return -1;
                    }
                    if (priorityB > priorityA) {
                        return 1;
                    }
                    return 0;
                });
                document.getElementById("sort").innerHTML = "Descendente";
            } else if (type.textContent.trim() == "Descendente") {
                tarefas.sort(function (a, b) {
                    let priorityA = a.priority.toUpperCase();
                    let priorityB = b.priority.toUpperCase();
                    if (priorityA < priorityB) {
                        return -1;
                    }
                    if (priorityA > priorityB) {
                        return 1;
                    }
                    return 0;
                });
                document.getElementById("sort").innerHTML = "Ascendente";
                console.log(" segundos if" + type.innerHTML);
            } else {
                document.getElementById("sort").innerHTML = "";
            }
        }else if(sort == "title"){
            if (type.textContent.trim() == "") {
                console.log(" primeiro if");
                tarefas.sort(function (a, b) {
                    let priorityA = a.title.toUpperCase();
                    let priorityB = b.title.toUpperCase();
                    if (priorityB < priorityA) {
                        return -1;
                    }
                    if (priorityB > priorityA) {
                        return 1;
                    }
                    return 0;
                });
                document.getElementById("sort").innerHTML = "Descendente";
            } else if (type.textContent.trim() == "Descendente") {
                tarefas.sort(function (a, b) {
                    let priorityA = a.title.toUpperCase();
                    let priorityB = b.title.toUpperCase();
                    if (priorityA < priorityB) {
                        return -1;
                    }
                    if (priorityA > priorityB) {
                        return 1;
                    }
                    return 0;
                });
                document.getElementById("sort").innerHTML = "Ascendente";
                console.log(" segundos if" + type.innerHTML);
            } else {
                document.getElementById("sort").innerHTML = "";
            }
        }else if(sort == "completion"){
            if (type.textContent.trim() == "") {
                console.log(" primeiro if");
                tarefas.sort(function (a, b) {
                    let priorityA = a.completed;
                    let priorityB = b.completed;
                    console.log("A "+priorityA+" B "+priorityB);
                    if (priorityB < priorityA) {
                        return -1;
                    }
                    if (priorityB > priorityA) {
                        return 1;
                    }
                    return 0;
                });
                document.getElementById("sort").innerHTML = "Descendente";
            } else if (type.textContent.trim() == "Descendente") {
                tarefas.sort(function (a, b) {
                    let priorityA = a.completed;
                    let priorityB = b.completed;
                    if (priorityA < priorityB) {
                        return -1;
                    }
                    if (priorityA > priorityB) {
                        return 1;
                    }
                    return 0;
                });
                document.getElementById("sort").innerHTML = "Ascendente";
                console.log(" segundos if" + type.innerHTML);
            } else {
                document.getElementById("sort").innerHTML = "";
            }
        }else if(sort == "deadline") {
            if (type.textContent.trim() == "") {
                console.log(" primeiro if");
                tarefas.sort(function (a, b) {
                    let priorityA = a.deadline.toUpperCase();
                    let priorityB = b.deadline.toUpperCase();
                    if (priorityB < priorityA) {
                        return -1;
                    }
                    if (priorityB > priorityA) {
                        return 1;
                    }
                    return 0;
                });
                document.getElementById("sort").innerHTML = "Descendente";
            } else if (type.textContent.trim() == "Descendente") {
                tarefas.sort(function (a, b) {
                    let priorityA = a.deadline.toUpperCase();
                    let priorityB = b.deadline.toUpperCase();
                    if (priorityA < priorityB) {
                        return -1;
                    }
                    if (priorityA > priorityB) {
                        return 1;
                    }
                    return 0;
                });
                document.getElementById("sort").innerHTML = "Ascendente";
                console.log(" segundos if" + type.innerHTML);
            } else {
                document.getElementById("sort").innerHTML = "";
            }
        }

        for (let i = 0; i < tarefas.length; i++) {
            console.log("esta completa "+tarefas[i].completed.checked);
            console.log("tarefa " + tarefas[i].title + " link " + tarefas[i].title.href);
            titles[i].innerHTML = tarefas[i].title;
            titles[i].href = tarefas[i].link;
            priorities[i].innerHTML = tarefas[i].priority;
            deadlines[i].innerHTML = tarefas[i].deadline;
            completed[i].checked = tarefas[i].completed;
        }
    }

    function search() {
        const list = document.getElementById("list");
        const search = document.getElementById("search");
        const filter = search.value.toLowerCase(); // Get the input value and convert to lowercase
        const items = list.getElementsByTagName("li"); // Get the list items

        for (let i = 0; i < items.length; i++) {
            const item = items[i];
            const text = item.textContent.toLowerCase(); // Get the text content of the item and convert to lowercase
            if (text.indexOf(filter) === -1) { // If the filter is not found in the text content
                item.style.display = "none"; // Hide the item
            } else {
                item.style.display = ""; // Show the item
            }
        }
    }


    function visibility(){
        var checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
        var deleteButton = document.getElementById('deleteAll');
        if (checkboxes.length > 0) {
            deleteButton.style.display = "block";
        } else {
            deleteButton.style.display = "none";
        }
    }

    function select() {
    var selectedIds = Array.from(document.querySelectorAll('input[name="ids"]:checked'))
                         .map(function(elem) { return elem.id; });
        if (selectedIds.length > 0 && confirm("Essa ação é irreversível, deseja prosseguir?")) {
            var args = selectedIds.join(',');
            window.location.href = "/taskmanager/tasks/delete/" + args + "/";

        }
    }