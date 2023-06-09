function sort() {
        let list = document.getElementById("list");
        const titles = list.getElementsByTagName("a");

        users = [];
        for(let i = 0; i < titles.length; i++ ){
            const user = {
                title: titles[i].innerHTML,
                link: titles[i].href,
            };
            users.push(user);
        }

        var type = document.getElementById("sort");

        if (type.textContent.trim()=="") {
            console.log(" primeiro if");
            users.sort(function (a, b) {
                  let priorityA = a.title.toUpperCase();
                  let priorityB = b.title.toUpperCase();
                  if (priorityB < priorityA) {
                    return -1;
                  }
                  if (priorityB > priorityA) {
                    return 1;
                  }
                  return 0;
            });            document.getElementById("sort").innerHTML="Descendente";
        }else if (type.textContent.trim()=="Descendente"){
            users.sort(function (a, b) {
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
            document.getElementById("sort").innerHTML="Ascendente";
            console.log(" segundos if"+type.innerHTML);
        }else{
            document.getElementById("sort").innerHTML="";
        }

        for (let i = 0; i < titles.length; i++) {
            console.log("User "+users[i].title+users[i].link);
            titles[i].innerHTML=users[i].title;
            titles[i].href=users[i].link;
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
            window.location.href = "/taskmanager/users/delete/" + args + "/";

        }
    }